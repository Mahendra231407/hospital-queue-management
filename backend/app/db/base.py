from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import models so SQLAlchemy registers them with Base.metadata.
from app.models import City, Department, Doctor, Hospital  # noqa: E402, F401
