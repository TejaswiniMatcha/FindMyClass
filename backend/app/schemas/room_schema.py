from pydantic import BaseModel


class BuildingMini(BaseModel):
    id: int
    name: str
    slug: str

    class Config:
        from_attributes = True


class RoomBase(BaseModel):
    room_no: str
    floor: int
    building_id: int


class RoomCreate(RoomBase):
    pass


class RoomResponse(BaseModel):
    id: int
    room_no: str
    floor: int
    building: BuildingMini

    class Config:
        from_attributes = True