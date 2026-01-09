from fastapi import APIRouter
from app.models.portfolio import PortfolioResponse
from app.services.portfolio_service import PortfolioService

router = APIRouter(prefix="/api/v1/portfolio", tags=["Portfolio"])


@router.get("", response_model=PortfolioResponse)
def get_portfolio():
    """Get current portfolio holdings"""
    holdings = PortfolioService.get_portfolio()
    return PortfolioResponse(holdings=holdings)