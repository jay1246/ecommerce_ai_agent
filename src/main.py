from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
import sqlite3
import pandas as pd
import plotly.express as px
from src.services.query_generator import generate_sql  # NEW (correct)

app = FastAPI()

@app.post("/ask")
async def ask_question(question: str = Body(..., embed=True)):
    try:
        # Generate and execute SQL
        sql = generate_sql(question)
        conn = sqlite3.connect('ecommerce.db')
        df = pd.read_sql(sql, conn)
        conn.close()
        
        # Determine if visualization would help
        visualization = None
        if len(df.columns) == 2 and len(df) > 3:  # Good candidate for chart
            x_col, y_col = df.columns[0], df.columns[1]
            if df[y_col].dtype in ['float64', 'int64']:
                fig = px.bar(df, x=x_col, y=y_col, title=question)
                visualization = fig.to_html()
        
        return {
            "question": question,
            "sql_query": sql,
            "data": df.to_dict(orient='records'),
            "visualization": visualization
        }
        
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

@app.get("/", response_class=HTMLResponse)
async def docs():
    return """
    <h1>E-commerce Analytics API</h1>
    <p>POST /ask with JSON: {"question": "Your question"}</p>
    """