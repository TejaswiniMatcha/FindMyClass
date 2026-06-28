from typing import Any, Dict, List
from app.database import SessionLocal, Base, engine
from app.models.building import Building
from app.models.department import Department
from app.models.room import Room
from app.models.faculty import Faculty
from app.models.section import Section
from sqlalchemy.orm import Session


def get_or_create_building(db: Session, name: str, code: str, floors: int) -> Building:
    building = db.query(Building).filter(Building.name == name).first()
    if building is None:
        building = Building(name=name, code=code, floors=floors)
        db.add(building)
        db.commit()
        db.refresh(building)
    return building


def get_or_create_department(db: Session, name: str, code: str) -> Department:
    department = db.query(Department).filter(Department.name == name).first()
    if department is None:
        department = Department(name=name, code=code)
        db.add(department)
        db.commit()
        db.refresh(department)
    return department


def get_or_create_room(db: Session, room_no: int, floor: int, building_name: str) -> Room:
    building = db.query(Building).filter(Building.name == building_name).first()
    if building is None:
        raise ValueError(f"Building '{building_name}' does not exist. Create it first.")

    room = db.query(Room).filter(Room.room_no == room_no, Room.building_id == building.id).first()
    if room is None:
        room = Room(room_no=room_no, floor=floor, building_id=building.id)
        db.add(room)
        db.commit()
        db.refresh(room)
    return room


