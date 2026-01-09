from pydantic import BaseModel, Field


class Holding(BaseModel):
    symbol: str
    quantity: int
    averagePrice: float = Field(..., gt=0)
    currentValue: float = Field(..., ge=0)


class PortfolioResponse(BaseModel):
    holdings: list[Holding]
