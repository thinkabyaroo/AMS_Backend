from fastapi import FastAPI
from app.routers import auth, staff, division, department, team, attendance, leave_balance, leave_form

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(staff.router, prefix="/staff", tags=["Staff"])
app.include_router(division.router, prefix="/division", tags=["Division"])
app.include_router(department.router, prefix="/department", tags=["Department"])
app.include_router(team.router, prefix="/team", tags=["Team"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])
app.include_router(leave_balance.router, prefix="/leave_balance", tags=["Leave-balance"])
app.include_router(leave_form.router, prefix="/leave_form", tags=["Leave-form"])

print("Hello World")
