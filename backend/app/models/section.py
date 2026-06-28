from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    year = Column(String)

    department_id = Column(Integer, ForeignKey("departments.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    department = relationship("Department", back_populates="sections")
    room = relationship("Room", back_populates="sections")