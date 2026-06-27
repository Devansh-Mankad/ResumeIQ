import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "database.db"


def get_db_connection():
    """
    Create and return a SQLite database connection.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    """
    Create all database tables using schema.sql
    """
    conn = get_db_connection()
    schema_path = BASE_DIR / "schema.sql"
    with open(schema_path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully.")


def close_connection(conn):
    """
    Close the database connection safely.
    """
    if conn:
        conn.close()