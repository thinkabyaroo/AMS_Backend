from sqlalchemy.orm import Session
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate


def create_attendance(db: Session, attendance: AttendanceCreate):
    db_obj = Attendance(**attendance.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_all_attendance(db: Session):
    return db.query(Attendance).all()