from sqlalchemy.orm import Session
from app.models.team import Team
from app.schemas.team import TeamCreate, TeamUpdate


# Create
def create_team(db: Session, team: TeamCreate):
    db_team = Team(**team.model_dump())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


# Get All
def get_teams(db: Session, skip: int=0, limit: int=100):
    return db.query(Team).offset(skip).limit(limit).all()


# Get by ID
def get_team(db: Session, team_id: int):
    return db.query(Team).filter(Team.id == team_id).first()


# Update
def update_team(db: Session, team_id: int, team: TeamUpdate):
    db_team = get_team(db, team_id)
    if not db_team:
        return None
    
    for key, value in team.model_dump(exclude_unset=True).items():
        setattr(db_team, key, value)

    db.commit()
    db.refresh(db_team)
    return db_team


# Delete
def delete_team(db: Session, team_id: int):
    db_team = get_team(db, team_id)
    if not db_team: 
        return None
    
    db.delete(db_team)
    db.commmit()
    return db_team