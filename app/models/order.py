from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field, field_validator


class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"


class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderStatus(str, Enum):
    NEW = "NEW"
    PLACED = "PLACED"
    EXECUTED = "EXECUTED"
    CANCELLED = "CANCELLED"


class OrderRequest(BaseModel):
    symbol: str = Field(..., description="Trading symbol")
    orderType: OrderType = Field(..., description="Order type")
    side: OrderSide = Field(..., description="Buy or Sell")
    quantity: int = Field(..., gt=0, description="Order quantity")
    price: Optional[float] = Field(None, gt=0, description="Limit price (required for LIMIT orders)")

    @field_validator('price')
    @classmethod
    def validate_price(cls, v, info):
        order_type = info.data.get('orderType')
        if order_type == OrderType.LIMIT and v is None:
            raise ValueError("price is mandatory for LIMIT orders")
        return v


class Order(BaseModel):
    orderId: str
    symbol: str
    orderType: OrderType
    side: OrderSide
    quantity: int
    price: Optional[float]
    status: OrderStatus
    createdAt: datetime
    executedAt: Optional[datetime] = None
    executedPrice: Optional[float] = None