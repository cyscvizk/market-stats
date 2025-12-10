from fastapi import APIRouter, HTTPException
from server.models.api import (
    MessageRequest, MessageResponse, HealthResponse, 
    UserCreate, UserResponse, UserDetail, UserUpdate,
    ProbabilityCreate, ProbabilityResponse, ProbabilityDetail, ProbabilityUpdate
)
from server.api.tasks import (
    check_health, process_message, 
    create_user, get_user, update_user, delete_user,
    create_probability, get_probability, update_probability, delete_probability
)

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health():
    """Health check endpoint."""
    return check_health()


@router.post("/message", response_model=MessageResponse)
def message(request: MessageRequest):
    """Process a message and return details about it."""
    return process_message(request.message)


# --------------------- USER ---------------------


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

@router.get("/user/{user_id}", response_model=UserDetail)
def get_user_endpoint(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/user/{user_id}", response_model=UserResponse)
def update_user_endpoint(user_id: int, user_data: UserUpdate):
    success = update_user(user_id, user_data)
    if not success:
        raise HTTPException(status_code=400, detail="Update failed")
    return {"message": "User updated successfully"}

@router.delete("/user/{user_id}", response_model=UserResponse)
def delete_user_endpoint(user_id: int):
    success = delete_user(user_id)
    if not success:
        raise HTTPException(status_code=400, detail="Delete failed")
    return {"message": "User deleted successfully"}

# --------------------- PROBABILITY ---------------------

@router.post("/probability_create", response_model=ProbabilityResponse)
def create_probability_endpoint(probability_data: ProbabilityCreate):
    result = create_probability(probability_data)

    if not result.get("success"):
        raise HTTPException(status_code=500, detail="Probability creation failed")

    return {"message": result["message"]}
    
@router.get("/probability/{probability_id}", response_model=ProbabilityDetail)
def get_probability_endpoint(probability_id: int):
    probability = get_probability(probability_id)
    if not probability:
        raise HTTPException(status_code=404, detail="Probability not found")
    return probability
    
@router.put("/probability/{probability_id}", response_model=ProbabilityResponse)
def update_probability_endpoint(probability_id: int, probability_data: ProbabilityUpdate):
    success = update_probability(probability_id, probability_data)
    if not success:
        raise HTTPException(status_code=400, detail="Update failed")
    return {"message": "Probability updated successfully"}
    
@router.delete("/probability/{probability_id}", response_model=ProbabilityResponse)
def delete_probability_endpoint(probability_id: int):
    success = delete_probability(probability_id)
    if not success:
        raise HTTPException(status_code=400, detail="Delete failed")
    return {"message": "Probability deleted successfully"}
