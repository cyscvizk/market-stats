from pydantic import BaseModel, Field


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