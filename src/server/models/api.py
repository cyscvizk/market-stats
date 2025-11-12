from pydantic import BaseModel, Field


class MessageRequest(BaseModel):
    message: str = Field(..., min_length=1)

class DataResponse(BaseModel):
    symbol: str
    last_price: float
    green_daily_ytd: int
    red_daily_ytd: int

class MessageResponse(BaseModel):
    data_response: DataResponse
    closing_red_probability: float
    
class HealthResponse(BaseModel):
    status: str


