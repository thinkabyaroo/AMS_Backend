from fastapi import FastAPI
from app.routers import auth, staff

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(staff.router, prefix="/staff", tags=["Staff"])
print("Hello World")
