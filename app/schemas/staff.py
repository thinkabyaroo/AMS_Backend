from pydantic import BaseModel
from typing import Optional


class StaffBase(BaseModel):
    staff_id: str
    staff_name: str
    staff_position: Optional[str] = None
    org_placement: Optional[str] = None
    staff_permanent_status: Optional[str] = None
    gender: Optional[str] = None
    floor: Optional[str] = None
    staff_mail: Optional[str] = None
    staff_passowrd: Optional[str] = None
    team_id: int


class StaffCreate(StaffBase):
    pass


class StaffUpdate(BaseModel):
    staff_name: Optional[str]
    staff_position: Optional[str]
    org_placement: Optional[str]
    staff_permanent_status: Optional[str]
    gender: Optional[str]
    floor: Optional[str]
    staff_mail: Optional[str]
    staff_passowrd: Optional[str]


class StaffResponse(StaffBase):
    id: int

    class Config:
        orm_mode = True
