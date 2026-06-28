from sqlalchemy.orm import Session, joinedload
from typing import List

from app.models.section import Section
from app.models.room import Room


def autocomplete_search(db: Session, query: str) -> List[str]:
    query = query.strip().lower()
    if not query:
        return []

    suggestions: set[str] = set()

    sections = (
        db.query(Section)
        .options(
            joinedload(Section.department),
            joinedload(Section.room).joinedload(Room.building)
        )
        .all()
    )

    for s in sections:
        # Section name
        if s.name and query in s.name.lower():
            suggestions.add(s.name)

        # Section year (cast to str if numeric)
        if s.year and query in str(s.year).lower():
            suggestions.add(str(s.year))

        # Department
        if s.department:
            if s.department.name and query in s.department.name.lower():
                suggestions.add(s.department.name)
            if s.department.code and query in s.department.code.lower():
                suggestions.add(s.department.code)

        # Room
        if s.room and s.room.room_no and query in s.room.room_no.lower():
            suggestions.add(s.room.room_no)

        # Building
        if s.room and s.room.building and s.room.building.name and query in s.room.building.name.lower():
            suggestions.add(s.room.building.name)

    return list(suggestions)[:10]
