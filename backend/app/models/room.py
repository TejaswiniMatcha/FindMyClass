from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)

    room_no = Column(String, nullable=False)
    floor = Column(Integer)

    building_id = Column(Integer, ForeignKey("buildings.id"))

    building = relationship("Building", back_populates="rooms")
    faculties = relationship("Faculty", back_populates="room")
    sections = relationship("Section", back_populates="room")