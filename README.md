# Market Stats AI 📈

Market Stats AI is a powerful financial analysis tool leveraging Google's Gemini AI to provide real-time market data, stock valuations, and trade probability tracking. It combines modern AI grounding with a robust backend to help traders and investors make data-driven decisions.

## 🚀 Features

- **AI-Powered Stock Valuation**: Leverages Gemini AI with Google Search grounding to fetch and analyze key financial metrics:
  - P/E Ratio (Price-to-Earnings)
  - PEG Ratio (Price/Earnings to Growth)
  - ROE (Return on Equity)
  - D/E Ratio (Debt-to-Equity)
  - EPS Growth
- **Real-time Market Data Tracking**: Automatically calculates YTD performance based on daily candle colors (Green vs. Red).
- **Probability Management**: Store and track trade probabilities for specific stock symbols.
- **User Management**: Simple and secure user registration and management system.
- **FastAPI Backend**: High-performance API built with FastAPI for seamless integration.
- **SQLite Database**: Lightweight and reliable local data storage.

## 🛠 Tech Stack

- **Backend**: Python 3.x, FastAPI, Uvicorn
- **AI Engine**: Google Gemini API (`gemini-2.0-flash`) with Search Grounding
- **Database**: SQLite3
- **Dev Tools**: Pydantic, Dotenv

## 📋 API Endpoints

### 🔍 Market & Evaluation
- `GET /evaluate/{symbol}`: Get an AI-powered valuation and analysis for a stock ticker.
- `POST /message`: Process a message to fetch real-time market data (YTD candle statistics).

### 👥 User Management
- `POST /user_create`: Create a new user profile.
- `GET /user/{user_id}`: Retrieve user details.
- `PUT /user/{user_id}`: Update user information.
- `DELETE /user/{user_id}`: Remove a user profile.
- `GET /users`: List all registered users.

### 🎲 Probability Tracking
- `POST /probability_create`: Record a new trade probability.
- `GET /probability/{probability_id}`: Fetch details for a specific probability record.
- `GET /probabilities/{user_id}`: List all probabilities for a specific user.
- `GET /probabilities?stock_symbol={symbol}`: List all probabilities for a specific ticker.
- `PUT /probability/{probability_id}`: Update a probability record.
- `DELETE /probability/{probability_id}`: Delete a probability record.

### ⚙️ System
- `GET /health`: System health check.

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/market-stats.git
   cd market-stats
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root directory and add your Google Gemini API key:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

5. **Initialize the Database**:
   The database will be automatically initialized when you start the server for the first time.

6. **Run the Server**:
   ```bash
   python src/server/main.py
   ```
   The API will be available at `http://localhost:8000`. You can access the interactive documentation at `http://localhost:8000/docs`.

## 📂 Project Structure

```text
market-stats/
├── src/
│   └── server/
│       ├── api/            # API Routes and Business Logic
│       ├── core/           # Configuration and Utilities
│       ├── db_manager/     # Database operations and Schema
│       ├── models/         # Pydantic models for request/response
│       └── main.py         # Application Entry Point
├── README.md
└── requirements.txt
```

## ⚖️ License

This project is licensed under the MIT License - see the LICENSE file for details.