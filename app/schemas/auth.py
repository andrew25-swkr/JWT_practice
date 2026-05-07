#로그인 응답 전용
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"