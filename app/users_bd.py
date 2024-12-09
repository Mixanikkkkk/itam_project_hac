import uuid
from sqlalchemy import Column, Text, Enum
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql://root:password@localhost/link_service', pool_size=10, max_overflow=20, echo=True)
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

class Teams(Base):
    __tablename__ = 'teams'

    id = Column(Text, default=uuid_to_str, primary_key=True)
    teamname = Column(Text, nullable=False)
    captain_username = Column(Text, nullable = False)
    achievments = Column(Text, nullable=False)

class TeamMembers(Base):
    __tablename__ = 'team_members'

    id = Column(Text, default=uuid_to_str, primary_key=True)
    teamname = Column(Text, nullable = False)
    username= Column(Text, nullable=False)


class TeamInvite(Base):
    __tablename__ = "invites"

    id = Column(Text, default=uuid_to_str, primary_key=True)
    teamname = Column(Text, nullable = False)
    captain_username = Column(Text, nullable=False)
    invited_username= Column(Text, nullable=False)
    status = Column(Enum('pending', 'accepted', 'rejected'), default="pending")




