from pydantic import BaseModel


class SectionBase(BaseModel):
    name: str
    year: str
    department_id: int
    room_id: int


class SectionCreate(SectionBase):
    pass


class SectionResponse(SectionBase):
    id: int

    class Config:
        from_attributes = True