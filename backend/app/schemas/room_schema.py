from pydantic import BaseModel


class RoomBase(BaseModel):
    room_no: str
    floor: int
    building_id: int


class RoomCreate(RoomBase):
    pass


class RoomResponse(RoomBase):
    id: int

    class Config:
        from_attributes = True