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
    conn.row_factory = sqlite3.Row  # Return dict-like objects instead of tuples
    cursor = conn.cursor()

    try:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

        if fetch:
            rows = cursor.fetchall()
            # Convert Row objects to dictionaries
            return [dict(row) for row in rows] if rows else []
        
        conn.commit()
        return True

    except sqlite3.IntegrityError as e:
        # This happens when UNIQUE constraint is violated
        error_message = str(e)
        if "username" in error_message:
            return {"error": "username_taken", "message": "This username already exists"}
        elif "email" in error_message:
            return {"error": "email_taken", "message": "This email already exists"}
        return {"error": "integrity_error", "message": str(e)}

    except sqlite3.Error as e:
        return {"error": "database_error", "message": str(e)}

    finally:
        conn.close()
