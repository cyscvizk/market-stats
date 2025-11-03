from fastapi import APIRouter
from server.models.api import MessageRequest, MessageResponse, HealthResponse
from server.api.tasks import check_health, process_message

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health():
    """Health check endpoint."""
    return check_health()


@router.post("/message", response_model=MessageResponse)
def message(request: MessageRequest):
    """Process a message and return details about it."""
    return process_message(request.message)
