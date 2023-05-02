import firebase_admin
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth, credentials
from sqlalchemy.orm import Session

from config import FIREBASE_JSON
from dependencies import database
from models.user import User

cred = credentials.Certificate(FIREBASE_JSON)
firebase_admin.initialize_app(cred)


async def authenticate(
    cred: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
    db: Session = Depends(database.get_db),
):
    """
    Authenticate a user with a Bearer token.
    This does not support the supervisor role.
    """

    if cred is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required",
        )

    try:
        decoded_token = auth.verify_id_token(cred.credentials)
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials. {err}",
        )
    user = db.query(User).filter(User.id == decoded_token["user_id"]).first()
    if not user:
        user = User(id=decoded_token["user_id"], email=decoded_token["email"])
        db.add(user)
        db.commit()
        db.refresh(user)
    return user, db
