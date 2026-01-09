from app.models.portfolio import Holding
from app.models.order import OrderSide
from app.storage.db import portfolio_db, instruments_db
from app.exceptions import InsufficientHoldingsException


class PortfolioService:
    
    @staticmethod
    def get_portfolio() -> list[Holding]:
        """Get all portfolio holdings with current values"""
        holdings = []
        for symbol, holding in portfolio_db.items():
            instrument = instruments_db.get(symbol)
            current_price = instrument.lastTradedPrice if instrument else holding.averagePrice
            
            holdings.append(Holding(
                symbol=holding.symbol,
                quantity=holding.quantity,
                averagePrice=holding.averagePrice,
                currentValue=holding.quantity * current_price
            ))
        return holdings
    
    @staticmethod
    def get_holding(symbol: str) -> Holding | None:
        """Get holding for a specific symbol"""
        return portfolio_db.get(symbol)
    
    @staticmethod
    def update_holding(symbol: str, side: OrderSide, quantity: int, executed_price: float):
        """Update portfolio after order execution"""
        
        if side == OrderSide.BUY:
            PortfolioService._handle_buy(symbol, quantity, executed_price)
        else:
            PortfolioService._handle_sell(symbol, quantity)
    
    @staticmethod
    def _handle_buy(symbol: str, quantity: int, executed_price: float):
        """Handle BUY order - increase holdings"""
        existing = portfolio_db.get(symbol)
        
        if existing:
            # Calculate new average price
            total_cost = (existing.quantity * existing.averagePrice) + (quantity * executed_price)
            new_quantity = existing.quantity + quantity
            new_avg_price = total_cost / new_quantity
            
            portfolio_db[symbol] = Holding(
                symbol=symbol,
                quantity=new_quantity,
                averagePrice=new_avg_price,
                currentValue=0  # Will be calculated in get_portfolio
            )
        else:
            # Create new holding
            portfolio_db[symbol] = Holding(
                symbol=symbol,
                quantity=quantity,
                averagePrice=executed_price,
                currentValue=0
            )
    
    @staticmethod
    def _handle_sell(symbol: str, quantity: int):
        """Handle SELL order - decrease holdings"""
        existing = portfolio_db.get(symbol)
        
        # Validate sufficient holdings
        if not existing or existing.quantity < quantity:
            available = existing.quantity if existing else 0
            raise InsufficientHoldingsException(
                f"Insufficient holdings for {symbol}. Available: {available}, Requested: {quantity}"
            )
        
        new_quantity = existing.quantity - quantity
        
        if new_quantity == 0:
            # Remove holding if quantity becomes zero
            del portfolio_db[symbol]
        else:
            # Update quantity, keep same average price
            portfolio_db[symbol] = Holding(
                symbol=symbol,
                quantity=new_quantity,
                averagePrice=existing.averagePrice,
                currentValue=0
            )