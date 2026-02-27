from sqlalchemy.orm import Session
from app.models.department import Department
from app.schemas.department import DepartmentCreate, DepartmentUpdate


# Create
def create_department(db: Session, department: DepartmentCreate):
    db_department = Department(**department.model_dump())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department


# Get All
def get_departments(db: Session, skip: int=0, limit: int=100):
    return db.query(Department).offset(skip).limit(limit).all()


# Get by ID
def get_department(db: Session, department_id: int):
    return db.query(Department).filter(Department.id == department_id).first()


# Update
def update_department(db: Session, department_id: int, department: DepartmentUpdate):
    db_department = get_department(db, department_id)
    if not db_department:
        return None
    
    for key, value in department.model_dump(exclude_unset=True).items():
        setattr(db_department, key, value)

    db.commit()
    db.refresh(db_department)
    return db_department


# Delete
def delete_department(db: Session, department_id: int):
    db_department = get_department(db, department_id)
    if not db_department: 
        return None
    
    db.delete(db_department)
    db.commmit()
    return db_department