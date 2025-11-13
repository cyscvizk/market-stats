from google import genai
from google.genai import types
from server.api.prompts import DATA_FETCH_SYSTEM_PROMPT
from server.models.api import DataResponse
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()

client = genai.Client()

def get_stock_data(user_input: str) -> DataResponse:

    grounding_tool = types.Tool(
        google_search=types.GoogleSearch()
    )

    config = types.GenerateContentConfig(
        tools=[grounding_tool],
        system_instruction=DATA_FETCH_SYSTEM_PROMPT,
        response_schema=DataResponse.model_json_schema()
    )

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=user_input,
        config=config,
    )

    # Extract JSON from response text
    text = response.text.strip()

    # Try to find JSON object in the response
    json_match = re.search(r'\{.*\}', text, re.DOTALL)
    if json_match:
        text = json_match.group(0)
    else:
        # Remove markdown code blocks if no JSON object found
        text = re.sub(r'^```json\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        text = text.strip()

    return DataResponse.model_validate_json(text)

def create_response_message(data_response: DataResponse, closing_red_probability: float, message: str) -> str:
    return_message = f"This is a placeholder"
    return return_message