from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import (hash_password, verify_password, create_access_token)

#회원가입
def create_user(db: Session, username: str, password: str):
    # username 중복 확인
    existing_user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if existing_user:
        raise ValueError("Username already exists")
    
    # 비밀번호 해싱
    hashed_pw = hash_password(password)

    #유저 생성
    user = User(
        username=username,
        password=hashed_pw
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

# 로그인 검증 
def authenticate_user(
    db: Session,
    username: str,
    password: str
):
    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if not user:
        return None
    
    # 비밀번호 비교
    if not verify_password(password, user.password):
        return None
    
    return user

#JWT 발급
def login_user(user: User):

    token = create_access_token({
        "sub": str(user.id)
    })

    return token