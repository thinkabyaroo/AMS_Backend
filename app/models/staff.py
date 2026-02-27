from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Staff(Base):
    __tablename__ = "staff_table"

    id = Column(Integer, primary_key=True, index=True)

    staff_id = Column(String(100), unique=True, index=True, nullable=False)
    staff_name = Column(String(255), nullable=False)

    staff_position = Column(String(255), nullable=True)
    org_placement = Column(String(255), nullable=True)
    staff_permanent_status = Column(String(100), nullable=True)
    gender = Column(String(50), nullable=True)
    floor = Column(String(50), nullable=True)
    staff_mail = Column(String(100), nullable=True)
    staff_passowrd = Column(String(45), nullable=True)

    team_id = Column(Integer, ForeignKey("team_table.id"), nullable=False)