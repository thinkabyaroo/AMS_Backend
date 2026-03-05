from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import attendance as schemas_attendance 
from app.crud import attendance as crud_attendance


router = APIRouter()

@router.post("/", response_model=schemas_attendance.AttendanceResponse)
def create_attendance(attendance: schemas_attendance.AttendanceCreate, db: Session = Depends(get_db)):
    return crud_attendance.create_attendance(db, attendance)


@router.get("/", response_model=list[schemas_attendance.AttendanceResponse])
def read_attendances(db: Session = Depends(get_db)):
    return crud_attendance.get_attendances(db)


@router.get("/{attendance_id}", response_model=schemas_attendance.AttendanceResponse)
def read_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = crud_attendance.get_attendance(db, attendance_id)
    if not attendance: 
        raise HTTPException(status_code=404, detail="Attendance not found")
    return attendance


@router.delete("/{attendance_id}")
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = crud_attendance.delete_attendance(db, attendance_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")
    return {"message": "Attendance deleted successfully"}
