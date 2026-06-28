from pydantic import BaseModel


class BuildingBase(BaseModel):
    name: str
    code: str
    slug: str
    short_name: str
    description: str
    image: str
    floors: int


class BuildingCreate(BuildingBase):
    pass


class BuildingResponse(BuildingBase):
    id: int

    class Config:
        from_attributes = True