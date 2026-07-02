from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.dependencies import get_db
from app.models.building import Building
from app.schemas.building_schema import (
    BuildingCreate,
    BuildingUpdate,
    BuildingResponse,
)

router = APIRouter(
    prefix="/buildings",
    tags=["Buildings"]
)


# ---------------------------------------------------------
# Create Building
# ---------------------------------------------------------
@router.post("/", response_model=BuildingResponse)
def create_building(
    building: BuildingCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Building).filter(
        Building.code == building.code
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Building already exists"
        )

    db_building = Building(**building.model_dump())

    db.add(db_building)
    db.commit()
    db.refresh(db_building)

    return db_building


# ---------------------------------------------------------
# Get All Buildings
# ---------------------------------------------------------
@router.get("/", response_model=list[BuildingResponse])
def get_buildings(
    db: Session = Depends(get_db)
):
    return (
    db.query(Building)
    .options(
        joinedload(Building.rooms)
    )
    .order_by(Building.name)
    .all()
)


# ---------------------------------------------------------
# Get Building By Slug
# ---------------------------------------------------------
@router.get("/{slug}", response_model=BuildingResponse)
def get_building(
    slug: str,
    db: Session = Depends(get_db)
):

    building = (
    db.query(Building)
    .options(
        joinedload(Building.rooms)
    )
    .filter(Building.slug == slug)
    .first()
)

    if building is None:
        raise HTTPException(
            status_code=404,
            detail="Building not found"
        )

    return building


# ---------------------------------------------------------
# Update Building
# ---------------------------------------------------------
@router.put("/{building_id}", response_model=BuildingResponse)
def update_building(
    building_id: int,
    building_data: BuildingUpdate,
    db: Session = Depends(get_db)
):

    building = (
        db.query(Building)
        .filter(Building.id == building_id)
        .first()
    )

    if building is None:
        raise HTTPException(
            status_code=404,
            detail="Building not found"
        )

    for key, value in building_data.model_dump().items():
        setattr(building, key, value)

    db.commit()
    db.refresh(building)

    return building


# ---------------------------------------------------------
# Delete Building
# ---------------------------------------------------------
@router.delete("/{building_id}")
def delete_building(
    building_id: int,
    db: Session = Depends(get_db)
):

    building = (
        db.query(Building)
        .filter(Building.id == building_id)
        .first()
    )

    if building is None:
        raise HTTPException(
            status_code=404,
            detail="Building not found"
        )

    db.delete(building)
    db.commit()

    return {
        "message": "Building deleted successfully"
    }