"""
Probability table SQL query builders.

Contains functions to generate SQL statements for CRUD operations on the probability_table.
"""

def sql_create_probability():
    return """
        INSERT INTO probability_table 
        (user_id, input_string, stock_symbol, probability_green)
        VALUES (?, ?, ?, ?)
    """

# -------------------- READ --------------------

def sql_get_probability_by_id():
    return "SELECT * FROM probability_table WHERE id = ?"

def sql_get_probability_by_user_id():
    return "SELECT * FROM probability_table WHERE user_id = ?"

def sql_get_probability_by_stock_symbol():
    return "SELECT * FROM probability_table WHERE stock_symbol = ? ORDER BY created_at DESC"

# -------------------- UPDATE --------------------
def sql_update_probability():
    return """
        UPDATE probability_table
        SET 
            user_id = ?, 
            input_string = ?, 
            stock_symbol = ?, 
            probability_green = ?, 
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """

# -------------------- DELETE --------------------
def sql_delete_probability():
    return "DELETE FROM probability_table WHERE id = ?"

# -------------------- LIST --------------------
def sql_list_probabilities():
    return "SELECT * FROM probability_table ORDER BY created_at DESC"

def sql_list_probabilities_by_user_id(user_id: int):    
    return "SELECT * FROM probability_table WHERE user_id = ? ORDER BY created_at DESC"

