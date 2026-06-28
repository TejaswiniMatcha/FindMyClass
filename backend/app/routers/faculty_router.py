from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.faculty import Faculty
from app.schemas.faculty_schema import FacultyCreate, FacultyResponse

router = APIRouter(
    prefix="/faculties",
    tags=["Faculties"]
)


@router.post("/", response_model=FacultyResponse)
def create_faculty(
    faculty: FacultyCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Faculty).filter(
        Faculty.email == faculty.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Faculty already exists"
        )

    db_faculty = Faculty(**faculty.model_dump())

    db.add(db_faculty)
    db.commit()
    db.refresh(db_faculty)

    return db_faculty


@router.get("/", response_model=list[FacultyResponse])
def get_faculties(db: Session =Depends(get_db)):
    return db.query(Faculty).all()


@router.get("/{faculty_id}", response_model=FacultyResponse)
def get_faculty(
    faculty_id: int,
    db: Session = Depends(get_db)
):

    faculty = db.query(Faculty).filter(
        Faculty.id == faculty_id
    ).first()

    if faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    return faculty


@router.put("/{faculty_id}", response_model=FacultyResponse)
def update_faculty(
    faculty_id: int,
    faculty_data: FacultyCreate,
    db: Session = Depends(get_db)
):

    faculty = db.query(Faculty).filter(
        Faculty.id == faculty_id
    ).first()

    if faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    for key, value in faculty_data.model_dump().items():
        setattr(faculty, key, value)

    db.commit()
    db.refresh(faculty)

    return faculty


@router.delete("/{faculty_id}")
def delete_faculty(
    faculty_id: int,
    db: Session = Depends(get_db)
):

    faculty = db.query(Faculty).filter(
        Faculty.id == faculty_id
    ).first()

    if faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    db.delete(faculty)
    db.commit()

    return {"message": "Faculty deleted successfully"}