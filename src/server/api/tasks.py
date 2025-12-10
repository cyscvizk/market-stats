from server.models.api import MessageResponse, HealthResponse
from server.api.gemini import get_stock_data
from server.api.prediction import get_probability_closing_red
from server.db_manager.sql_executor import execute_sql
from server.db_manager.user import sql_create_user

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
def create_user(user_data) -> dict:
    sql_statement = sql_create_user()
    result = execute_sql(sql_statement, params=(...))

    if result == True:
        return {"success": True, "message": "User created successfully"}
    elif isinstance(result, dict) and "error" in result:
        return {"success": False, **result}
    else:
        return {"success": False, "message": "Unknown error"}
