from pydantic import BaseModel


class BuildingBase(BaseModel):
    name: str
    code: str
    slug: str
    short_name: str
    icon: str
    description: str
    image: str
    floors: int
    highlights: list[str]


class BuildingCreate(BuildingBase):
    pass


class BuildingUpdate(BuildingBase):
    pass


class BuildingResponse(BuildingBase):
    id: int
    room_count: int

    class Config:
        from_attributes = True