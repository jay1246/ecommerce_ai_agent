import pandas as pd
from sqlalchemy import create_engine

def excel_to_sql():
    # Read Excel files
    eligibility = pd.read_excel("E:/ecommerce_ai_agent/data/Product-Level Eligibility Table (mapped).xlsx")
    ad_metrics = pd.read_excel("E:/ecommerce_ai_agent/data/Product-Level Ad Sales and Metrics (mapped).xlsx")
    total_sales = pd.read_excel("E:/ecommerce_ai_agent/data/Product-Level Total Sales and Metrics (mapped).xlsx")

    
    # Create SQLite database
    engine = create_engine('sqlite:///../ecommerce.db')
    
    # Export to SQL
    eligibility.to_sql('eligibility', engine, if_exists='replace', index=False)
    ad_metrics.to_sql('ad_metrics', engine, if_exists='replace', index=False)
    total_sales.to_sql('total_sales', engine, if_exists='replace', index=False)
    
    print("Database created successfully!")

if __name__ == "__main__":
    excel_to_sql()