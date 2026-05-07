from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str | None = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: str | None

    class Config:
        from_attributes = True