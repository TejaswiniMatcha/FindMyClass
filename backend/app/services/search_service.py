from typing import Any, cast
import re

from sqlalchemy import or_
from sqlalchemy.orm import Session, joinedload

from app.models.building import Building
from app.models.department import Department
from app.models.faculty import Faculty
from app.models.room import Room
from app.models.section import Section


TYPE_ICON_MAP = {
    'Building': 'Building',
    'Room': 'Door',
    'Faculty': 'User',
    'Department': 'Layers',
    'Section': 'LayoutList',
}

SYNONYM_QUERIES = {
    'principal office': [
        'principal office',
        'administration',
        'central block',
        'principal',
        'admin office',
    ],
    'hod room': [
        'hod',
        'head of department',
        'hod room',
        'faculty cabin',
        'department head',
    ],
    'cse class': [
        'cse',
        'computer science',
        'computer science and engineering',
        'cse department',
    ],
    'computer science': [
        'cse',
        'computer science',
        'computer science and engineering',
        'cse department',
    ],
}


def normalize_text(text: str) -> str:
    return re.sub(r'\s+', ' ', (text or '').strip().lower())


def query_tokens(query: str) -> list[str]:
    return [token for token in re.split(r'\W+', normalize_text(query)) if token]


def create_highlight(title: str, query: str) -> str:
    if not query:
        return title

    normalized_title = normalize_text(title)
    normalized_query = normalize_text(query)

    if normalized_query in normalized_title:
        return query

    for phrase, aliases in SYNONYM_QUERIES.items():
        if normalized_query == phrase or normalized_query in phrase:
            for alias in aliases:
                if alias in normalized_title:
                    return alias

    title_tokens = set(query_tokens(title))
    query_tokens_set = set(query_tokens(query))
    overlap = title_tokens & query_tokens_set
    if overlap:
        return ' '.join(sorted(overlap))

    return title


def calculate_score(text: str, query: str) -> int:
    text = normalize_text(text)
    query = normalize_text(query)

    if not query or not text:
        return 0

    if text == query:
        return 100

    if text.startswith(query):
        return 90

    if query in text:
        return 80

    text_tokens = set(query_tokens(text))
    query_tokens_set = set(query_tokens(query))
    overlap = text_tokens & query_tokens_set
    if overlap:
        return 70 + min(20, len(overlap) * 5)

    for phrase, aliases in SYNONYM_QUERIES.items():
        if phrase == query or phrase in query or query in phrase:
            for alias in aliases:
                if alias in text:
                    return 65

    return 0


def build_search_result(
    id: int,
    title: str,
    subtitle: str,
    type_name: str,
    route: str,
    query: str,
) -> dict[str, Any]:
    result = {
        'id': id,
        'title': title,
        'subtitle': subtitle,
        'type': type_name,
        'route': route,
        'icon': TYPE_ICON_MAP.get(type_name, 'Search'),
        'highlight': create_highlight(title, query),
    }
    result['score'] = calculate_score(f"{title} {subtitle}", query)
    return result


def gather_search_results(db: Session, query: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    normalized_query = normalize_text(query)

    if len(normalized_query) < 2:
        return results

    query_filter = f"%{query}%"

    buildings = (
        db.query(Building)
        .filter(
            or_(
                Building.name.ilike(query_filter),
                Building.code.ilike(query_filter),
                Building.slug.ilike(query_filter),
            )
        )
        .all()
    )

    for building in buildings:
        results.append(
            build_search_result(
                cast(int, building.id),
                building.name,
                f'{building.code} • {building.floors} Floors',
                'Building',
                f'/block/{building.slug}',
                query,
            )
        )

    rooms = (
        db.query(Room)
        .options(joinedload(Room.building))
        .filter(Room.room_no.ilike(query_filter))
        .all()
    )

    for room in rooms:
        building_name = room.building.name if room.building else 'Unknown Building'
        results.append(
            build_search_result(
                cast(int, room.id),
                f'Room {room.room_no}',
                f'{building_name} • Floor {room.floor}',
                'Room',
                f'/room/{room.id}',
                query,
            )
        )

    departments = (
        db.query(Department)
        .filter(
            or_(
                Department.name.ilike(query_filter),
                Department.code.ilike(query_filter),
            )
        )
        .all()
    )

    for department in departments:
        results.append(
            build_search_result(
                cast(int, department.id),
                str(department.name),
                str(department.code),
                'Department',
                f'/department/{department.id}',
                query,
            )
        )

    faculties = (
        db.query(Faculty)
        .options(joinedload(Faculty.department))
        .filter(
            or_(
                Faculty.name.ilike(query_filter),
                Faculty.email.ilike(query_filter),
            )
        )
        .all()
    )

    for faculty in faculties:
        department_code = faculty.department.code if faculty.department else ''
        results.append(
            build_search_result(
                cast(int, faculty.id),
                faculty.name,
                f'{faculty.designation} • {department_code}',
                'Faculty',
                f'/faculty/{faculty.id}',
                query,
            )
        )

    sections = (
        db.query(Section)
        .options(joinedload(Section.department), joinedload(Section.room))
        .filter(
            or_(
                Section.name.ilike(query_filter),
                Section.year.ilike(query_filter),
            )
        )
        .all()
    )

    for section in sections:
        department_code = section.department.code if section.department else ''
        room_number = section.room.room_no if section.room else ''
        results.append(
            build_search_result(
                cast(int, section.id),
                f'Section {section.name}',
                f'{department_code} • {section.year} Year • Room {room_number}',
                'Section',
                f'/section/{section.id}',
                query,
            )
        )

    return results


def search_service(db: Session, query: str, limit: int = 20, offset: int = 0) -> list[dict[str, Any]]:
    results = gather_search_results(db, query)
    results.sort(key=lambda item: (-item['score'], item['title']))
    return results[offset:offset + limit]


def search_suggestions_service(db: Session, query: str, limit: int = 10) -> list[dict[str, Any]]:
    normalized_query = normalize_text(query)
    if len(normalized_query) < 2:
        return []

    results = gather_search_results(db, query)
    results.sort(key=lambda item: (-item['score'], item['title']))

    seen: set[tuple[str, int]] = set()
    suggestions: list[dict[str, Any]] = []
    for item in results:
        key = (item['type'], item['id'])
        if key not in seen:
            seen.add(key)
            suggestions.append(item)
        if len(suggestions) >= limit:
            break

    if suggestions:
        return suggestions

    for phrase, aliases in SYNONYM_QUERIES.items():
        if phrase in normalized_query or normalized_query in phrase:
            for alias in aliases:
                fallback_results = gather_search_results(db, alias)
                for item in fallback_results:
                    key = (item['type'], item['id'])
                    if key not in seen:
                        seen.add(key)
                        suggestions.append(item)
                    if len(suggestions) >= limit:
                        break
                if len(suggestions) >= limit:
                    break
            break

    suggestions.sort(key=lambda item: (-item['score'], item['title']))
    return suggestions[:limit]
