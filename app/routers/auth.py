from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.staff import Staff
from app.schemas.staff import StaffCreate
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(data: StaffCreate, db: Session = Depends(get_db)):
    hashed_pw = hash_password(data.password)
    new_user = Staff(
        staff_id=data.staff_id,
        staff_name=data.staff_name,
        staff_mail=data.staff_mail,
        staff_password=hashed_pw,
        team_id=data.team_id
    )
    db.add(new_user)
    db.commit()
    return {"message": "User created"}


# @router.post("/login")
# def login(data: StaffLogin, db: Session = Depends(get_db)):
#     user = db.query(Staff).filter(Staff.staff_mail == data.staff_mail).first()
#     if not user or not verify_password(data.password, user.staff_password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     token = create_access_token({"sub": user.staff_mail})
#     return {"access_token": token, "token_type": "bearer"}
