from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import staff as crud_staff
from app.schemas import staff as schema_staff

router = APIRouter()


@router.post("/", response_model=schema_staff.StaffResponse)
def create_staff(staff: schema_staff.StaffCreate, db: Session = Depends(get_db)):
    return crud_staff.create_staff(db, staff)


@router.get("/", response_model=list[schema_staff.StaffResponse])
def read_staff(db: Session = Depends(get_db)):
    return crud_staff.get_all_staff(db)


@router.get("/{staff_id}", response_model=schema_staff.StaffResponse)
def read_single_staff(staff_id: int, db: Session = Depends(get_db)):
    staff = crud_staff.get_staff(db, staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff


@router.put("/{staff_id}", response_model=schema_staff.StaffResponse)
def update_staff(staff_id: int, staff: schema_staff.StaffUpdate,
                 db: Session = Depends(get_db)):
    updated = crud_staff.update_staff(db, staff_id, staff)
    if not updated:
        raise HTTPException(status_code=404, detail="Staff not found")
    return updated


@router.delete("/{staff_id}")
def delete_staff(staff_id: int, db: Session = Depends(get_db)):
    deleted = crud_staff.delete_staff(db, staff_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Staff not found")
    return {"message": "Staff deleted"}
