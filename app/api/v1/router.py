from fastapi import APIRouter, Depends
from app.utils.dependencies import get_current_user

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.get("/protected")
async def protected_route(current_user = Depends(get_current_user)):
    return {"message": "This is a protected route", "user": current_user}