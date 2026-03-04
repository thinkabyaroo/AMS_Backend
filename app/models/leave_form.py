from sqlalchemy import Column, BigInteger, String, Date, DateTime, DECIMAL, Enum, ForeignKey
from app.database import Base
import enum


class FormStatus(str, enum.Enum):
    pending = "pending"
    rejected = "rejected"
    approved = "approved"


class LeaveForm(Base):
    __tablename__ = "leave_form_table"

    leave_form_id = Column(BigInteger, primary_key=True, index=True)
    staff_id = Column(String(100), ForeignKey("staff_table.staff_id", ondelete="CASCADE"), nullable=False)

    req_leave_date_from = Column(Date, nullable=False)
    req_leave_date_to = Column(Date, nullable=False)
    total_leave_day = Column(DECIMAL(5, 2))
    leave_type = Column(String(100))
    attachment = Column(String(500))
    reason = Column(String(1000))
    form_status = Column(Enum(FormStatus), default=FormStatus.pending)
    approved_by = Column(String(255))
    approved_date = Column(DateTime)