from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class LeaveBalance(Base):
    __tablename__ = "leave_balance_table"

    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(String(100), ForeignKey("staff_table.staff_id", ondelete="CASCADE"), unique=True, nullable=False)

    cascual_leave = Column(Integer, default=0)
    family_funeral_health_leave = Column(Integer, default=0)
    leave_with_pay = Column(Integer, default=0)
    leave_without_pay = Column(Integer, default=0)
    married_leave = Column(Integer, default=0)
    medical_leave = Column(Integer, default=0)
    parternity_leave = Column(Integer, default=0)