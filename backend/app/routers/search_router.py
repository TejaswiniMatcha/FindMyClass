from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.search_schema import SearchResponse
from app.services.search_service import (
    search_service,
    search_suggestions_service,
)

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.get("/", response_model=SearchResponse)
def search(
    q: str = Query(..., min_length=2, description="Search query string"),
    limit: int = Query(20, ge=1, le=50, description="Maximum number of results to return"),
    offset: int = Query(0, ge=0, description="Number of records to skip for pagination"),
    db: Session = Depends(get_db),
) -> SearchResponse:

    results = search_service(db, q, limit=limit, offset=offset)
    return SearchResponse(
        query=q,
        count=len(results),
        limit=limit,
        offset=offset,
        results=results,
    )


@router.get("/suggestions", response_model=SearchResponse)
def suggestions(
    q: str = Query(..., min_length=2, description="Search query string"),
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1, le=20, description="Maximum number of suggestions"),
) -> SearchResponse:

    results = search_suggestions_service(db, q, limit=limit)
    return SearchResponse(
        query=q,
        count=len(results),
        limit=limit,
        offset=0,
        results=results,
    )
