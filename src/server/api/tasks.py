from server.models.api import MessageResponse, HealthResponse
from server.api.gemini import get_stock_data
from server.api.prediction import get_probability_closing_red
from server.db_manager.sql_executor import execute_sql
from server.db_manager.user import (
    sql_create_user, sql_get_user_by_id, sql_update_user, 
    sql_delete_user, sql_list_users
)
from server.db_manager.probability import (
    sql_create_probability, sql_get_probability_by_id, 
    sql_get_probability_by_user_id, sql_update_probability,
    sql_delete_probability, sql_list_probabilities
)

def check_health() -> HealthResponse:
    """Check if the API is healthy."""
    return HealthResponse(status="healthy")

def process_message(message: str) -> MessageResponse:
    """Process the incoming message and return response with message details."""
    
    data_response = get_stock_data(message)
    #probability_response = get_probability_closing_red(message)
    
    # 1) data = gemini_stock_data_colelctor(message)
    # 2) function that stores data in db
    # 3) call prediciton script
    # 4) prepares final response with gemini again
    return MessageResponse(
        received_message=data_response,
    )

# --------------------- USER ---------------------

def create_user(user_data) -> dict:
    sql_statement = sql_create_user()
    result = execute_sql(sql_statement, params=(...))

    if result == True:
        return {"success": True, "message": "User created successfully"}
    elif isinstance(result, dict) and "error" in result:
        return {"success": False, **result}
    else:
        return {"success": False, "message": "Unknown error"}

def get_user(user_id: int):
    sql = sql_get_user_by_id()
    result = execute_sql(sql, params=(user_id,), fetch=True)
    if result:
        return result[0]  # Return first row
    return None

def update_user(user_id: int, user_data):
    sql = sql_update_user()
    params = (user_data.username, user_data.first_name,
              user_data.last_name, user_data.email,
              user_data.password, user_id)
    return execute_sql(sql, params=params)

def delete_user(user_id: int):
    sql = sql_delete_user()
    return execute_sql(sql, params=(user_id,))

def list_users():
    sql = sql_list_users()
    return execute_sql(sql, fetch=True)

# --------------------- PROBABILITY ---------------------

def create_probability(probability_data) -> dict:
    sql_statement = sql_create_probability()
    result = execute_sql(sql_statement, params=(...))

    if result == True:
        return {"success": True, "message": "Probability created successfully"}
    elif isinstance(result, dict) and "error" in result:
        return {"success": False, **result}
    else:
        return {"success": False, "message": "Unknown error"}

def get_probability(probability_id: int):
    sql = sql_get_probability_by_id()
    result = execute_sql(sql, params=(probability_id,), fetch=True)
    if result:
        return result[0]  # Return first row
    return None

def update_probability(probability_id: int, probability_data):
    sql = sql_update_probability()
    params = (probability_data.user_id, probability_data.input_string,
              probability_data.stock_symbol, probability_data.probability_green,
              probability_id)
    return execute_sql(sql, params=params)

def delete_probability(probability_id: int):
    sql = sql_delete_probability()
    return execute_sql(sql, params=(probability_id,))

def list_probabilities(user_id: int = None):
    if user_id is not None:
        sql = sql_get_probability_by_user_id()
        return execute_sql(sql, params=(user_id,), fetch=True)
    else:
        sql = sql_list_probabilities()
        return execute_sql(sql, fetch=True)

