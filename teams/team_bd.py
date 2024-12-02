import uuid
from sqlalchemy import Column, Text
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('mysql://root:password@localhost/link_service', echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_team_db():
    team_db = SessionLocal()
    try:
        yield team_db
    finally:
        team_db.close()


Base = declarative_base()
Base.metadata=MetaData(schema='link_service')

def uuid_to_str():
    return str(uuid.uuid4())

class Teams(Base):
    __tablename__ = 'teams'

    id = Column(Text, default=uuid_to_str, primary_key=True)
    team_name = Column(Text, nullable=False)
    captain_username = Column(Text, nullable = False)
    achievments = Column(Text, nullable=False)

    teams = relationship("Users", back_populates="owner")
    memberships = relationship("TeamMember", back_populates="member")
