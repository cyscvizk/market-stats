from server.models.api import MessageResponse, HealthResponse
# from gemini import gemini_stock_data_colelctor

def check_health() -> HealthResponse:
    """Check if the API is healthy."""
    return HealthResponse(status="healthy")

def process_message(message: str) -> MessageResponse:
    """Process the incoming message and return response with message details."""
    
    # 1) data = gemini_stock_data_colelctor(message)
    # 2) function that stores data in db
    # 3) call prediciton script
    # 4) prepares final response with gemini again
    return MessageResponse(
        received_message=message,
        length=len(message)
    )
