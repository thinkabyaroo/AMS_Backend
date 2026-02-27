from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Division(Base):
    __tablename__ = "division_table"

    id = Column(Integer, primary_key=True, index=True)
    div_id = Column(String(100), unique=True, nullable=False)
    div_name = Column(String(255), unique=True, nullable=False)

    departments = relationship("Department", back_populates="division")