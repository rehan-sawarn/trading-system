# Backend Trading Simulation System

A robust, backend-only trading simulation platform built with **FastAPI** (Python). This project demonstrates a clean, scalable Layered Architecture (Controller-Service-Repository) designed to simulate real-world trading logic.

## 🚀 Features

- **Order Management**: Place `MARKET` and `LIMIT` orders.
- **Portfolio Tracking**: Real-time updates of holdings and average buy price calculations.
- **Trade Execution**: Automatic trade creation upon order execution.
- **Instrument Master**: Pre-loaded in-memory database of equity instruments.
- **Clean Architecture**: Strict separation of concerns using Routers, Services, Models, and Storage.

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.9+
- **Validation**: Pydantic
- **Server**: Uvicorn

## 🏗️ Architecture

The project follows a modular **Layered Architecture**:

1.  **Routers (`/routers`)**: Handle HTTP requests and responses. Acts as the entry point.
2.  **Services (`/services`)**: Contains all business logic (e.g., executing orders, calculating portfolio averages).
3.  **Models (`/models`)**: Pydantic schemas for strict data validation.
4.  **Storage (`/storage`)**: In-memory data persistence (simulating a database).

## 🏃‍♂️ Getting Started

### Prerequisites

- Python 3.10 or higher

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/YOUR_USERNAME/trading-system-simulation.git
    cd trading-system-simulation
    ```

2.  **Create and Activate Virtual Environment**
    ```bash
    python -m venv venv
    
    # Windows
    .\venv\Scripts\activate
    
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Server**
    ```bash
    uvicorn app.main:app --reload
    ```

## 📚 API Documentation

Once the server is running, you can access the interactive Swagger documentation at:

👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

## 📂 Project Structure

```bash
trading-system/
├── app/
│   ├── main.py              # Application entry point
│   ├── models/              # Pydantic data models
│   ├── routers/             # API endpoints (Controllers)
│   ├── services/            # Business logic (The "Brain")
│   └── storage/             # In-memory database
├── requirements.txt         # Project dependencies
└── README.md
```

## 🔌 Key Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/v1/instruments` | List all tradable instruments |
| `POST` | `/api/v1/orders` | Place a new Buy/Sell order |
| `GET` | `/api/v1/portfolio` | View current holdings and value |
| `GET` | `/api/v1/trades` | History of executed trades |

## 🧪 Testing

To test the flow manually via Swagger or Postman:

1.  **Get Instruments**: Copy a symbol (e.g., `TCS`).
2.  **Place Order**: Send a `POST` request with:
    ```json
    {
      "symbol": "TCS",
      "orderType": "MARKET",
      "side": "BUY",
      "quantity": 10
    }
    ```
3.  **Check Portfolio**: Verify the shares appear in your portfolio.
