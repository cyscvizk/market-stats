from fastapi import APIRouter
from server.models.api import MessageRequest, MessageResponse, HealthResponse
from server.api.tasks import check_health, process_message, create_user

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health():
    """Health check endpoint."""
    return check_health()


@router.post("/message", response_model=MessageResponse)
def message(request: MessageRequest):
    """Process a message and return details about it."""
    return process_message(request.message)

@router.post("/user_create", response_model=UserCreate)
def message(user_data: UserCreate):
    
    success_message = create_user(user_data)
    
    return str