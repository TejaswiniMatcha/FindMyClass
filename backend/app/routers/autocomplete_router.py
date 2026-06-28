from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.autocomplete_service import autocomplete_search

router = APIRouter(prefix="/autocomplete", tags=["Autocomplete"])


@router.get("/")
def autocomplete(query: str, db: Session = Depends(get_db)):
    return {
        "query": query,
        "suggestions": autocomplete_search(db, query)
    }