from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.db.session import check_database_connection
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health_check():
    db_connected = check_database_connection()

    response = HealthResponse(
        status="ok" if db_connected else "degraded",
        database="connected" if db_connected else "disconnected",
    )

    if not db_connected:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content=response.model_dump(),
        )

    return response
