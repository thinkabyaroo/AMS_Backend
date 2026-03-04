from sqlalchemy.orm import Session
from app.models.leave_balance import LeaveBalance
from app.schemas.leave_balance import LeaveBalanceCreate


def create_leave_balance(db: Session, leave_balance: LeaveBalanceCreate):
    db_obj = LeaveBalance(**leave_balance.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_leave_balance_by_staff(db: Session, staff_id: str):
    return db.query(LeaveBalance).filter(LeaveBalance.staff_id == staff_id).first()