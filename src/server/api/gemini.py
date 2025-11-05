from google import genai
from google.genai import types
from server.api.prompts import DATA_FETCH_SYSTEM_PROMPT
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = genai.Client()

def get_stock_data(user_input: str) -> str: 
        
    grounding_tool = types.Tool(    
        google_search=types.GoogleSearch()  
    )   
        
    config = types.GenerateContentConfig(   
        tools=[grounding_tool],
        system_instruction=DATA_FETCH_SYSTEM_PROMPT
    )   
        
    response = client.models.generate_content(  
        model="gemini-2.5-pro", 
        contents=user_input,    
        config=config,  
    )   
        
    return response.text