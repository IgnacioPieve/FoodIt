from fastapi import APIRouter, Depends

from dependencies import auth

router = APIRouter(prefix="/user", tags=["User"])


@router.get("", status_code=200, include_in_schema=False)
@router.get("/", status_code=200, summary="Get user data")
async def get_user(authentication=Depends(auth.authenticate)):
    """
    Get user data
    """
    user, _ = authentication
    return user
