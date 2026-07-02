from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.dependencies import get_db
from app.models.section import Section
from app.schemas.section_schema import SectionCreate, SectionResponse
from app.models.room import Room

router = APIRouter(
    prefix="/sections",
    tags=["Sections"]
)


@router.post("/", response_model=SectionResponse)
def create_section(
    section: SectionCreate,
    db: Session = Depends(get_db)
):

    db_section = Section(**section.model_dump())

    db.add(db_section)
    db.commit()
    db.refresh(db_section)

    return db_section


@router.get("/", response_model=list[SectionResponse])
def get_sections(
    db: Session = Depends(get_db)
):

    return (
        db.query(Section)
        .options(
            joinedload(Section.department),
            joinedload(Section.room).joinedload(Room.building)
        )
        .order_by(
            Section.year,
            Section.name
        )
        .all()
    )


@router.get("/{section_id}", response_model=SectionResponse)
def get_section(
    section_id: int,
    db: Session = Depends(get_db)
):

    section = (
    db.query(Section)
    .options(
        joinedload(Section.department),
        joinedload(Section.room).joinedload(Room.building)
    )
    .filter(
        Section.id == section_id
    )
    .first()
)

    return section


@router.put("/{section_id}", response_model=SectionResponse)
def update_section(
    section_id: int,
    section_data: SectionCreate,
    db: Session = Depends(get_db)
):

    section = db.query(Section).filter(
        Section.id == section_id
    ).first()

    if section is None:
        raise HTTPException(
            status_code=404,
            detail="Section not found"
        )

    for key, value in section_data.model_dump().items():
        setattr(section, key, value)

    db.commit()
    db.refresh(section)

    return section


@router.delete("/{section_id}")
def delete_section(
    section_id: int,
    db: Session = Depends(get_db)
):

    section = db.query(Section).filter(
        Section.id == section_id
    ).first()

    if section is None:
        raise HTTPException(
            status_code=404,
            detail="Section not found"
        )

    db.delete(section)
    db.commit()

    return {"message": "Section deleted successfully"}