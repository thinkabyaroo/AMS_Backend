from sqlalchemy.orm import Session
from app.models.division import Division
from app.schemas.division import DivisionCreate, DivisionUpdate


# Create
def create_division(db: Session, division: DivisionCreate):
    db_division = Division(**division.model_dump())
    db.add(db_division)
    db.commit()
    db.refresh(db_division)
    return db_division


# Get All
def get_divisions(db: Session, skip: int=0, limit: int=100):
    return db.query(Division).offset(skip).limit(limit).all()


# Get by ID
def get_division(db: Session, division_id: int):
    return db.query(Division).filter(Division.id == division_id).first()


# Update
def update_division(db: Session, division_id: int, division: DivisionUpdate):
    db_division = get_division(db, division_id)
    if not db_division:
        return None
    
    for key, value in division.model_dump(exclude_unset=True).items():
        setattr(db_division, key, value)

    db.commit()
    db.refresh(db_division)
    return db_division


# Delete
def delete_division(db: Session, division_id: int):
    db_division = get_division(db, division_id)
    if not db_division: 
        return None
    
    db.delete(db_division)
    db.commmit()
    return db_division