from datetime import datetime
from pydantic import BaseModel, Field
from app.models.order import OrderSide


class Trade(BaseModel):
    tradeId: str
    orderId: str
    symbol: str
    side: OrderSide
    quantity: int = Field(..., gt=0)
    price: float = Field(..., gt=0)
    executedAt: datetime


class TradeResponse(BaseModel):
    trades: list[Trade]