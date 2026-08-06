from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    hospital_id: Mapped[int] = mapped_column(
        ForeignKey("hospitals.id"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    hospital: Mapped["Hospital"] = relationship(back_populates="departments")
    doctors: Mapped[list["Doctor"]] = relationship(back_populates="department")

    def __repr__(self) -> str:
        return (
            f"<Department(id={self.id}, name={self.name!r}, "
            f"hospital_id={self.hospital_id})>"
        )
