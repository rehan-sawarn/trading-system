from pydantic import BaseModel, Field


class Instrument(BaseModel):
    symbol: str = Field(..., description="Trading symbol")
    exchange: str = Field(..., description="Exchange name")
    instrumentType: str = Field(..., description="Type of instrument")
    lastTradedPrice: float = Field(..., gt=0, description="Last traded price")


class InstrumentResponse(BaseModel):
    instruments: list[Instrument]