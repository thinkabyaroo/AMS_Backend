from sqlalchemy import Column, BigInteger, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Attendance(Base):
    __tablename__ = "attendance_table"

    id = Column(BigInteger, primary_key=True, index=True)
    staff_id = Column(String(100), ForeignKey("staff_table.staff_id", ondelete="CASCADE"), nullable=False)
    date = Column(Date, nullable=False)
    attendance_status = Column(String(100))
    attendace_type = Column(String(100))
    remark = Column(String(500))