def insert_custom_data() -> None:
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # Fill this dictionary with your own campus data.
        # Leave it empty if you do not want to insert anything yet.
        custom_data: Dict[str, List[Any]] = {
            "buildings": [
                {"name": "A Block", "code": "A", "floors": 4},
                {"name": "B Block", "code": "B", "floors": 4},
                {"name": "C Block", "code": "C", "floors": 4},
                {"name": "D Block", "code": "D", "floors": 4},
                {"name": "Siemens Block", "code": "S", "floors": 5},
                {"name": "Freshman Block", "code": "F", "floors": 5},
                {"name": "Central Block", "code": "CB", "floors": 4},
                {"name": "OAT", "code": "O", "floors": 0}
            ],
            "departments": [
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
                {"name": "Computer Systems and Machine Learning", "code": "CSM"}
            ],
            "rooms": [
                # A Block rooms (101-406)
                {"room_no": 101, "floor": 0, "building": "A Block"},
                {"room_no": 102, "floor": 0, "building": "A Block"},
                {"room_no": 103, "floor": 0, "building": "A Block"},
                {"room_no": 104, "floor": 0, "building": "A Block"},
                {"room_no": 105, "floor": 0, "building": "A Block"},
                {"room_no": 106, "floor": 0, "building": "A Block"},
                {"room_no": 201, "floor": 1, "building": "A Block"},
                {"room_no": 202, "floor": 1, "building": "A Block"},
                {"room_no": 203, "floor": 1, "building": "A Block"},
                {"room_no": 204, "floor": 1, "building": "A Block"},
                {"room_no": 205, "floor": 1, "building": "A Block"},
                {"room_no": 206, "floor": 1, "building": "A Block"},
                {"room_no": 301, "floor": 2, "building": "A Block"},
                {"room_no": 302, "floor": 2, "building": "A Block"},
                {"room_no": 303, "floor": 2, "building": "A Block"},
                {"room_no": 304, "floor": 2, "building": "A Block"},
                {"room_no": 305, "floor": 2, "building": "A Block"},
                {"room_no": 306, "floor": 2, "building": "A Block"},
                {"room_no": 401, "floor": 3, "building": "A Block"},
                {"room_no": 402, "floor": 3, "building": "A Block"},
                {"room_no": 403, "floor": 3, "building": "A Block"},
                {"room_no": 404, "floor": 3, "building": "A Block"},
                {"room_no": 405, "floor": 3, "building": "A Block"},
                {"room_no": 406, "floor": 3, "building": "A Block"},
                # B Block rooms (101-406)
                {"room_no": 101, "floor": 0, "building": "B Block"},
                {"room_no": 102, "floor": 0, "building": "B Block"},
                {"room_no": 103, "floor": 0, "building": "B Block"},
                {"room_no": 104, "floor": 0, "building": "B Block"},
                {"room_no": 105, "floor": 0, "building": "B Block"},
                {"room_no": 106, "floor": 0, "building": "B Block"},
                {"room_no": 201, "floor": 1, "building": "B Block"},
                {"room_no": 202, "floor": 1, "building": "B Block"},
                {"room_no": 203, "floor": 1, "building": "B Block"},
                {"room_no": 204, "floor": 1, "building": "B Block"},
                {"room_no": 205, "floor": 1, "building": "B Block"},
                {"room_no": 206, "floor": 1, "building": "B Block"},
                {"room_no": 301, "floor": 2, "building": "B Block"},
                {"room_no": 302, "floor": 2, "building": "B Block"},
                {"room_no": 303, "floor": 2, "building": "B Block"},
                {"room_no": 304, "floor": 2, "building": "B Block"},
                {"room_no": 305, "floor": 2, "building": "B Block"},
                {"room_no": 306, "floor": 2, "building": "B Block"},
                {"room_no": 401, "floor": 3, "building": "B Block"},
                {"room_no": 402, "floor": 3, "building": "B Block"},
                {"room_no": 403, "floor": 3, "building": "B Block"},
                {"room_no": 404, "floor": 3, "building": "B Block"},
                {"room_no": 405, "floor": 3, "building": "B Block"},
                {"room_no": 406, "floor": 3, "building": "B Block"},
                # C Block rooms (101-406)
                {"room_no": 101, "floor": 0, "building": "C Block"},
                {"room_no": 102, "floor": 0, "building": "C Block"},
                {"room_no": 103, "floor": 0, "building": "C Block"},
                {"room_no": 104, "floor": 0, "building": "C Block"},
                {"room_no": 105, "floor": 0, "building": "C Block"},
                {"room_no": 106, "floor": 0, "building": "C Block"},
                {"room_no": 201, "floor": 1, "building": "C Block"},
                {"room_no": 202, "floor": 1, "building": "C Block"},
                {"room_no": 203, "floor": 1, "building": "C Block"},
                {"room_no": 204, "floor": 1, "building": "C Block"},
                {"room_no": 205, "floor": 1, "building": "C Block"},
                {"room_no": 206, "floor": 1, "building": "C Block"},
                {"room_no": 301, "floor": 2, "building": "C Block"},
                {"room_no": 302, "floor": 2, "building": "C Block"},
                {"room_no": 303, "floor": 2, "building": "C Block"},
                {"room_no": 304, "floor": 2, "building": "C Block"},
                {"room_no": 305, "floor": 2, "building": "C Block"},
                {"room_no": 306, "floor": 2, "building": "C Block"},
                {"room_no": 401, "floor": 3, "building": "C Block"},
                {"room_no": 402, "floor": 3, "building": "C Block"},
                {"room_no": 403, "floor": 3, "building": "C Block"},
                {"room_no": 404, "floor": 3, "building": "C Block"},
                {"room_no": 405, "floor": 3, "building": "C Block"},
                {"room_no": 406, "floor": 3, "building": "C Block"},
                # D Block rooms (101-406)
                {"room_no": 101, "floor": 0, "building": "D Block"},
                {"room_no": 102, "floor": 0, "building": "D Block"},
                {"room_no": 103, "floor": 0, "building": "D Block"},
                {"room_no": 104, "floor": 0, "building": "D Block"},
                {"room_no": 105, "floor": 0, "building": "D Block"},
                {"room_no": 106, "floor": 0, "building": "D Block"},
                {"room_no": 201, "floor": 1, "building": "D Block"},
                {"room_no": 202, "floor": 1, "building": "D Block"},
                {"room_no": 203, "floor": 1, "building": "D Block"},
                {"room_no": 204, "floor": 1, "building": "D Block"},
                {"room_no": 205, "floor": 1, "building": "D Block"},
                {"room_no": 206, "floor": 1, "building": "D Block"},
                {"room_no": 301, "floor": 2, "building": "D Block"},
                {"room_no": 302, "floor": 2, "building": "D Block"},
                {"room_no": 303, "floor": 2, "building": "D Block"},
                {"room_no": 304, "floor": 2, "building": "D Block"},
                {"room_no": 305, "floor": 2, "building": "D Block"},
                {"room_no": 306, "floor": 2, "building": "D Block"},
                {"room_no": 401, "floor": 3, "building": "D Block"},
                {"room_no": 402, "floor": 3, "building": "D Block"},
                {"room_no": 403, "floor": 3, "building": "D Block"},
                {"room_no": 404, "floor": 3, "building": "D Block"},
                {"room_no": 405, "floor": 3, "building": "D Block"},
                {"room_no": 406, "floor": 3, "building": "D Block"},
                # Siemens Block rooms (Ground: 101-120, 1st: 201-220, 2nd: 301-320, 3rd: 401-420, 4th: 501-520)
                # Ground Floor (0): 101-120
                {"room_no": 101, "floor": 0, "building": "Siemens Block"},
                {"room_no": 102, "floor": 0, "building": "Siemens Block"},
                {"room_no": 103, "floor": 0, "building": "Siemens Block"},
                {"room_no": 104, "floor": 0, "building": "Siemens Block"},
                {"room_no": 105, "floor": 0, "building": "Siemens Block"},
                {"room_no": 106, "floor": 0, "building": "Siemens Block"},
                {"room_no": 107, "floor": 0, "building": "Siemens Block"},
                {"room_no": 108, "floor": 0, "building": "Siemens Block"},
                {"room_no": 109, "floor": 0, "building": "Siemens Block"},
                {"room_no": 110, "floor": 0, "building": "Siemens Block"},
                {"room_no": 111, "floor": 0, "building": "Siemens Block"},
                {"room_no": 112, "floor": 0, "building": "Siemens Block"},
                {"room_no": 113, "floor": 0, "building": "Siemens Block"},
                {"room_no": 114, "floor": 0, "building": "Siemens Block"},
                {"room_no": 115, "floor": 0, "building": "Siemens Block"},
                {"room_no": 116, "floor": 0, "building": "Siemens Block"},
                {"room_no": 117, "floor": 0, "building": "Siemens Block"},
                {"room_no": 118, "floor": 0, "building": "Siemens Block"},
                {"room_no": 119, "floor": 0, "building": "Siemens Block"},
                {"room_no": 120, "floor": 0, "building": "Siemens Block"},
                # 1st Floor (1): 201-220
                {"room_no": 201, "floor": 1, "building": "Siemens Block"},
                {"room_no": 202, "floor": 1, "building": "Siemens Block"},
                {"room_no": 203, "floor": 1, "building": "Siemens Block"},
                {"room_no": 204, "floor": 1, "building": "Siemens Block"},
                {"room_no": 205, "floor": 1, "building": "Siemens Block"},
                {"room_no": 206, "floor": 1, "building": "Siemens Block"},
                {"room_no": 207, "floor": 1, "building": "Siemens Block"},
                {"room_no": 208, "floor": 1, "building": "Siemens Block"},
                {"room_no": 209, "floor": 1, "building": "Siemens Block"},
                {"room_no": 210, "floor": 1, "building": "Siemens Block"},
                {"room_no": 211, "floor": 1, "building": "Siemens Block"},
                {"room_no": 212, "floor": 1, "building": "Siemens Block"},
                {"room_no": 213, "floor": 1, "building": "Siemens Block"},
                {"room_no": 214, "floor": 1, "building": "Siemens Block"},
                {"room_no": 215, "floor": 1, "building": "Siemens Block"},
                {"room_no": 216, "floor": 1, "building": "Siemens Block"},
                {"room_no": 217, "floor": 1, "building": "Siemens Block"},
                {"room_no": 218, "floor": 1, "building": "Siemens Block"},
                {"room_no": 219, "floor": 1, "building": "Siemens Block"},
                {"room_no": 220, "floor": 1, "building": "Siemens Block"},
                # 2nd Floor (2): 301-320
                {"room_no": 301, "floor": 2, "building": "Siemens Block"},
                {"room_no": 302, "floor": 2, "building": "Siemens Block"},
                {"room_no": 303, "floor": 2, "building": "Siemens Block"},
                {"room_no": 304, "floor": 2, "building": "Siemens Block"},
                {"room_no": 305, "floor": 2, "building": "Siemens Block"},
                {"room_no": 306, "floor": 2, "building": "Siemens Block"},
                {"room_no": 307, "floor": 2, "building": "Siemens Block"},
                {"room_no": 308, "floor": 2, "building": "Siemens Block"},
                {"room_no": 309, "floor": 2, "building": "Siemens Block"},
                {"room_no": 310, "floor": 2, "building": "Siemens Block"},
                {"room_no": 311, "floor": 2, "building": "Siemens Block"},
                {"room_no": 312, "floor": 2, "building": "Siemens Block"},
                {"room_no": 313, "floor": 2, "building": "Siemens Block"},
                {"room_no": 314, "floor": 2, "building": "Siemens Block"},
                {"room_no": 315, "floor": 2, "building": "Siemens Block"},
                {"room_no": 316, "floor": 2, "building": "Siemens Block"},
                {"room_no": 317, "floor": 2, "building": "Siemens Block"},
                {"room_no": 318, "floor": 2, "building": "Siemens Block"},
                {"room_no": 319, "floor": 2, "building": "Siemens Block"},
                {"room_no": 320, "floor": 2, "building": "Siemens Block"},
                # 3rd Floor (3): 401-420
                {"room_no": 401, "floor": 3, "building": "Siemens Block"},
                {"room_no": 402, "floor": 3, "building": "Siemens Block"},
                {"room_no": 403, "floor": 3, "building": "Siemens Block"},
                {"room_no": 404, "floor": 3, "building": "Siemens Block"},
                {"room_no": 405, "floor": 3, "building": "Siemens Block"},
                {"room_no": 406, "floor": 3, "building": "Siemens Block"},
                {"room_no": 407, "floor": 3, "building": "Siemens Block"},
                {"room_no": 408, "floor": 3, "building": "Siemens Block"},
                {"room_no": 409, "floor": 3, "building": "Siemens Block"},
                {"room_no": 410, "floor": 3, "building": "Siemens Block"},
                {"room_no": 411, "floor": 3, "building": "Siemens Block"},
                {"room_no": 412, "floor": 3, "building": "Siemens Block"},
                {"room_no": 413, "floor": 3, "building": "Siemens Block"},
                {"room_no": 414, "floor": 3, "building": "Siemens Block"},
                {"room_no": 415, "floor": 3, "building": "Siemens Block"},
                {"room_no": 416, "floor": 3, "building": "Siemens Block"},
                {"room_no": 417, "floor": 3, "building": "Siemens Block"},
                {"room_no": 418, "floor": 3, "building": "Siemens Block"},
                {"room_no": 419, "floor": 3, "building": "Siemens Block"},
                {"room_no": 420, "floor": 3, "building": "Siemens Block"},
                # 4th Floor (4): 501-520
                {"room_no": 501, "floor": 4, "building": "Siemens Block"},
                {"room_no": 502, "floor": 4, "building": "Siemens Block"},
                {"room_no": 503, "floor": 4, "building": "Siemens Block"},
                {"room_no": 504, "floor": 4, "building": "Siemens Block"},
                {"room_no": 505, "floor": 4, "building": "Siemens Block"},
                {"room_no": 506, "floor": 4, "building": "Siemens Block"},
                {"room_no": 507, "floor": 4, "building": "Siemens Block"},
                {"room_no": 508, "floor": 4, "building": "Siemens Block"},
                {"room_no": 509, "floor": 4, "building": "Siemens Block"},
                {"room_no": 510, "floor": 4, "building": "Siemens Block"},
                {"room_no": 511, "floor": 4, "building": "Siemens Block"},
                {"room_no": 512, "floor": 4, "building": "Siemens Block"},
                {"room_no": 513, "floor": 4, "building": "Siemens Block"},
                {"room_no": 514, "floor": 4, "building": "Siemens Block"},
                {"room_no": 515, "floor": 4, "building": "Siemens Block"},
                {"room_no": 516, "floor": 4, "building": "Siemens Block"},
                {"room_no": 517, "floor": 4, "building": "Siemens Block"},
                {"room_no": 518, "floor": 4, "building": "Siemens Block"},
                {"room_no": 519, "floor": 4, "building": "Siemens Block"},
                {"room_no": 520, "floor": 4, "building": "Siemens Block"},
                # Freshman Block rooms (Ground: 101-120, 1st: 201-220, 2nd: 301-320, 3rd: 401-420, 4th: 501-520)
                # Ground Floor (0): 101-120
                {"room_no": 101, "floor": 0, "building": "Freshman Block"},
                {"room_no": 102, "floor": 0, "building": "Freshman Block"},
                {"room_no": 103, "floor": 0, "building": "Freshman Block"},
                {"room_no": 104, "floor": 0, "building": "Freshman Block"},
                {"room_no": 105, "floor": 0, "building": "Freshman Block"},
                {"room_no": 106, "floor": 0, "building": "Freshman Block"},
                {"room_no": 107, "floor": 0, "building": "Freshman Block"},
                {"room_no": 108, "floor": 0, "building": "Freshman Block"},
                {"room_no": 109, "floor": 0, "building": "Freshman Block"},
                {"room_no": 110, "floor": 0, "building": "Freshman Block"},
                {"room_no": 111, "floor": 0, "building": "Freshman Block"},
                {"room_no": 112, "floor": 0, "building": "Freshman Block"},
                {"room_no": 113, "floor": 0, "building": "Freshman Block"},
                {"room_no": 114, "floor": 0, "building": "Freshman Block"},
                {"room_no": 115, "floor": 0, "building": "Freshman Block"},
                {"room_no": 116, "floor": 0, "building": "Freshman Block"},
                {"room_no": 117, "floor": 0, "building": "Freshman Block"},
                {"room_no": 118, "floor": 0, "building": "Freshman Block"},
                {"room_no": 119, "floor": 0, "building": "Freshman Block"},
                {"room_no": 120, "floor": 0, "building": "Freshman Block"},
                # 1st Floor (1): 201-220
                {"room_no": 201, "floor": 1, "building": "Freshman Block"},
                {"room_no": 202, "floor": 1, "building": "Freshman Block"},
                {"room_no": 203, "floor": 1, "building": "Freshman Block"},
                {"room_no": 204, "floor": 1, "building": "Freshman Block"},
                {"room_no": 205, "floor": 1, "building": "Freshman Block"},
                {"room_no": 206, "floor": 1, "building": "Freshman Block"},
                {"room_no": 207, "floor": 1, "building": "Freshman Block"},
                {"room_no": 208, "floor": 1, "building": "Freshman Block"},
                {"room_no": 209, "floor": 1, "building": "Freshman Block"},
                {"room_no": 210, "floor": 1, "building": "Freshman Block"},
                {"room_no": 211, "floor": 1, "building": "Freshman Block"},
                {"room_no": 212, "floor": 1, "building": "Freshman Block"},
                {"room_no": 213, "floor": 1, "building": "Freshman Block"},
                {"room_no": 214, "floor": 1, "building": "Freshman Block"},
                {"room_no": 215, "floor": 1, "building": "Freshman Block"},
                {"room_no": 216, "floor": 1, "building": "Freshman Block"},
                {"room_no": 217, "floor": 1, "building": "Freshman Block"},
                {"room_no": 218, "floor": 1, "building": "Freshman Block"},
                {"room_no": 219, "floor": 1, "building": "Freshman Block"},
                {"room_no": 220, "floor": 1, "building": "Freshman Block"},
                # 2nd Floor (2): 301-320
                {"room_no": 301, "floor": 2, "building": "Freshman Block"},
                {"room_no": 302, "floor": 2, "building": "Freshman Block"},
                {"room_no": 303, "floor": 2, "building": "Freshman Block"},
                {"room_no": 304, "floor": 2, "building": "Freshman Block"},
                {"room_no": 305, "floor": 2, "building": "Freshman Block"},
                {"room_no": 306, "floor": 2, "building": "Freshman Block"},
                {"room_no": 307, "floor": 2, "building": "Freshman Block"},
                {"room_no": 308, "floor": 2, "building": "Freshman Block"},
                {"room_no": 309, "floor": 2, "building": "Freshman Block"},
                {"room_no": 310, "floor": 2, "building": "Freshman Block"},
                {"room_no": 311, "floor": 2, "building": "Freshman Block"},
                {"room_no": 312, "floor": 2, "building": "Freshman Block"},
                {"room_no": 313, "floor": 2, "building": "Freshman Block"},
                {"room_no": 314, "floor": 2, "building": "Freshman Block"},
                {"room_no": 315, "floor": 2, "building": "Freshman Block"},
                {"room_no": 316, "floor": 2, "building": "Freshman Block"},
                {"room_no": 317, "floor": 2, "building": "Freshman Block"},
                {"room_no": 318, "floor": 2, "building": "Freshman Block"},
                {"room_no": 319, "floor": 2, "building": "Freshman Block"},
                {"room_no": 320, "floor": 2, "building": "Freshman Block"},
                # 3rd Floor (3): 401-420
                {"room_no": 401, "floor": 3, "building": "Freshman Block"},
                {"room_no": 402, "floor": 3, "building": "Freshman Block"},
                {"room_no": 403, "floor": 3, "building": "Freshman Block"},
                {"room_no": 404, "floor": 3, "building": "Freshman Block"},
                {"room_no": 405, "floor": 3, "building": "Freshman Block"},
                {"room_no": 406, "floor": 3, "building": "Freshman Block"},
                {"room_no": 407, "floor": 3, "building": "Freshman Block"},
                {"room_no": 408, "floor": 3, "building": "Freshman Block"},
                {"room_no": 409, "floor": 3, "building": "Freshman Block"},
                {"room_no": 410, "floor": 3, "building": "Freshman Block"},
                {"room_no": 411, "floor": 3, "building": "Freshman Block"},
                {"room_no": 412, "floor": 3, "building": "Freshman Block"},
                {"room_no": 413, "floor": 3, "building": "Freshman Block"},
                {"room_no": 414, "floor": 3, "building": "Freshman Block"},
                {"room_no": 415, "floor": 3, "building": "Freshman Block"},
                {"room_no": 416, "floor": 3, "building": "Freshman Block"},
                {"room_no": 417, "floor": 3, "building": "Freshman Block"},
                {"room_no": 418, "floor": 3, "building": "Freshman Block"},
                {"room_no": 419, "floor": 3, "building": "Freshman Block"},
                {"room_no": 420, "floor": 3, "building": "Freshman Block"},
                # 4th Floor (4): 501-520
                {"room_no": 501, "floor": 4, "building": "Freshman Block"},
                {"room_no": 502, "floor": 4, "building": "Freshman Block"},
                {"room_no": 503, "floor": 4, "building": "Freshman Block"},
                {"room_no": 504, "floor": 4, "building": "Freshman Block"},
                {"room_no": 505, "floor": 4, "building": "Freshman Block"},
                {"room_no": 506, "floor": 4, "building": "Freshman Block"},
                {"room_no": 507, "floor": 4, "building": "Freshman Block"},
                {"room_no": 508, "floor": 4, "building": "Freshman Block"},
                {"room_no": 509, "floor": 4, "building": "Freshman Block"},
                {"room_no": 510, "floor": 4, "building": "Freshman Block"},
                {"room_no": 511, "floor": 4, "building": "Freshman Block"},
                {"room_no": 512, "floor": 4, "building": "Freshman Block"},
                {"room_no": 513, "floor": 4, "building": "Freshman Block"},
                {"room_no": 514, "floor": 4, "building": "Freshman Block"},
                {"room_no": 515, "floor": 4, "building": "Freshman Block"},
                {"room_no": 516, "floor": 4, "building": "Freshman Block"},
                {"room_no": 517, "floor": 4, "building": "Freshman Block"},
                {"room_no": 518, "floor": 4, "building": "Freshman Block"},
                {"room_no": 519, "floor": 4, "building": "Freshman Block"},
                {"room_no": 520, "floor": 4, "building": "Freshman Block"},
                # Central Block - Special rooms for different departments
                {"room_no": 1, "floor": 0, "building": "Central Block", "description": "Management"},
                {"room_no": 1, "floor": 1, "building": "Central Block", "description": "Training and Placement Center"},
                {"room_no": 1, "floor": 2, "building": "Central Block", "description": "Library"},
                {"room_no": 1, "floor": 3, "building": "Central Block", "description": "Reference Library"},
                
            ],
            "faculties": [
                # CSE Department faculties (example)
                {"name": "Dr. John Doe", "email": "john.doe@university.edu", "designation": "Professor", "department": "Computer Science and Engineering", "room": 101, "building": "A Block", "floor": 1},
                {"name": "Dr. Jane Smith", "email": "jane.smith@university.edu", "designation": "Associate Professor", "department": "Computer Science and Engineering", "room": 102, "building": "A Block", "floor": 1},
                # CIC Department faculties
                {"name": "Dr. Rajesh Kumar", "email": "rajesh.kumar@university.edu", "designation": "Professor", "department": "Cybersecurity, IOT and Blockchain technology", "room": 201, "building": "B Block", "floor": 2},
                # Add more faculties as needed
            ],
            "sections": [
                # CIC-2 Sections (only A and B) - All years
                {"name": "A", "year": "1st", "department": "Cybersecurity, IOT and Blockchain technology", "room": 101, "building": "A Block", "floor": 0},
                {"name": "B", "year": "1st", "department": "Cybersecurity, IOT and Blockchain technology", "room": 102, "building": "A Block", "floor": 0},
                {"name": "A", "year": "2nd", "department": "Cybersecurity, IOT and Blockchain technology", "room": 103, "building": "A Block", "floor": 0},
                {"name": "B", "year": "2nd", "department": "Cybersecurity, IOT and Blockchain technology", "room": 104, "building": "A Block", "floor": 0},
                # CSE-8 Sections (A to H) - All years
                {"name": "A", "year": "1st", "department": "Computer Science and Engineering", "room": 201, "building": "A Block", "floor": 1},
                {"name": "B", "year": "1st", "department": "Computer Science and Engineering", "room": 202, "building": "A Block", "floor": 1},
                {"name": "C", "year": "1st", "department": "Computer Science and Engineering", "room": 203, "building": "A Block", "floor": 1},
                {"name": "D", "year": "1st", "department": "Computer Science and Engineering", "room": 204, "building": "A Block", "floor": 1},
                {"name": "E", "year": "2nd", "department": "Computer Science and Engineering", "room": 205, "building": "A Block", "floor": 1},
                {"name": "F", "year": "2nd", "department": "Computer Science and Engineering", "room": 206, "building": "A Block", "floor": 1},
                {"name": "G", "year": "3rd", "department": "Computer Science and Engineering", "room": 301, "building": "B Block", "floor": 2},
                {"name": "H", "year": "3rd", "department": "Computer Science and Engineering", "room": 302, "building": "B Block", "floor": 2},
                {"name": "A", "year": "4th", "department": "Computer Science and Engineering", "room": 401, "building": "B Block", "floor": 3},
                {"name": "B", "year": "4th", "department": "Computer Science and Engineering", "room": 402, "building": "B Block", "floor": 3},
                # Add more sections for other departments as needed
            ],
        }

        if not any(custom_data.values()):
            print("No data available.")
            return

        for item in custom_data["buildings"]:
            item_dict: Dict[str, Any] = item
            get_or_create_building(
                db,
                name=str(item_dict["name"]),
                code=str(item_dict["code"]),
                floors=int(item_dict["floors"]),
            )

        for item in custom_data["departments"]:
            item_dict = item
            get_or_create_department(
                db,
                name=str(item_dict["name"]),
                code=str(item_dict["code"]),
            )

        for item in custom_data["rooms"]:
            item_dict = item
            get_or_create_room(
                db,
                room_no=int(item_dict["room_no"]),
                floor=int(item_dict["floor"]),
                building_name=str(item_dict["building"]),
            )

        for item in custom_data["faculties"]:
            item_dict = item
            department = get_or_create_department(
                db,
                name=str(item_dict["department"]),
                code=str(item_dict.get("department_code", str(item_dict["department"])[:3].upper())),
            )
            room = get_or_create_room(
                db,
                room_no=int(item_dict["room"]),
                floor=int(item_dict.get("floor", 1)),
                building_name=str(item_dict.get("building", "")),
            )

            faculty = db.query(Faculty).filter(Faculty.email == str(item_dict["email"])).first()
            if faculty is None:
                faculty = Faculty(
                    name=str(item_dict["name"]),
                    email=str(item_dict["email"]),
                    designation=str(item_dict["designation"]),
                    department_id=department.id,
                    room_id=room.id,
                )
                db.add(faculty)
                db.commit()
                db.refresh(faculty)

        for item in custom_data["sections"]:
            item_dict = item
            department = get_or_create_department(
                db,
                name=str(item_dict["department"]),
                code=str(item_dict.get("department_code", str(item_dict["department"])[:3].upper())),
            )
            room = get_or_create_room(
                db,
                room_no=int(item_dict["room"]),
                floor=int(item_dict.get("floor", 0)),
                building_name=str(item_dict.get("building", "")),
            )

            section = db.query(Section).filter(
                Section.name == str(item_dict["name"]), 
                Section.year == str(item_dict.get("year", "1st")),
                Section.department_id == department.id
            ).first()
            if section is None:
                section = Section(
                    name=str(item_dict["name"]),
                    year=str(item_dict.get("year", "1st")),
                    department_id=department.id,
                    room_id=room.id,
                )
                db.add(section)
                db.commit()
                db.refresh(section)

        print("Finished processing custom data.")
    finally:
        db.close()


if __name__ == "__main__":
    insert_custom_data()
