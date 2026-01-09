from datetime import datetime
from app.models.trade import Trade
from app.models.order import OrderSide
from app.storage.db import trades_db, get_next_trade_id


class TradeService:
    
    @staticmethod
    def create_trade(order_id: str, symbol: str, side: OrderSide, quantity: int, price: float) -> Trade:
        """Create a new trade record"""
        trade = Trade(
            tradeId=get_next_trade_id(),
            orderId=order_id,
            symbol=symbol,
            side=side,
            quantity=quantity,
            price=price,
            executedAt=datetime.utcnow()
        )
        trades_db.append(trade)
        return trade
    
    @staticmethod
    def get_all_trades() -> list[Trade]:
        """Get all executed trades"""
        return trades_db.copy()