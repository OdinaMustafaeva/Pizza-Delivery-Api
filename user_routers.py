from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT

from database import Session, engine
from models import User
from schemas import UserModel

user_router = APIRouter(
    prefix="/user",
    tags=["users"]
)

session = Session(bind=engine)


@user_router.get("/profile")
def user_profile(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")

    current_user = Authorize.get_jwt_subject()
    user = session.query(User).filter(User.username == current_user).first()
    return UserModel(
        id=user.id,
        username=user.username,
        email=user.email,
        is_staff=user.is_staff,
        is_active=user.is_active
    )
