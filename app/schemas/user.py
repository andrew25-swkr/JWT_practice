from pydantic import BaseModel

#클라이언트 > 서버 요청 데이터
class UserCreate(BaseModel):
    username: str
    password: str

#회원가입과 같아보이지만 의미가 다르기에 분리
class UserLogin(BaseModel):
    username: str
    password: str

#password 포함 안 함, orm 객체 > 자동 변환
class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True # (구 orm_mode)
