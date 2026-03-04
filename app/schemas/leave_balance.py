from pydantic import BaseModel

class LeaveBalanceBase(BaseModel):
    staff_id: str
    cascual_leave: int = 0
    family_funeral_health_leave: int = 0
    leave_with_pay: int = 0
    leave_without_pay: int = 0
    married_leave: int = 0
    medical_leave: int = 0
    parternity_leave: int = 0


class LeaveBalanceCreate(LeaveBalanceBase):
    pass


class LeaveBalanceResponse(LeaveBalanceBase):
    id: int

    model_config = {
        "from_attributes": True
    }