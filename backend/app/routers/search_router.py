from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any

from app.dependencies import get_db
from app.services.search_service import search_service

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/")
def search(
    q: str,
    db: Session = Depends(get_db)
) -> dict[str, list[dict[str, Any]]]:

    return {
        "results": search_service(db, q)
    }