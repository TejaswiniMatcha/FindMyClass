from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    code = Column(String, unique=True)

    faculties = relationship("Faculty", back_populates="department")
    sections = relationship("Section", back_populates="department")