from pydantic import BaseModel
from datetime import date
from typing import Optional

class AttendanceBase(BaseModel):
    staff_id: str
    date: date
    attendance_status: Optional[str] = None
    attendace_type: Optional[str] = None
    remark: Optional[str] = None


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceUpdate(BaseModel):
    staff_id: str | None = None
    date: date | None 
    attendance_status: str | None = None
    attendace_type: str | None = None
    remark: str | None = None


class AttendanceResponse(AttendanceBase):
    id: int

    model_config = {
        "from_attributes": True
    }