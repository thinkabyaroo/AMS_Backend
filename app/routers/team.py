from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import team as crud_team
from app.schemas import team as schema_team

router = APIRouter()


@router.post("/", response_model=schema_team.TeamResponse)
def create_team(team: schema_team.TeamCreate, db: Session = Depends(get_db)):
    return crud_team.create_team(db, team)


@router.get("/", response_model=list[schema_team.TeamResponse])
def read_teams(db: Session = Depends(get_db)):
    return crud_team.get_teams(db)


@router.get("/{team_id}", response_model=schema_team.TeamResponse)
def read_team(team_id: int, db: Session = Depends(get_db)):
    team = crud_team.get_team(db, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team