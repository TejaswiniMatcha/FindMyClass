from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_

from app.models.building import Building
from app.models.room import Room
from app.models.department import Department
from app.models.faculty import Faculty
from app.models.section import Section


def calculate_score(text: str, query: str) -> int:
    text = (text or "").lower()
    query = query.lower()

    if text == query:
        return 100
    if text.startswith(query):
        return 90
    if query in text:
        return 70
    return 0


def search_service(db: Session, query: str):
    query = query.strip()

    if not query:
        return []

    results = []

    # BUILDINGS
    buildings = db.query(Building).filter(
        or_(
            Building.name.ilike(f"%{query}%"),
            Building.code.ilike(f"%{query}%")
        )
    ).all()

    for b in buildings:
        results.append({
            "id": b.id,
            "title": b.name,
            "subtitle": f"Code: {b.code}",
            "type": "Building",
            "route": f"/block/{b.id}",
            "score": calculate_score(b.name, query)
        })

    # ROOMS
    rooms = db.query(Room).options(joinedload(Room.building))\
        .filter(Room.room_no.ilike(f"%{query}%")).all()

    for r in rooms:
        building_name = r.building.name if r.building else ""

        results.append({
            "id": r.id,
            "title": f"Room {r.room_no}",
            "subtitle": f"{building_name} • Floor {r.floor}",
            "type": "Room",
            "route": f"/room/{r.id}",
            "score": calculate_score(r.room_no, query)
        })

    # DEPARTMENTS
    departments = db.query(Department).filter(
        or_(
            Department.name.ilike(f"%{query}%"),
            Department.code.ilike(f"%{query}%")
        )
    ).all()

    for d in departments:
        results.append({
            "id": d.id,
            "title": d.name,
            "subtitle": d.code,
            "type": "Department",
            "route": f"/department/{d.id}",
            "score": calculate_score(d.name, query)
        })

    # FACULTY
    faculties = db.query(Faculty).options(joinedload(Faculty.department))\
        .filter(Faculty.name.ilike(f"%{query}%")).all()

    for f in faculties:
        dept_code = f.department.code if f.department else ""

        results.append({
            "id": f.id,
            "title": f.name,
            "subtitle": f"{f.designation} • {dept_code}",
            "type": "Faculty",
            "route": f"/faculty/{f.id}",
            "score": calculate_score(f.name, query)
        })

    # SECTIONS
    sections = db.query(Section).options(
        joinedload(Section.department),
        joinedload(Section.room)
    ).filter(Section.name.ilike(f"%{query}%")).all()

    for s in sections:
        dept_code = s.department.code if s.department else ""
        room_no = s.room.room_no if s.room else ""

        results.append({
            "id": s.id,
            "title": f"Section {s.name}",
            "subtitle": f"{dept_code} • {s.year} Year • Room {room_no}",
            "type": "Section",
            "route": f"/section/{s.id}",
            "score": calculate_score(s.name, query)
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:20]