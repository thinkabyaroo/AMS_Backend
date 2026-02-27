from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Department(Base):
    __tablename__ = "department_table"

    id = Column(Integer, primary_key=True, index=True)
    dept_id = Column(String(100), unique=True, nullable=False)
    dept_name = Column(String(255), unique=True, nullable=False)

    div_id = Column(Integer, ForeignKey("division_table.id"), nullable=False)

    division = relationship("Division", back_populates="departments")
    teams = relationship("Team", back_populates="department")