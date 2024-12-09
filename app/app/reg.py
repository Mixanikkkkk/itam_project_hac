from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from passlib.context import CryptContext
from app.users_bd import get_db
from sqlalchemy.orm import Session
from app.users_bd import Users, Teams, TeamMembers, TeamInvite


app = FastAPI()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


class NewUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    email : str
    password: str
    bio: str


@app.post('/register')
def register_user(user:NewUser, db: Session = Depends(get_db)):
    existing_user_email = db.query(Users).filter(Users.email == user.email).first()
    existing_user_username = db.query(Users).filter(Users.username == user.username).first()
    if existing_user_email or existing_user_username:
        raise HTTPException(status_code=400, detail="Пользователь с таким email или именем пользователя уже существует")

    h_password = get_password_hash(user.password)

    new_user = Users(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=h_password,
        bio=user.bio
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return f'Пользователь {user.username} успешно зарегистрирован'


from starlette.middleware.sessions import SessionMiddleware
from fastapi import Request, Response
from rediska import redis_client


app.add_middleware(SessionMiddleware, secret_key="super-secret-key")

def verify_password(plain_password, password):
    return pwd_context.verify(plain_password, password)

class LoginData(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(
    request: Request,
    login_data: LoginData,
    db: Session = Depends(get_db)

):
    user = db.query(Users).filter(Users.username == login_data.username).first()
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль",
        )
    session_username = user.username
    request.session["user_username"] = user.username
    redis_client.set(f"session:{session_username}", user.username, ex=3600)
    return {"message": "Вы успешно вошли в систему!"}

@app.get("/protected")
def protected_route(request: dict = None, db: Session = Depends(get_db)):
    user_username = request.session.get("user_username")
    if not user_username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Вы не авторизованы",
        )

    user = db.query(Users).filter(Users.username == user_username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

@app.post("/logout")
def logout(request: Request, response: Response):
    request.session.clear()
    return {"message": "Вы вышли из системы"}

def get_user_by_username(db: Session, username: str):
    return db.query(Users).filter(Users.username == username).first()
def get_current_user(request: Request, db: Session = Depends(get_db)):
    username = request.session.get("user_username")
    if not username:
        raise HTTPException(status_code=401, detail="Пользователь  неавторизован")

    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    return user

@app.get("/profile/{username}", response_model=NewUser)
def get_user_profile(username: str, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    user = get_user_by_username(db, username)
    if current_user.username != username:
        raise HTTPException(status_code=403, detail="Вы не можете просматривать чужой профиль")
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

    return {"username": user.username, "message": "Добро пожаловать!"}


class NewTeam(BaseModel):
    teamname: str
    achievments: str
    captain_username: str



@app.post('/create_team')
def team_creation(team:NewTeam, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user) ):
    existing_teamname = db.query(Teams).filter(Teams.teamname == team.teamname).first()
    if existing_teamname:
        raise HTTPException(status_code=400, detail="Команда с таким названием уже существует")
    if current_user.username != team.captain_username:
        raise HTTPException(status_code=403, detail="Только авторизованный пользователь может создать команду!")

    new_team = Teams(
        teamname=team.teamname,
        achievments=team.achievments,
        captain_username=team.captain_username
    )

    db.add(new_team)
    db.commit()
    db.refresh(new_team)

    return {"message": f"Команда {team.teamname} успешно создана", "team_id": new_team.id}


@app.post('/create_team/{teamname}/add_user')
def add_team_member(teamname:str, username:str, db: Session=Depends(get_db), current_user: Users = Depends(get_current_user)):

    team = db.query(Teams).filter(Teams.teamname==teamname).first()
    if not team:
        raise HTTPException(status_code=404, detail="Команда не найдена")

    if team.captain_username != current_user.username:
        raise HTTPException(status_code=403, detail="Только капитан может добавлять участников")

    user_to_add = db.query(Users).filter(Users.username == username).first()
    if not user_to_add:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    existing_member = db.query(TeamMembers).filter(TeamMembers.teamname == teamname, TeamMembers.username == user_to_add.username).first()
    if existing_member:
        raise HTTPException(status_code=400, detail="Пользователь уже состоит в команде")

    new_invite = TeamInvite(
        teamname=teamname,
        invited_username=username,
        captain_username=current_user.username,
        status="pending"
    )
    db.add(new_invite)
    db.commit()

    return {"message": f"Приглашение отправлено пользователю {username}"}

@app.post('/invites/{invite_id}/respond')
def respond_to_invite(invite_id: int, action: str, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    
    invite = db.query(TeamInvite).filter(TeamInvite.id == invite_id).first()
    if not invite:
        raise HTTPException(status_code=404, detail="Приглашение не найдено")


    if invite.invited_username != current_user.username:
        raise HTTPException(status_code=403, detail="Это приглашение вам не адресовано")


    if action not in ["accept", "reject"]:
        raise HTTPException(status_code=400, detail="Действие должно быть 'accept' или 'reject'")


    if action == "accept":
        new_member = TeamMembers(teamname=invite.teamname, username=current_user.username)
        db.add(new_member)
        invite.status = "accepted"
    elif action == "reject":
        invite.status = "rejected"

    db.commit()

    return {"message": f"Приглашение успешно {action}ed"}

@app.get('/my_invites')
def get_my_invites(db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    invites = db.query(TeamInvite).filter(
        TeamInvite.invited_username == current_user.username,
        TeamInvite.status == "pending"
    ).all()
    return invites