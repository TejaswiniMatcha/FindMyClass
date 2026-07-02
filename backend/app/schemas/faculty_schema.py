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


class FacultyCreate(BaseModel):
    name: str
    email: str
    designation: str
    department_id: int
    room_id: int


class FacultyResponse(BaseModel):
    id: int
    name: str
    email: str
    designation: str

    department: DepartmentMini

    room: RoomMini

    class Config:
        from_attributes = True