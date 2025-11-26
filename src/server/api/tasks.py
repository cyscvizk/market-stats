from server.models.api import MessageResponse, HealthResponse
from server.api.gemini import get_stock_data
from server.api.prediction import get_probability_closing_red
from server.db_manager.sql_executor import execute_sql
from server.db_manager.user import generate_create_user_sql

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
def create_user(user_data) -> str:
    """Create a new user in the database."""
    sql_statement = generate_create_user_sql(user_data)
    success = execute_sql(sql_statement)
    if success != True:
        return "User creation failed."
    return "User created successfully."