from sqlalchemy.orm import Session
from app.schemas import staff as staff_schema
from app.models import staff as staff_models


def create_staff(db: Session, staff: staff_schema.StaffCreate):
    db_staff = staff_models.Staff(**staff.dict())
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff


def get_all_staff(db: Session):
    return db.query(staff_models.Staff).all()


def get_staff(db: Session, staff_id: int):
    return db.query(staff_models.Staff).filter(staff_models.Staff.id == staff_id).first()


def update_staff(db: Session, staff_id: int, staff: staff_schema.StaffUpdate):
    db_staff = get_staff(db, staff_id)
    if db_staff:
        for key, value in staff.dict(exclude_unset=True).items():
            setattr(db_staff, key, value)
        db.commit()
        db.refresh(db_staff)
    return db_staff


def delete_staff(db: Session, staff_id: int):
    db_staff = get_staff(db, staff_id)
    if db_staff:
        db.delete(db_staff)
        db.commit()
    return db_staff
