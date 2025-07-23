from src.services.query_generator import generate_sql

# Test the function
test_question = "What is total sales?"
print("Testing with question:", test_question)
print("Generated SQL:", generate_sql(test_question))