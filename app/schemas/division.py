from pydantic import BaseModel


class DivisionBase(BaseModel):
    div_id: str
    div_name: str


class DivisionCreate(DivisionBase):
    pass


class DivisionUpdate(BaseModel):
    div_id: str | None = None
    div_name: str | None = None


class DivisionResponse(DivisionBase):
    id: int

    model_config = {
        "from_attributes": True
    }
    