# main function to execute sql statement (sql statement is argument inserted)

# step 1: initiate database client to communicate with db
# step 2: place cursor
# step 3: execute sql statement
# step 4: commit changes
# step 5: close connection

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "market_stats.db"


def execute_sql(sql: str, params: tuple = None, fetch: bool = False):
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if params:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)

    rows = cursor.fetchall() if fetch else None
    conn.commit()
    conn.close()

    return rows
