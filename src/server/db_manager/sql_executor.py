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
        try:
            cursor.execute(sql, params)
            result = conn.commit()
            conn.close()
            print(result) #### as indicator for where we need to handle the exceptions of entries being present already
        except Exception as e:
            print(f"SQL Execution Error: {e}")
            conn.close()
            return False
    else:
        print("userdata not set")
        return False

    return True