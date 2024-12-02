import uuid
from sqlalchemy import Column, Text
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql://root:password@localhost/link_service', echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_team_member_db():
    team_member_db = SessionLocal()
    try:
        yield team_member_db
    finally:
        team_member_db.close()


Base = declarative_base()
Base.metadata=MetaData(schema='link_service')

def uuid_to_str():
    return str(uuid.uuid4())

class TeamMember(Base):
    __tablename__ = 'team_member'

    id = Column(Text, default=uuid_to_str, primary_key=True)
    team_id = Column(Text, nullable = False)
    username= Column(Text, nullable=False)

    team = relationship("Teams", back_populates="teams")
    member = relationship("Users", back_populates="memberships")