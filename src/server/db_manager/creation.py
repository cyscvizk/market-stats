"""
Responsible for:
# create DB
# create tables
# define tabels
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "market_stats.db"


# --- Table definitions --------------------------------------------------------

USER_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS user_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    first_name TEXT,
    last_name TEXT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

PROBABILITY_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS probability_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    input_string TEXT NOT NULL,
    stock_symbol TEXT NOT NULL,
    probability_green REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user_table(id)
);
"""


# --- Creation functions -------------------------------------------------------

def create_database():
    """Creates database file if not present."""
    if not DB_PATH.exists():
        DB_PATH.touch()
        print(f"[DB] Created database at {DB_PATH}")
    else:
        print(f"[DB] Database already exists at {DB_PATH}")


def create_tables():
    """Creates required tables."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(USER_TABLE_SQL)
    cursor.execute(PROBABILITY_TABLE_SQL)

    conn.commit()
    conn.close()

    print("[DB] Tables created / already existed.")


def initialize_db():
    """Wrapper to initialize everything."""
    create_database()
    create_tables()
