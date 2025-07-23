# services/query_generator.py
import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
from google.api_core import retry
from google.api_core.exceptions import ResourceExhausted
from functools import lru_cache

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configuration
MODEL_NAME = 'models/gemini-1.0-pro-vision-latest'  # From your available models
FALLBACK_MODEL = 'models/gemini-1.5-flash-latest'  # Fallback option
RATE_LIMIT_DELAY = 2.0  # Seconds between requests

# Custom retry strategy
custom_retry = retry.Retry(
    initial=1.0,
    maximum=60.0,
    multiplier=2.0,
    deadline=300.0,  # 5 minute timeout
    predicate=retry.if_exception_type(
        ResourceExhausted,
        Exception
    )
)

@lru_cache(maxsize=100)
@custom_retry
def generate_sql(question: str) -> str:
    """Generate SQL from natural language question with robust error handling."""
    time.sleep(RATE_LIMIT_DELAY)  # Enforce rate limiting
    
    models_to_try = [MODEL_NAME, FALLBACK_MODEL]
    
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            
            prompt = f"""Convert this business question to SQL:
            
            DATABASE SCHEMA:
            1. eligibility (product_id, is_eligible, category)
            2. ad_metrics (product_id, ad_spend, clicks, cpc, roas)
            3. total_sales (product_id, total_sales, units_sold, profit)
            
            QUESTION: {question}
            
            IMPORTANT:
            - Return ONLY the SQL query
            - Use table aliases for clarity
            - Include proper JOINs when needed
            - For aggregate queries, include GROUP BY"""
            
            response = model.generate_content(prompt)
            return response.text.strip()
            
        except Exception as e:
            print(f"Error with model {model_name}: {str(e)}")
            if "quota" in str(e).lower() or "rate limit" in str(e).lower():
                # Exponential backoff for rate limits
                wait_time = min(60, 2 ** len(models_to_try))  # Cap at 60 seconds
                print(f"Rate limited. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
            continue
    
    raise Exception("All model attempts failed")

if __name__ == "__main__":
    test_question = "What is total sales?"
    print(f"Testing with question: {test_question}")
    try:
        print(generate_sql(test_question))
    except Exception as e:
        print(f"Failed to generate SQL: {e}")
        print("Possible solutions:")
        print("1. Check your Google Cloud billing status")
        print("2. Wait for quota to reset (usually hourly/daily)")
        print("3. Upgrade your plan at https://ai.google.dev/pricing")
        print("4. Try again later with reduced frequency")