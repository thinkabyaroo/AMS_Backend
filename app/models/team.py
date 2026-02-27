from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Team(Base):
    __tablename__ = "team_table"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(String(100), unique=True, nullable=False)
    team_name = Column(String(255), unique=True, nullable=False)

    dept_id = Column(Integer, ForeignKey("department_table.id"), nullable=False)

    department = relationship("Department", back_populates="teams")