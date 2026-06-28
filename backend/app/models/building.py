from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False, unique=True)
    code = Column(String, nullable=False, unique=True)
    slug = Column(String, nullable=False, unique=True)

    short_name = Column(String, nullable=False)
    description = Column(String)
    image = Column(String)
    floors = Column(Integer)

    rooms = relationship("Room", back_populates="building")