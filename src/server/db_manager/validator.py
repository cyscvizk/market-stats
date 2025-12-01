# check if db is present
# check if tables are present and correct

import sqlite3
from pathlib import Path
from .creation import DB_PATH


REQUIRED_TABLES = {
    "user_table": {
        "id", "username", "first_name", "last_name",
        "email", "password", "created_at", "updated_at"
    },
    "probability_table": {
        "id", "user_id", "input_string", "stock_symbol",
        "probability_green", "created_at", "updated_at"
    }
}


def db_exists() -> bool:
    return DB_PATH.exists()


def get_table_columns(table: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table})")
    cols = {row[1] for row in cursor.fetchall()}  # row[1] = column name

    conn.close()
    return cols


def validate_tables():
    if not db_exists():
        return False, "Database does not exist."

    for table, required_cols in REQUIRED_TABLES.items():
        cols = get_table_columns(table)

        if not cols:
            return False, f"Missing table: {table}"

        missing = required_cols - cols
        if missing:
            return False, f"Table '{table}' missing columns: {', '.join(missing)}"

    return True, "Database and tables are valid."
