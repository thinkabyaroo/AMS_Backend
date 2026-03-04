from sqlalchemy.orm import Session
from app.models.leave_form import LeaveForm
from app.schemas.leave_form import LeaveFormCreate, LeaveFormUpdate
from datetime import datetime


def create_leave_form(db: Session, leave_form: LeaveFormCreate):
    db_obj = LeaveForm(**leave_form.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_leave_form_status(db: Session, leave_form_id: int, update_data: LeaveFormUpdate):
    db_obj = db.query(LeaveForm).filter(
        LeaveForm.leave_form_id == leave_form_id
    ).first()

    if db_obj:
        db_obj.form_status = update_data.form_status
        db_obj.approved_by = update_data.approved_by
        db_obj.approved_date = datetime.now()
        db.commit()
        db.refresh(db_obj)

    return db_obj