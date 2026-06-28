from pydantic import BaseModel


class FacultyBase(BaseModel):
    name: str
    email: str
    designation: str
    department_id: int
    room_id: int


class FacultyCreate(FacultyBase):
    pass


class FacultyResponse(FacultyBase):
    id: int

    class Config:
        from_attributes = True