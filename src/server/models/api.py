from pydantic import BaseModel, Field
from typing import Optional


class MessageRequest(BaseModel):
    message: str = Field(..., min_length=1)

class MessageResponse(BaseModel):
    received_message: str

class HealthResponse(BaseModel):
    status: str

class DataResponse(BaseModel):
    symbol: str
    last_price: float
    green_daily_ytd: int
    red_daily_ytd: int
    probability: int

 # --------------------- USER ---------------------

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    
class UserResponse(BaseModel):
    message: str

class UserUpdate(BaseModel):
    username: str
    email: str
    password : str
    
class UserDetail(BaseModel):
    id: int
    username: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    created_at: str

# --------------------- PROBABILITY ---------------------

class ProbabilityCreate(BaseModel):
    user_id: int
    input_string: str
    stock_symbol: str
    probability_green: int
    probability_red: int
    created_at: str
    updated_at: str
    
class ProbabilityResponse(BaseModel):
    message: str

class ProbabilityUpdate(BaseModel):
    user_id: int
    input_string: str
    stock_symbol: str
    probability_green: int
    probability_red: int
    created_at: str
    updated_at: str
    
class ProbabilityDetail(BaseModel):
    id: int
    user_id: int
    input_string: str
    stock_symbol: str
    probability_green: int
    probability_red: int
    created_at: str
    updated_at: str

    
