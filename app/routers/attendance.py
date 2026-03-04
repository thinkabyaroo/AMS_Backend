from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import attendance as schemas_attendance 
from app.crud import attendance as crud_attendance


router = APIRouter()

@router.post("/", response_model=schemas_attendance.AttendanceResponse)
def create(attendance: schemas_attendance.AttendanceCreate, db: Session = Depends(get_db)):
    return crud_attendance.create_attendance(db, attendance)


@router.get("/", response_model=list[schemas_attendance.AttendanceResponse])
def read_all(db: Session = Depends(get_db)):
    return crud_attendance.get_all_attendance(db)