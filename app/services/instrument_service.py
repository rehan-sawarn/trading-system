from app.models.instrument import Instrument
from app.storage.db import instruments_db
from app.exceptions import InstrumentNotFoundException


class InstrumentService:
    
    @staticmethod
    def get_all_instruments() -> list[Instrument]:
        """Get all available instruments"""
        return list(instruments_db.values())
    
    @staticmethod
    def get_instrument(symbol: str) -> Instrument:
        """Get instrument by symbol"""
        instrument = instruments_db.get(symbol)
        if not instrument:
            raise InstrumentNotFoundException(f"Instrument with symbol '{symbol}' not found")
        return instrument