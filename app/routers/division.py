from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import division as crud_division
from app.schemas import division as schema_division


router = APIRouter()


@router.post("/", response_model=schema_division.DivisionResponse)
def create_division(division: schema_division.DivisionCreate, db: Session = Depends(get_db)):
    return crud_division.create_division(db, division)


@router.get("/", response_model=list[schema_division.DivisionResponse])
def read_divisions(db: Session = Depends(get_db)):
    return crud_division.get_divisions(db)


@router.get("/{division_id}", response_model=schema_division.DivisionResponse)
def read_division(division_id: int, db: Session = Depends(get_db)):
    division = crud_division.get_division(db, division_id)
    if not division:
        raise HTTPException(status_code=404, detail="Division not found")
    return division


@router.delete("/{division_id}")
def delete_division(division_id: int, db: Session = Depends(get_db)):
    division = crud_division.delete_division(db, division_id)
    if not division:
        raise HTTPException(status_code=404, detail="Division not found")
    return {"message": "Division deleted successfully"}
