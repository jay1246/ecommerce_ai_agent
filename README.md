# 🚀 E-commerce Analytics AI Agent

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

**An intelligent API that transforms business questions into SQL queries and visual insights**  
*Powered by Google Gemini AI with automatic data visualization*

![API Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW0yY2VjZGZ4dG5jZ2V1Y2R6Z2Z6Z2JjY2Z1Z2Z1Z2Z1Z2Z1Z2Z1Z2Z1Z2Z1Zw/giphy.gif)

## ✨ Features
- **Natural Language Processing**: Ask questions like "Show top products by revenue"
- **Auto-Generated SQL**: Transparent query generation
- **Interactive Visualizations**: Built-in Plotly charts
- **Local Development**: SQLite + Excel support
- **Rate Limited**: Protects API quotas

## 🛠️ Tech Stack
| Component       | Technology |
|-----------------|------------|
| Backend         | FastAPI    |
| AI Engine       | Gemini API |
| Database        | SQLite     |
| Visualization   | Plotly     |
| Auth            | API Key    |

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

```bash
# Clone and setup
git clone https://github.com/yourusername/ecommerce-ai-agent.git
cd ecommerce-ai-agent

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API key

# Initialize database
python src/database.py

# Launch server
python -m uvicorn src.main:app --reload
**📚 API Usage
Endpoints
Method	Endpoint	Description
POST	/ask	Submit business query
Example Request:
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"question":"What's our monthly sales trend?"}'
Sample Response:
{
  "question": "What's our monthly sales trend?",
  "sql_query": "SELECT strftime('%Y-%m', date) AS month, SUM(amount) FROM sales GROUP BY month",
  "data": [
    {"month": "2023-01", "SUM(amount)": 15000},
    {"month": "2023-02", "SUM(amount)": 18000}
  ],
  "visualization": "<div id='plotly-chart'>...</div>"
}[deepseek_text_20250723_ad9952.txt](https://github.com/user-attachments/files/21393484/deepseek_text_20250723_ad9952.txt)

🌐 Deployment
Option A: Docker
dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]
Option B: Render
Connect GitHub repo

Set environment variables

Deploy!

🤝 Contributing
Fork the repo

Create feature branch (git checkout -b feat/awesome-feature)

Commit changes (git commit -m 'feat: Add awesome feature')

Push to branch (git push origin feat/awesome-feature)

Open PR

📄 License
MIT © 2023 [Your Name] - See LICENSE for details.
**


