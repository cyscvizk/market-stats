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
    
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    #required and optinal fields still missing
    
class UserResponse(BaseModel):
    message: str
    