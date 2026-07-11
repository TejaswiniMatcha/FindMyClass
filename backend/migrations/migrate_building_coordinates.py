from sqlalchemy import text

from app.database import engine


MIGRATION_SQL = """
ALTER TABLE buildings
    ADD COLUMN IF NOT EXISTS latitude numeric(9,6),
    ADD COLUMN IF NOT EXISTS longitude numeric(9,6);
"""


def run_migration() -> None:
    with engine.begin() as connection:
        connection.execute(text(MIGRATION_SQL))
    print("✅ Migration complete: added buildings.latitude and buildings.longitude.")


if __name__ == "__main__":
    run_migration()
