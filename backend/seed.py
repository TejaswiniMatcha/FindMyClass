from typing import TypedDict, List, Optional
from sqlalchemy.orm import Session

from app.database import SessionLocal, Base, engine
from app.models.building import Building
from app.models.department import Department
from app.models.room import Room


# ==========================================================
# Typed Structures (FIXS PYLANCE ERRORS)
# ==========================================================

class BuildingData(TypedDict):
    name: str
    code: str
    slug: str
    short_name: str
    description: str
    image: str
    floors: int


class DepartmentData(TypedDict):
    name: str
    code: str


class RoomData(TypedDict):
    room_no: int
    floor: int
    building: str


# ==========================================================
# Seed Data
# ==========================================================

BUILDINGS: List[BuildingData] = [
    {
        "name": "A Block",
        "code": "A",
        "slug": "a-block",
        "short_name": "A",
        "description": "Main academic block",
        "image": "blockA.jpeg",
        "floors": 4,
    },
    {
        "name": "B Block",
        "code": "B",
        "slug": "b-block",
        "short_name": "B",
        "description": "Engineering departments",
        "image": "blockB.jpeg",
        "floors": 4,
    },
]


DEPARTMENTS: List[DepartmentData] = [
    {"name": "Computer Science and Engineering", "code": "CSE"},
    {"name": "Information Technology", "code": "IT"},
]


ROOMS: List[RoomData] = []


def add_standard_block_rooms(building_name: str) -> None:
    for floor in range(4):
        start = (floor + 1) * 100
        for room in range(1, 7):
            ROOMS.append({
                "room_no": start + room,
                "floor": floor,
                "building": building_name
            })


add_standard_block_rooms("A Block")
add_standard_block_rooms("B Block")


# ==========================================================
# DB Helpers (TYPE SAFE)
# ==========================================================

def get_or_create_building(db: Session, data: BuildingData) -> Building:
    building = db.query(Building).filter(
        Building.code == data["code"]
    ).first()

    if building:
        return building

    building = Building(**data)
    db.add(building)
    db.commit()
    db.refresh(building)
    return building


def get_or_create_department(db: Session, data: DepartmentData) -> Department:
    department = db.query(Department).filter(
        Department.code == data["code"]
    ).first()

    if department:
        return department

    department = Department(**data)
    db.add(department)
    db.commit()
    db.refresh(department)

    print(f"✓ Department Added: {department.code}")
    return department


def get_building(db: Session, name: str) -> Optional[Building]:
    return db.query(Building).filter(
        Building.name == name
    ).first()


def get_room(db: Session, room_no: int, building_id: int) -> Optional[Room]:
    return db.query(Room).filter(
        Room.room_no == room_no,
        Room.building_id == building_id
    ).first()


# ==========================================================
# Seed Functions
# ==========================================================

def seed_buildings(db: Session) -> None:
    for b in BUILDINGS:
        get_or_create_building(db, b)


def seed_departments(db: Session) -> None:
    for d in DEPARTMENTS:
        get_or_create_department(db, d)


from sqlalchemy.orm import Session
from app.models.room import Room


def seed_rooms(db: Session) -> None:
    print("Seeding rooms...")

    for r in ROOMS:

        building = get_building(db, r["building"])
        if not building:
            continue

        # SAFE access (removes Column[int] issue completely)
        building_id = getattr(building, "id")

        existing = get_room(db, r["room_no"], building_id)
        if existing:
            continue

        db.add(Room(
            room_no=r["room_no"],
            floor=r["floor"],
            building_id=building_id
        ))

    db.commit()
    print("Seeding completed.")

# ==========================================================
# MASTER SEEDER
# ==========================================================

def insert_custom_data() -> None:
    db: Session = SessionLocal()

    try:
        Base.metadata.create_all(bind=engine)

        seed_buildings(db)
        seed_departments(db)
        seed_rooms(db)

        print("\n✔ Database seeded successfully")

    except Exception as e:
        db.rollback()
        print(f"❌ Error: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    insert_custom_data()