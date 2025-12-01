# functions to create sql queries for all crud tasks

# user create function sql statement creation

# -------------------- CREATE --------------------
def sql_create_user():
    return """
        INSERT INTO user_table 
        (username, first_name, last_name, email, password)
        VALUES (?, ?, ?, ?, ?)
    """


# -------------------- READ --------------------
def sql_get_user_by_id():
    return "SELECT * FROM user_table WHERE id = ?"


def sql_get_user_by_username():
    return "SELECT * FROM user_table WHERE username = ?"


# -------------------- UPDATE --------------------
def sql_update_user():
    return """
        UPDATE user_table
        SET 
            username = ?, 
            first_name = ?, 
            last_name = ?, 
            email = ?, 
            password = ?, 
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """


# -------------------- DELETE --------------------
def sql_delete_user():
    return "DELETE FROM user_table WHERE id = ?"


# -------------------- LIST --------------------
def sql_list_users():
    return "SELECT * FROM user_table ORDER BY created_at DESC"
