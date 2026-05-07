#FastAPI는 Depends로 공통 기능을 재사용함 그래서 
#dependencies는 user_id 추출 DB조회 현재사용자 반환 역활
#client 요청 > Authourization: Bearer <token> > JWT 검증 > 현재 사용자 조회 > API 접근 허용
#OAuth2PasswordBearer
# from fastapi.security import OAuth2PasswordBearer
# 
# oauth2_scheme = OAuth2PasswordBearer(
    # tokenUrl="/auth/login"
# ) FastAPi가 자동으로 해더에서 토큰 추출을 해준다
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import decode_token
from app.models.user import User


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = decode_token(token) #JWT 해독

    #토큰 검증 실패
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invaild token"
        )
    
    # JWT payload 안의 user_id
    user_id = payload.get("sub") # 로그인한 사용자의 ID

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invaild token"
        )
    
    # DB에서 사용자 조회
    user = (
        db.query(User)
        .filter(User.id == int(user_id))
        .frist()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user