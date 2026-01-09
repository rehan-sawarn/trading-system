from fastapi import APIRouter, HTTPException, status
from app.models.order import Order, OrderRequest
from app.services.order_service import OrderService
from app.exceptions import (
    InstrumentNotFoundException,
    OrderNotFoundException,
    InsufficientHoldingsException,
    InvalidOrderException
)

router = APIRouter(prefix="/api/v1/orders", tags=["Orders"])


@router.post("", response_model=Order, status_code=status.HTTP_201_CREATED)
def place_order(order_request: OrderRequest):
    """Place a new order"""
    try:
        order = OrderService.place_order(order_request)
        return order
    except InstrumentNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except InsufficientHoldingsException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except InvalidOrderException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/{orderId}", response_model=Order)
def get_order(orderId: str):
    """Get order by ID"""
    try:
        order = OrderService.get_order(orderId)
        return order
    except OrderNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))