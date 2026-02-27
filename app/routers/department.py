from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import department as crud_department
from app.schemas import department as schema_department

router = APIRouter()


@router.post("/", response_model=schema_department.DepartmentResponse)
def create_department(department: schema_department.DepartmentCreate, db: Session = Depends(get_db)):
    return crud_department.create_department(db, department)


@router.get("/", response_model=list[schema_department.DepartmentResponse])
def read_departments(db: Session = Depends(get_db)):
    return crud_department.get_departments(db)


@router.get("/{department_id}", response_model=schema_department.DepartmentResponse)
def read_department(department_id: int, db: Session = Depends(get_db)):
    department = crud_department.get_department(db, department_id)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department