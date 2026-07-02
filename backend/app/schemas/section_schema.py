from pydantic import BaseModel


class DepartmentMini(BaseModel):
    id: int
    code: str
    name: str

    class Config:
        from_attributes = True


class BuildingMini(BaseModel):
    id: int
    name: str
    slug: str

    class Config:
        from_attributes = True


class RoomMini(BaseModel):
    id: int
    room_no: str
    floor: int
    building: BuildingMini

    class Config:
        from_attributes = True


class SectionCreate(BaseModel):
    name: str
    year: str
    department_id: int
    room_id: int


class SectionResponse(BaseModel):
    id: int
    name: str
    year: str

    department: DepartmentMini

    room: RoomMini

    class Config:
        from_attributes = True