from fastapi import APIRouter
from app.models.instrument import InstrumentResponse
from app.services.instrument_service import InstrumentService

router = APIRouter(prefix="/api/v1/instruments", tags=["Instruments"])


@router.get("", response_model=InstrumentResponse)
def get_instruments():
    """Get all tradable instruments"""
    instruments = InstrumentService.get_all_instruments()
    return InstrumentResponse(instruments=instruments)