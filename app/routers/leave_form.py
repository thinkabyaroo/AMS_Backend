from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import leave_form as schema_leave_form
from app.crud import leave_form as crud_leave_form

router = APIRouter()


@router.post("/", response_model=schema_leave_form.LeaveFormResponse)
def create(leave_form: schema_leave_form.LeaveFormCreate, db: Session = Depends(get_db)):
    return crud_leave_form.create_leave_form(db, leave_form)


@router.put("/{leave_form_id}", response_model=schema_leave_form.LeaveFormResponse)
def update_status(
    leave_form_id: int,
    update_data: schema_leave_form.LeaveFormUpdate,
    db: Session = Depends(get_db),
):
    db_obj = crud_leave_form.update_leave_form_status(db, leave_form_id, update_data)

    if not db_obj:
        raise HTTPException(status_code=404, detail="Leave form not found")

    return db_obj