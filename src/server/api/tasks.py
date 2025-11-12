from server.models.api import MessageResponse, HealthResponse
from server.api.gemini import get_stock_data, create_response_message
from server.api.prediction import get_probability_closing_red

def check_health() -> HealthResponse:
    """Check if the API is healthy."""
    return HealthResponse(status="healthy")

def process_message(message: str) -> MessageResponse:
    """Process the incoming message and return response with message details."""
    
    data_response = get_stock_data(message)
    # 2) function that stores data in db

    closing_red_probability = get_probability_closing_red(data_response)

    response_message = create_response_message(data_response, closing_red_probability, message)
    # 4) prepares final response with gemini again
    return MessageResponse(
        response_message=response_message,
        data_response=data_response,
        closing_red_probability=closing_red_probability
    )
