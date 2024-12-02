from pydantic import BaseModel
from fastapi import  Depends, HTTPException
from sqlalchemy.orm import Session
from teams.team_bd import Teams, get_team_db
from registration.reg import app

class NewTeam(BaseModel):
    teamname: str
    achievments: str
    captain_username: str

@app.post('/create_team')
def register_user(team:NewTeam, db: Session = Depends(get_team_db)):

    new_team = Teams(
        team_name = team.teamname,
        achievments = team.achievments,
        captain_username = team.captain_username

    )
    db.add(new_team)
    db.commit()
    db.refresh(new_team)

    return f'Команда {team.teamname} успешно создана'
