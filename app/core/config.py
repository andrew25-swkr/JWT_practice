#환경 변수
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKNE_EXPIRE_MINUTES: int = 60

settings = Settings()