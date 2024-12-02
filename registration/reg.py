from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from passlib.context import CryptContext
from registration.users_bd import get_db
from sqlalchemy.orm import Session
from registration.users_bd import Users





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
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует")

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


from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi import Request, Response

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
    # Сохраняем user_id в сессии
    request.session["user_id"] = user.id
    return {"message": "Вы успешно вошли в систему!"}

@app.get("/protected")
def protected_route(request: dict = None, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Вы не авторизованы",
        )

    user = db.query(Users).filter(Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

@app.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="session")
    return {"message": "Вы вышли из системы"}

def get_user_by_username(db: Session, username: str):
    return db.query(Users).filter(Users.username == username).first()

@app.get("/profile/{username}", response_model=NewUser)
def get_user_profile(username: str, db: Session = Depends(get_db)):
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

    return {"username": user.username, "message": "Добро пожаловать!"}