#user_id 없음 JWT로 가져올 것임 create / response 분리
from pydantic import BaseModel

class ReadingLogCreate(BaseModel):
    book_id: int
    review: str | None = None
    rating: int | None = None

    class Config:
        from_attributes = True