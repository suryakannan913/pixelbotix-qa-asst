from google import genai
from google.genai import types 
import os

from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

def generate_answer(prompt: str):
    """
    Generate a context-aware answer using Gemini 2.5-flash
    with robust handling for different response structures.
    """
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=4096,
            )
        )
        
        # Properly extract the response text
        if hasattr(response, 'text'):
            return response.text
        elif hasattr(response, 'candidates') and len(response.candidates) > 0:
            return response.candidates[0].content.parts[0].text
        else:
            return "Sorry, I couldn't generate a proper response. Please try again."
    except Exception as e:
        return f"Error generating answer: {str(e)}"