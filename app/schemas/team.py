from pydantic import BaseModel


class TeamBase(BaseModel):
    team_id: str
    team_name: str
    dept_id: int


class TeamCreate(TeamBase):
    pass


class TeamUpdate(BaseModel):
    team_id: str | None = None
    team_name: str | None = None
    dept_id: int | None = None

class TeamResponse(TeamBase):
    id: int

    model_config = {
        "from_attributes": True
    }