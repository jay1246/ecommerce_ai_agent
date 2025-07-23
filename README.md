# 🛍️ E-commerce Analytics AI Agent

**Transform business questions into actionable SQL insights with AI**  
*A FastAPI service that converts natural language queries about e-commerce data into SQL, executes them, and returns visualized results.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## ✨ Features
- **Natural Language Processing**: Ask questions like "What's our top-selling product?"
- **Auto-Generated SQL**: See the exact query executed
- **Visual Analytics**: Automatic Plotly charts for numeric results
- **Local Development**: SQLite database support
- **Rate Limited**: Built-in protection against API quota limits

## 🚀 Quick Start
```bash
**# 1. Clone and setup
git clone https://github.com/yourusername/ecommerce-ai-agent.git
cd ecommerce-ai-agent

# 2. Configure environment (Linux/Mac)
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gemini API key
echo "GEMINI_API_KEY=your_key_here" > .env

# 5. Initialize sample database
python src/database.py

# 6. Start the server
python -m uvicorn src.main:app --reload**
