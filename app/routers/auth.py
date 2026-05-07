from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.schemas.auth import Token
from app.services.auth_service import create_user, authenticate_user, login_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/signup", response_model=UserResponse)

def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        user = create_user(
            db,
            user_data.username,
            user_data.password
        )

        return user
    
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.post(
    "/login",
    response_model=Token
)
def login(user_data: UserLogin,db: Session = Depends(get_db)):
    user = authenticate_user(
        db, 
        user_data.username,
        user_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    
    token = login_user(user)

    return {
        "access_token": token,
        "token_type": "bearer"
    }