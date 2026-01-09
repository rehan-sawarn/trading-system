from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers.instruments import router as instruments_router
from app.routers.orders import router as orders_router
from app.routers.trades import router as trades_router
from app.routers.portfolio import router as portfolio_router
from app.exceptions import TradingException

app = FastAPI(
    title="Trading Simulation System",
    description="Backend-only trading simulation platform",
    version="1.0.0"
)

# Register routers
app.include_router(instruments_router)
app.include_router(orders_router)
app.include_router(trades_router)
app.include_router(portfolio_router)


@app.get("/", tags=["Health"])
def root():
    """Health check endpoint"""
    return {
        "status": "running",
        "message": "Trading Simulation System API",
        "version": "1.0.0"
    }


@app.exception_handler(TradingException)
async def trading_exception_handler(request, exc):
    """Global exception handler for trading exceptions"""
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )