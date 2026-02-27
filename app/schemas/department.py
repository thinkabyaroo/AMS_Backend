from pydantic import BaseModel


class DepartmentBase(BaseModel):
    dept_id: str
    dept_name: str
    div_id: int


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(BaseModel):
    dept_id: str | None = None
    dept_name: str | None = None
    div_id: int | None = None

class DepartmentResponse(DepartmentBase):
    id: int

    model_config = {
        "from_attributes": True
    }