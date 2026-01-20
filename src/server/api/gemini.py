from google import genai
from google.genai import types
from server.api.prompts import DATA_FETCH_SYSTEM_PROMPT, VALUATION_SYSTEM_PROMPT

client = genai.Client()

def evaluate_stock(symbol: str) -> str:
    grounding_tool = types.Tool(
        google_search=types.GoogleSearch()
    )

    config = types.GenerateContentConfig(
        tools=[grounding_tool],
        system_instruction=VALUATION_SYSTEM_PROMPT
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Evaluate the stock: {symbol}",
        config=config,
    )

    return response.text


def get_stock_data(user_input: str) -> str: 
        
    grounding_tool = types.Tool(    
        google_search=types.GoogleSearch()  
    )   
        
    config = types.GenerateContentConfig(   
        tools=[grounding_tool],
        system_instruction=DATA_FETCH_SYSTEM_PROMPT
    )   
        
    response = client.models.generate_content(  
        model="gemini-2.5-flash", 
        contents=user_input,    
        config=config,  
    )   
        
    return response.text