from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Faculty(Base):
    __tablename__ = "faculties"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    email = Column(String, unique=True)
    designation = Column(String)

    department_id = Column(Integer, ForeignKey("departments.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    department = relationship("Department", back_populates="faculties")
    room = relationship("Room", back_populates="faculties")