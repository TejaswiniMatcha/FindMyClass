from pydantic import BaseModel, ConfigDict


class BuildingBase(BaseModel):
    # Basic Information
    name: str
    code: str
    slug: str

    # Display Information
    short_name: str
    icon: str

    # Description
    description: str

    # Image filename stored in /static
    image: str

    # Building Information
    floors: int

    # Building Highlights
    highlights: list[str]


class BuildingCreate(BuildingBase):
    pass


class BuildingUpdate(BuildingBase):
    pass


class BuildingResponse(BuildingBase):
    id: int

    # Calculated dynamically from the relationship
    room_count: int

    model_config = ConfigDict(
        from_attributes=True
    )