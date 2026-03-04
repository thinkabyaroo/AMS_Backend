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


class AttendanceResponse(AttendanceBase):
    id: int

    model_config = {
        "from_attributes": True
    }