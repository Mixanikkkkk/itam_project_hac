from fastapi import FastAPI, Depends, HTTPException
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
        password=h_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return f'Пользователь {user.username} успешно зарегистрирован'