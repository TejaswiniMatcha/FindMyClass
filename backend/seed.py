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
    icon: str
    description: str
    image: str
    floors: int
    highlights: list[str]


class DepartmentData(TypedDict):
    name: str
    code: str


class RoomData(TypedDict):
    room_no: str
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
        "icon": "A",
        "description": "Main academic block with lecture halls and faculty offices.",
        "image": "blockA.jpeg",
        "floors": 4,
        "highlights": [
            "Smart Classrooms",
            "Seminar Rooms",
            "Faculty Cabins"
        ]
    },

    {
        "name": "B Block",
        "code": "B",
        "slug": "b-block",
        "short_name": "B",
        "icon": "B",
        "description": "Engineering departments and laboratory facilities.",
        "image": "blockB.jpeg",
        "floors": 4,
        "highlights": [
            "CSE Department",
            "Project Labs",
            "Discussion Rooms"
        ]
    },

    {
        "name": "C Block",
        "code": "C",
        "slug": "c-block",
        "short_name": "C",
        "icon": "C",
        "description": "Administrative offices and student support services.",
        "image": "blockC.jpeg",
        "floors": 4,
        "highlights": [
            "Admissions",
            "Examination Cell",
            "Student Services"
        ]
    },

    {
        "name": "D Block",
        "code": "D",
        "slug": "d-block",
        "short_name": "D",
        "icon": "D",
        "description": "Research and innovation block with workshops.",
        "image": "blockD.jpeg",
        "floors": 4,
        "highlights": [
            "Innovation Lab",
            "Workshop",
            "Design Studio"
        ]
    },

    {
        "name": "Siemens Block",
        "code": "SB",
        "slug": "siemens-block",
        "short_name": "SB",
        "icon": "SB",
        "description": "Industry-oriented laboratories and automation training.",
        "image": "Siemensblock.jpeg",
        "floors": 5,
        "highlights": [
            "Automation Lab",
            "PLC Training",
            "Simulation Center"
        ]
    },

    {
        "name": "Freshman Block",
        "code": "FB",
        "slug": "freshman-block",
        "short_name": "FB",
        "icon": "FB",
        "description": "Dedicated classrooms and mentoring spaces for first-year students.",
        "image": "Freshmanblock.jpeg",
        "floors": 5,
        "highlights": [
            "Foundation Courses",
            "Mentoring Rooms",
            "Study Area"
        ]
    },

    {
        "name": "Central Block",
        "code": "CB",
        "slug": "central-block",
        "short_name": "CB",
        "icon": "CB",
        "description": "Campus administration and common facilities.",
        "image": "Centralblock.jpeg",
        "floors": 4,
        "highlights": [
            "Principal Office",
            "Accounts",
            "Conference Hall"
        ]
    },

    {
        "name": "Open Air Theatre",
        "code": "OAT",
        "slug": "oat",
        "short_name": "OAT",
        "icon": "OAT",
        "description": "Venue for cultural events and large student gatherings.",
        "image": "OAT.jpeg",
        "floors": 0,
        "highlights": [
            "Cultural Events",
            "Freshers Day",
            "Annual Fest"
        ]
    }

]


DEPARTMENTS: List[DepartmentData] = [
    {"name": "Computer Science and Engineering", "code": "CSE"},
                {"name": "Electronics and Communication Engineering", "code": "ECE"},
                {"name": "Mechanical Engineering", "code": "MECH"},
                {"name": "Civil Engineering", "code": "CIVIL"},
                {"name": "Cybersecurity, IOT and Blockchain technology", "code": "CIC"},
                {"name": "Computer Science and IOT", "code": "CSO"},
                {"name": "Electrical and Electronics Engineering", "code": "EEE"},
                {"name": "Information Technology", "code": "IT"},
                {"name": "Artificial Intelligence and Machine Learning", "code": "AIM"},
                {"name": "Artificial Intelligence and Data Science", "code": "AID"},
                {"name": "Computer Systems and Machine Learning", "code": "CSM"},
                {"name": "Master of Business Administration", "code": "MBA"},
]


ROOMS: List[RoomData] = []


def add_standard_block_rooms(building_name: str) -> None:
    for floor in range(4):
        start = (floor + 1) * 100
        for room in range(1, 7):
            ROOMS.append({
                "room_no": str(start + room),
                "floor": floor,
                "building": building_name
            })
def add_siemens_freshman_rooms(building_name: str) -> None:
    for floor in range(5):
        start = (floor + 1) * 100
        for room in range(1, 20):
            ROOMS.append({
                "room_no": str(start + room),
                "floor": floor,
                "building": building_name
            })



add_standard_block_rooms("A Block")
add_standard_block_rooms("B Block")
add_standard_block_rooms("C Block")
add_standard_block_rooms("D Block")
add_standard_block_rooms("Central Block")
add_siemens_freshman_rooms("Siemens Block")
add_siemens_freshman_rooms("Freshman Block")

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


def get_room(
    db: Session,
    room_no: str,
    building_id: int
) -> Optional[Room]:
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