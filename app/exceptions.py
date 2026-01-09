class TradingException(Exception):
    """Base exception for trading system"""
    pass


class InstrumentNotFoundException(TradingException):
    """Raised when instrument symbol is not found"""
    pass


class OrderNotFoundException(TradingException):
    """Raised when order ID is not found"""
    pass


class InsufficientHoldingsException(TradingException):
    """Raised when trying to sell more than available holdings"""
    pass


class InvalidOrderException(TradingException):
    """Raised for invalid order parameters"""
    pass