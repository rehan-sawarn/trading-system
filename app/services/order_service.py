from datetime import datetime
from app.models.order import Order, OrderRequest, OrderType, OrderStatus, OrderSide
from app.storage.db import orders_db, get_next_order_id
from app.services.instrument_service import InstrumentService
from app.services.trade_service import TradeService
from app.services.portfolio_service import PortfolioService
from app.exceptions import OrderNotFoundException


class OrderService:
    
    @staticmethod
    def place_order(order_request: OrderRequest) -> Order:
        """Place a new order"""
        
        # Validate instrument exists
        instrument = InstrumentService.get_instrument(order_request.symbol)
        
        # Create order
        order = Order(
            orderId=get_next_order_id(),
            symbol=order_request.symbol,
            orderType=order_request.orderType,
            side=order_request.side,
            quantity=order_request.quantity,
            price=order_request.price,
            status=OrderStatus.PLACED,
            createdAt=datetime.utcnow()
        )
        
        # Try to execute the order
        OrderService._execute_order(order, instrument.lastTradedPrice)
        
        # Store order
        orders_db[order.orderId] = order
        
        return order
    
    @staticmethod
    def get_order(order_id: str) -> Order:
        """Get order by ID"""
        order = orders_db.get(order_id)
        if not order:
            raise OrderNotFoundException(f"Order with ID '{order_id}' not found")
        return order
    
    @staticmethod
    def _execute_order(order: Order, current_price: float):
        """Execute order based on type and conditions"""
        
        can_execute = False
        executed_price = None
        
        if order.orderType == OrderType.MARKET:
            # MARKET orders always execute immediately
            can_execute = True
            executed_price = current_price
            
        elif order.orderType == OrderType.LIMIT:
            # LIMIT orders execute if price condition matches
            if order.side == OrderSide.BUY and current_price <= order.price:
                can_execute = True
                executed_price = current_price
            elif order.side == OrderSide.SELL and current_price >= order.price:
                can_execute = True
                executed_price = current_price
        
        if can_execute:
            # Update portfolio (this will raise exception if insufficient holdings for SELL)
            PortfolioService.update_holding(
                order.symbol,
                order.side,
                order.quantity,
                executed_price
            )
            
            # Create trade record
            TradeService.create_trade(
                order.orderId,
                order.symbol,
                order.side,
                order.quantity,
                executed_price
            )
            
            # Update order status
            order.status = OrderStatus.EXECUTED
            order.executedAt = datetime.utcnow()
            order.executedPrice = executed_price