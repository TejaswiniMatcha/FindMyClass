from sqlalchemy import Column, Integer, Numeric, String, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from app.database import Base


class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)

    # Basic Information
    name = Column(String(100), nullable=False, unique=True)
    code = Column(String(20), nullable=False, unique=True)
    slug = Column(String(100), nullable=False, unique=True)

    # Display Information
    short_name = Column(String(20), nullable=False)
    icon = Column(String(20), nullable=False)

    # Description
    description = Column(Text, nullable=False)

    # Image filename stored in /static
    image = Column(String(255), nullable=False)

    # Building Information
    floors = Column(Integer, nullable=False)
    latitude = Column(Numeric(9, 6), nullable=True)
    longitude = Column(Numeric(9, 6), nullable=True)

    # Building Highlights
    highlights = Column(
        ARRAY(String),
        nullable=False,
        default=list
    )

    # Relationships
    rooms = relationship(
        "Room",
        back_populates="building",
        cascade="all, delete-orphan"
    )

    @property
    def room_count(self) -> int:
        """
        Returns the number of rooms in the building.
        Calculated dynamically from the relationship.
        """
        return len(self.rooms) if self.rooms else 0