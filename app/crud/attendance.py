from sqlalchemy.orm import Session
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate, AttendanceUpdate


# Create
def create_attendance(db: Session, attendance: AttendanceCreate):
    db_obj = Attendance(**attendance.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


# Get All
def get_attendances(db: Session, skip: int=0, limit: int=100):
    return db.query(Attendance).offset(skip).limit(limit).all()


# Get by ID
def get_attendance(db: Session, attendance_id: int):
    return db.query(Attendance).filter(Attendance.id == attendance_id).first()


# Update
def update_attendance(db: Session, attendance_id: int, attendance: AttendanceUpdate):
    db_attendance = get_attendance(db, attendance_id)
    if not db_attendance:
        return None
    
    for key, value in attendance.model_dump(exclude_unset=True).items():
        setattr(db_attendance, key, value)

    db.commit()
    db.refresh(db_attendance)
    return db_attendance


# Delete
def delete_attendance(db: Session, attendance_id: int):
    db_attendance = get_attendance(db, attendance_id)
    if not db_attendance:
        return None
    
    db.delete(db_attendance)
    db.commit()
    return db_attendance