from sqlalchemy import Column, Integer, String
from app.database import Base


class Staff(Base):
    __tablename__ = "staff_table"

    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(String(100), unique=True, index=True)
    staff_name = Column(String(255))
    staff_position = Column(String(255))
    org_placement = Column(String(255))
    staff_permanent_status = Column(String(100))
    gender = Column(String(50))
    floor = Column(String(50))
    staff_mail = Column(String(100))
    staff_passowrd = Column(String(45))
    team_id = Column(Integer)
