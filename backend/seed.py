from typing import TypedDict, List, Optional

from sqlalchemy.orm import Session

from app.database import Base, SessionLocal, engine

from app.models.building import Building
from app.models.department import Department
from app.models.room import Room
from app.models.section import Section
from app.models.faculty import Faculty


# ==========================================================
# Typed Structures (FIXS PYLANCE ERRORS)
# ==========================================================

# ==========================================================
# Typed Structures
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


class SectionData(TypedDict):
    name: str
    year: str
    department: str
    room_no: str


class FacultyData(TypedDict):
    name: str
    email: str
    designation: str
    department: str
    room_no: str



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
SECTIONS: List[SectionData] = []
FACULTIES: List[FacultyData] = []

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



SECTION_PATTERN = {
    "CSE": ["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P"],
    "CSM": ["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P"],
    "AIM": ["A", "B","C","D"],
    "AID": ["A", "B","C"],
    "IT": ["A","B", "C", "D"],
    "CIC": ["A", "B", "C"],
    "CSO": ["A","B", "C"],
    "ECE": ["A", "B", "C"],
    "EEE": ["A", "B", "C"],
    "MECH": ["A", "B", "C"],
    "CIVIL": ["A", "B", "C"],
    "MBA": ["A", "B", "C"],
}






FACULTY_COUNT = {
    "CSE": 18,
    "ECE": 12,
    "EEE": 8,
    "MECH": 7,
    "CIVIL": 6,
    "IT": 12,
    "AIM": 7,
    "AID": 6,
    "CSM": 8,
    "CIC":9,
    "CSO": 5,
    "MBA": 6,
}




add_standard_block_rooms("A Block")
add_standard_block_rooms("B Block")
add_standard_block_rooms("C Block")
add_standard_block_rooms("D Block")
add_standard_block_rooms("Central Block")
add_siemens_freshman_rooms("Siemens Block")
add_siemens_freshman_rooms("Freshman Block")

# ==========================================================
# Generate Sections
# ==========================================================

def generate_sections() -> None:

    room_index = 0

    years = [
        "1st",
        "2nd",
        "3rd",
        "4th"
    ]

    for year in years:

        for department, section_letters in SECTION_PATTERN.items():

            for letter in section_letters:

                if room_index >= len(ROOMS):
                    room_index = 0

                room = ROOMS[room_index]

                SECTIONS.append(
                    {
                        "name": f"{department}-{letter}",
                        "year": year,
                        "department": department,
                        "room_no": room["room_no"],
                    }
                )

                room_index += 1


# ==========================================================
# Faculty Name Pool
# ==========================================================

FIRST_NAMES = [
    "Anil",
    "Priya",
    "Suresh",
    "Lakshmi",
    "Ravi",
    "Swathi",
    "Harish",
    "Kiran",
    "Aruna",
    "Bhavani",
    "Madhavi",
    "Srinivas",
    "Naveen",
    "Deepika",
    "Rajesh",
    "Keerthi",
    "Manoj",
    "Sunitha",
    "Venkatesh",
    "Ramesh",
]

LAST_NAMES = [
    "Kumar",
    "Reddy",
    "Sharma",
    "Rao",
    "Naidu",
    "Prasad",
    "Devi",
    "Varma",
    "Murthy",
    "Patel",
]


def build_faculty_name(index: int) -> str:

    first = FIRST_NAMES[index % len(FIRST_NAMES)]

    last = LAST_NAMES[index % len(LAST_NAMES)]

    return f"Dr. {first} {last}"



# ==========================================================
# Generate Faculties
# ==========================================================

def generate_faculties() -> None:

    room_index = 0
    name_index = 0

    designations = [
        "Assistant Professor",
        "Associate Professor",
        "Professor",
    ]

    for department, count in FACULTY_COUNT.items():

        for number in range(count):

            if room_index >= len(ROOMS):
                room_index = 0

            room = ROOMS[room_index]

            FACULTIES.append(
                {
                    "name": build_faculty_name(name_index),
                    "email": f"{department.lower()}{number+1}@vvit.edu.in",
                    "designation": designations[number % 3],
                    "department": department,
                    "room_no": room["room_no"],
                }
            )

            room_index += 1
            name_index += 1

generate_sections()
generate_faculties()



  
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



def get_or_create_section(
    db: Session,
    data: SectionData
) -> None:

    department = get_department(
        db,
        data["department"]
    )

    room = get_room_by_number(
        db,
        data["room_no"]
    )

    if department is None or room is None:
        return

    existing = (
        db.query(Section)
        .filter(
            Section.name == data["name"],
            Section.year == data["year"],
            Section.department_id == department.id
        )
        .first()
    )

    if existing:
        return

    db.add(
        Section(
            name=data["name"],
            year=data["year"],
            department_id=department.id,
            room_id=room.id
        )
    )


def get_or_create_faculty(
    db: Session,
    data: FacultyData
) -> None:

    department = get_department(
        db,
        data["department"]
    )

    room = get_room_by_number(
        db,
        data["room_no"]
    )

    if department is None or room is None:
        return

    existing = (
        db.query(Faculty)
        .filter(
            Faculty.email == data["email"]
        )
        .first()
    )

    if existing:
        return

    db.add(
        Faculty(
            name=data["name"],
            email=data["email"],
            designation=data["designation"],
            department_id=department.id,
            room_id=room.id
        )
    )



def get_building(db: Session, name: str) -> Optional[Building]:
    return db.query(Building).filter(
        Building.name == name
    ).first()


def get_department(
    db: Session,
    code: str
) -> Optional[Department]:

    return (
        db.query(Department)
        .filter(Department.code == code)
        .first()
    )



def get_room(
    db: Session,
    room_no: str,
    building_id: int
) -> Optional[Room]:
    return db.query(Room).filter(
        Room.room_no == room_no,
        Room.building_id == building_id
    ).first()


def get_room_by_number(
    db: Session,
    room_no: str
) -> Optional[Room]:

    return (
        db.query(Room)
        .filter(Room.room_no == room_no)
        .first()
    )


# ==========================================================
# Seed Functions
# ==========================================================

def seed_buildings(db: Session) -> None:
    for b in BUILDINGS:
        get_or_create_building(db, b)


def seed_departments(db: Session) -> None:
    for d in DEPARTMENTS:
        get_or_create_department(db, d)



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



def seed_sections(
    db: Session
) -> None:

    print("Seeding Sections...")

    for section in SECTIONS:

        get_or_create_section(
            db,
            section
        )

    db.commit()

    print(
        f"✓ {len(SECTIONS)} Sections Added"
    )



def seed_faculties(
    db: Session
) -> None:

    print("Seeding Faculties...")

    for faculty in FACULTIES:

        get_or_create_faculty(
            db,
            faculty
        )

    db.commit()

    print(
        f"✓ {len(FACULTIES)} Faculties Added"
    )

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
        seed_sections(db)
        seed_faculties(db)

        print("\n✔ Database seeded successfully")

    except Exception as e:
        db.rollback()
        print(f"❌ Error: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    insert_custom_data()