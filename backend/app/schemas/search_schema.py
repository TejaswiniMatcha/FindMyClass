from typing import Optional

from pydantic import BaseModel


class SearchResult(BaseModel):
    id: int
    title: str
    subtitle: str
    type: str
    route: str
    icon: str
    highlight: Optional[str] = None
    score: int


class SearchResponse(BaseModel):
    query: str
    count: int
    limit: int
    offset: int
    results: list[SearchResult]
