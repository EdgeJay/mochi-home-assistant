from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["system"])
def health_check():
    """
    Health check endpoint.

    Returns:
        dict: Status message.
    """
    return {"status": "ok"}
