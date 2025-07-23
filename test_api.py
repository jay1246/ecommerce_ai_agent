# test_api.py
import requests
import json

# Local FastAPI endpoint
API_URL = "http://127.0.0.1:8000/ask"

# Test questions
TEST_QUESTIONS = [
    "What is the total sales?",
    "Which product has the highest ROAS?",
    "Show top 5 products by ad spend"
]

def run_tests():
    for question in TEST_QUESTIONS:
        print(f"\nTesting: '{question}'")
        
        # Send request to your API
        response = requests.post(
            API_URL,
            json={"question": question},
            headers={"Content-Type": "application/json"}
        )
        
        # Print results
        if response.status_code == 200:
            data = response.json()
            print("SQL Query:", data["sql_query"])
            print("Answer:", json.dumps(data["data"], indent=2))
            if data.get("visualization"):
                print("✅ Chart generated")
        else:
            print(f"❌ Error {response.status_code}:", response.text)

if __name__ == "__main__":
    run_tests()