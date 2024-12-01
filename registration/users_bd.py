import uuid
from sqlalchemy import Column, Text
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from teams.team_bd import Teams
from teams.team_member_bd import TeamMember

engine = create_engine('mysql://root:password@localhost/link_service', echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
Base.metadata=MetaData(schema='link_service')

def uuid_to_str():
    return str(uuid.uuid4())

class Users(Base):
    __tablename__ = 'users'

    id = Column(Text, default=uuid_to_str, primary_key=True)
    username = Column(Text, nullable = False, unique=True)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    bio = Column(Text, nullable=True)

    owner = relationship("Teams", back_populates="teams")
    memberships = relationship("TeamMember", back_populates="member")


