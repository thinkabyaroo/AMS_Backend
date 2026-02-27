from fastapi import FastAPI
from app.routers import auth, staff, division, department, team

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(staff.router, prefix="/staff", tags=["Staff"])
app.include_router(division.router, prefix="/division", tags=["Division"])
app.include_router(department.router, prefix="/department", tags=["Department"])
app.include_router(team.router, prefix="/team", tags=["Team"])

print("Hello World")
