from fastapi import APIRouter
from server.models.api import MessageRequest, MessageResponse, HealthResponse, UserCreate, UserResponse
from server.api.tasks import check_health, process_message, create_user
from fastapi import HTTPException

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health():
    """Health check endpoint."""
    return check_health()


@router.post("/message", response_model=MessageResponse)
def message(request: MessageRequest):
    """Process a message and return details about it."""
    return process_message(request.message)

@router.post("/user_create", response_model=UserResponse)
def message(user_data: UserCreate):
    
    success_message = create_user(user_data)
    
    return {"message": success_message}

@router.post("/user_create", response_model=UserResponse)
def create_user_endpoint(user_data: UserCreate):
    result = create_user(user_data)

    if not result.get("success"):
        if result.get("error") == "username_taken":
            raise HTTPException(status_code=409, detail="Username already exists")
        elif result.get("error") == "email_taken":
            raise HTTPException(status_code=409, detail="Email already exists")
        raise HTTPException(status_code=500, detail="User creation failed")

    return {"message": result["message"]}
