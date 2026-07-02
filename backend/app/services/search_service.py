from typing import Any

from sqlalchemy import or_
from sqlalchemy.orm import Session, joinedload

from app.models.building import Building
from app.models.room import Room
from app.models.department import Department
from app.models.faculty import Faculty
from app.models.section import Section


def calculate_score(text: str, query: str) -> int:
    text = (text or "").lower().strip()
    query = query.lower().strip()

    if text == query:
        return 100

    if text.startswith(query):
        return 90

    if query in text:
        return 70

    return 0


def search_service(
    db: Session,
    query: str
) -> list[dict[str, Any]]:

    query = query.strip()

    if not query:
        return []

    results: list[dict[str, Any]] = []

    # =====================================================
    # BUILDINGS
    # =====================================================

    buildings = (
        db.query(Building)
        .filter(
            or_(
                Building.name.ilike(f"%{query}%"),
                Building.code.ilike(f"%{query}%"),
                Building.slug.ilike(f"%{query}%")
            )
        )
        .all()
    )

    for building in buildings:
        results.append({
            "id": building.id,
            "title": building.name,
            "subtitle": f"{building.code} • {building.floors} Floors",
            "type": "Building",
            "route": f"/block/{building.slug}",
            "score": calculate_score(str(building.name), query)
        })

    # =====================================================
    # ROOMS
    # =====================================================

    rooms = (
        db.query(Room)
        .options(joinedload(Room.building))
        .filter(
            Room.room_no.ilike(f"%{query}%")
        )
        .all()
    )

    for room in rooms:

        building_name = (
            room.building.name
            if room.building
            else "Unknown Building"
        )

        results.append({
            "id": room.id,
            "title": f"Room {room.room_no}",
            "subtitle": f"{building_name} • Floor {room.floor}",
            "type": "Room",
            "route": f"/room/{room.id}",
            "score": calculate_score(str(room.room_no), query)
        })

    # =====================================================
    # DEPARTMENTS
    # =====================================================

    departments = (
        db.query(Department)
        .filter(
            or_(
                Department.name.ilike(f"%{query}%"),
                Department.code.ilike(f"%{query}%")
            )
        )
        .all()
    )

    for department in departments:
        results.append({
            "id": department.id,
            "title": department.name,
            "subtitle": department.code,
            "type": "Department",
            "route": f"/department/{department.id}",
            "score": calculate_score(str(department.name), query)
        })

    # =====================================================
    # FACULTY
    # =====================================================

    faculties = (
        db.query(Faculty)
        .options(joinedload(Faculty.department))
        .filter(
            or_(
                Faculty.name.ilike(f"%{query}%"),
                Faculty.email.ilike(f"%{query}%")
            )
        )
        .all()
    )

    for faculty in faculties:

        department_code = (
            faculty.department.code
            if faculty.department
            else ""
        )

        results.append({
            "id": faculty.id,
            "title": faculty.name,
            "subtitle": f"{faculty.designation} • {department_code}",
            "type": "Faculty",
            "route": f"/faculty/{faculty.id}",
            "score": calculate_score(str(faculty.name), query)
        })

    # =====================================================
    # SECTIONS
    # =====================================================

    sections = (
        db.query(Section)
        .options(
            joinedload(Section.department),
            joinedload(Section.room)
        )
        .filter(
            or_(
                Section.name.ilike(f"%{query}%"),
                Section.year.ilike(f"%{query}%")
            )
        )
        .all()
    )

    for section in sections:

        department_code = (
            section.department.code
            if section.department
            else ""
        )

        room_number = (
            section.room.room_no
            if section.room
            else ""
        )

        results.append({
            "id": section.id,
            "title": f"Section {section.name}",
            "subtitle": (
                f"{department_code} • "
                f"{section.year} Year • "
                f"Room {room_number}"
            ),
            "type": "Section",
            "route": f"/section/{section.id}",
            "score": calculate_score(str(section.name), query)
        })

    # =====================================================
    # SORT RESULTS
    # =====================================================

    results.sort(
        key=lambda item: (-item["score"], item["title"])
    )

    return results[:20]