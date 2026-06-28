from pydantic import BaseModel


class SearchResult(BaseModel):
    id: int
    title: str
    subtitle: str
    type: str
    route: str


class SearchResponse(BaseModel):
    query: str
    count: int
    results: list[SearchResult]