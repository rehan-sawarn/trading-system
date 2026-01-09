from app.models.instrument import Instrument
from app.models.order import Order
from app.models.trade import Trade
from app.models.portfolio import Holding

# In-memory storage
instruments_db: dict[str, Instrument] = {}
orders_db: dict[str, Order] = {}
trades_db: list[Trade] = []
portfolio_db: dict[str, Holding] = {}

# Order counter for generating unique IDs
order_counter = 1
trade_counter = 1


def initialize_instruments():
    """Initialize with sample instruments"""
    sample_instruments = [
        Instrument(
            symbol="RELIANCE",
            exchange="NSE",
            instrumentType="EQUITY",
            lastTradedPrice=2450.50
        ),
        Instrument(
            symbol="TCS",
            exchange="NSE",
            instrumentType="EQUITY",
            lastTradedPrice=3890.75
        ),
        Instrument(
            symbol="INFY",
            exchange="NSE",
            instrumentType="EQUITY",
            lastTradedPrice=1523.30
        ),
        Instrument(
            symbol="HDFCBANK",
            exchange="NSE",
            instrumentType="EQUITY",
            lastTradedPrice=1645.20
        ),
        Instrument(
            symbol="ICICIBANK",
            exchange="NSE",
            instrumentType="EQUITY",
            lastTradedPrice=1089.60
        ),
    ]
    
    for instrument in sample_instruments:
        instruments_db[instrument.symbol] = instrument


def get_next_order_id() -> str:
    global order_counter
    order_id = f"ORD_{order_counter:06d}"
    order_counter += 1
    return order_id


def get_next_trade_id() -> str:
    global trade_counter
    trade_id = f"TRD_{trade_counter:06d}"
    trade_counter += 1
    return trade_id


# Initialize instruments on module load
initialize_instruments()