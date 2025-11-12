from google.genai import types
from server.api.prompts import DATA_FETCH_SYSTEM_PROMPT
from server.models.api import DataResponse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_probability_closing_red(data_response: DataResponse) -> float: 

    closing_red_probability = data_response.red_daily_ytd / (data_response.green_daily_ytd + data_response.red_daily_ytd) * 100

    return closing_red_probability