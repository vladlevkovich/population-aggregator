from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import UUID
import uuid

class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

class CountryPopulation(Base):
    __tablename__ = 'population'

    country: Mapped[str]
    region: Mapped[str]
    population: Mapped[int]

