from fastapi import APIRouter, HTTPException, Query
from server.models.api import (
    MessageRequest, MessageResponse, HealthResponse, 
    UserCreate, UserResponse, UserDetail, UserUpdate,
    ProbabilityCreate, ProbabilityResponse, ProbabilityDetail, ProbabilityUpdate,
    ValuationResponse, StockSymbolQuery
)
from server.api.tasks import (
    check_health, process_message, 
    create_user, get_user, update_user, delete_user, list_users,
    create_probability, get_probability, update_probability, delete_probability,
    list_probabilities_by_user_id, list_probabilities_by_stock_symbol,
    get_stock_valuation
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
    """
    Create a new user in the system.

    - **username**: Unique username (required)
    - **email**: Unique email address (required)
    - **password**: User password (required, will be hashed)
    - **first_name**: Optional first name
    - **last_name**: Optional last name

    Returns success message or error if username/email exists.
    """
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
    """Get user details by user ID."""
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/user/{user_id}", response_model=UserResponse)
def update_user_endpoint(user_id: int, user_data: UserUpdate):
    """Update user information. Password will be re-hashed if changed."""
    success = update_user(user_id, user_data)
    if not success:
        raise HTTPException(
            status_code=400,
            detail="Failed to update user. Please check that the user exists and data is valid."
        )
    return {"message": "User updated successfully"}

@router.delete("/user/{user_id}", response_model=UserResponse)
def delete_user_endpoint(user_id: int):
    """Delete a user from the system."""
    success = delete_user(user_id)
    if not success:
        raise HTTPException(
            status_code=400,
            detail="Failed to delete user. Please check that the user exists."
        )
    return {"message": "User deleted successfully"}

@router.get("/users", response_model=list[UserDetail])
def list_users_endpoint():
    """Get all users in the system."""
    users = list_users()
    if users is None:
        return []
    return users


# --------------------- PROBABILITY ---------------------

@router.post("/probability_create", response_model=ProbabilityResponse)
def create_probability_endpoint(probability_data: ProbabilityCreate):
    """
    Record a new trade probability.

    - **user_id**: ID of the user creating the probability
    - **input_string**: Description or input data
    - **stock_symbol**: Stock ticker symbol
    - **probability_green**: Probability value for green candle
    """
    result = create_probability(probability_data)

    if not result.get("success"):
        raise HTTPException(status_code=500, detail="Probability creation failed")

    return {"message": result["message"]}
    
@router.get("/probability/{probability_id}", response_model=ProbabilityDetail)
def get_probability_endpoint(probability_id: int):
    """Get details of a specific probability record by ID."""
    probability = get_probability(probability_id)
    if not probability:
        raise HTTPException(status_code=404, detail="Probability not found")
    return probability
    
@router.put("/probability/{probability_id}", response_model=ProbabilityResponse)
def update_probability_endpoint(probability_id: int, probability_data: ProbabilityUpdate):
    """Update an existing probability record."""
    success = update_probability(probability_id, probability_data)
    if not success:
        raise HTTPException(
            status_code=400,
            detail="Failed to update probability. Please check that the probability record exists and data is valid."
        )
    return {"message": "Probability updated successfully"}
    
@router.delete("/probability/{probability_id}", response_model=ProbabilityResponse)
def delete_probability_endpoint(probability_id: int):
    """Delete a probability record."""
    success = delete_probability(probability_id)
    if not success:
        raise HTTPException(
            status_code=400,
            detail="Failed to delete probability. Please check that the probability record exists."
        )
    return {"message": "Probability deleted successfully"}

@router.get("/probabilities/{user_id}", response_model=list[ProbabilityDetail])
def list_probabilities_by_user_id_endpoint(user_id: int):
    """Get all probability records for a specific user."""
    probabilities = list_probabilities_by_user_id(user_id)
    if probabilities is None:
        return []
    return probabilities

@router.get("/probabilities", response_model=list[ProbabilityDetail])
def list_probabilities_by_stock_symbol_endpoint(
    stock_symbol: str = Query(..., min_length=1, max_length=10, pattern="^[A-Z]+$", 
                               description="Stock ticker symbol (uppercase letters only)")
):
    """Get all probability records for a specific stock symbol (uppercase letters only)."""
    probabilities = list_probabilities_by_stock_symbol(stock_symbol)
    if probabilities is None:
        return []
    return probabilities

@router.get("/evaluate/{symbol}", response_model=ValuationResponse)
def evaluate_stock_endpoint(symbol: str):
    """Evaluate stock valuation using Gemini."""
    result = get_stock_valuation(symbol)
    if not result:
        raise HTTPException(status_code=500, detail="Stock evaluation failed")
    return result