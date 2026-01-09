from fastapi import APIRouter
from app.models.trade import TradeResponse
from app.services.trade_service import TradeService

router = APIRouter(prefix="/api/v1/trades", tags=["Trades"])


@router.get("", response_model=TradeResponse)
def get_trades():
    """Get all executed trades"""
    trades = TradeService.get_all_trades()
    return TradeResponse(trades=trades)