from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import leave_balance as schema_leave_balance
from app.crud import leave_balance as crud_leave_balance

router = APIRouter()


@router.post("/", response_model=schema_leave_balance.LeaveBalanceResponse)
def create(leave_balance: schema_leave_balance.LeaveBalanceCreate, db: Session = Depends(get_db)):
    return crud_leave_balance.create_leave_balance(db, leave_balance)


@router.get("/{staff_id}", response_model=schema_leave_balance.LeaveBalanceResponse)
def get_by_staff(staff_id: str, db: Session = Depends(get_db)):
    return crud_leave_balance.get_leave_balance_by_staff(db, staff_id)