from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_
from app.models import Building, Room, Department, Faculty, Section

def calculate_score(name: str, query: str) -> int:
    name = (name or "").lower()
    query = query.lower()

    if name == query:
        return 100
    if name.startswith(query):
        return 90
    if query in name:
        return 70
    return 0