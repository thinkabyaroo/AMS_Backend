from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from decimal import Decimal
from enum import Enum


class FormStatus(str, Enum):
    pending = "pending"
    rejected = "rejected"
    approved = "approved"


class LeaveFormBase(BaseModel):
    staff_id: str
    req_leave_date_from: date
    req_leave_date_to: date
    total_leave_day: Optional[Decimal] = None
    leave_type: Optional[str] = None
    attachment: Optional[str] = None
    reason: Optional[str] = None


class LeaveFormCreate(LeaveFormBase):
    pass


class LeaveFormUpdate(BaseModel):
    form_status: FormStatus
    approved_by: Optional[str] = None


class LeaveFormResponse(LeaveFormBase):
    leave_form_id: int
    form_status: Optional[FormStatus]
    approved_by: Optional[str]
    approved_date: Optional[datetime]

    model_config = {
        "from_attributes": True
    }