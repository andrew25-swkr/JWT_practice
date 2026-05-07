from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.book import BookCreate, BookResponse
from app.services.book_service import create_book, get_book, get_books, delete_book

router = APIRouter(
    prefix="/books"
    tags=["Books"]
)

#책 생성
@router.post(
    "/",
    response_description=BookResponse
)
def create_new_book(
    book_data: BookCreate,
    db: Session = Depends(get_db)
):
    
    return create_book(
        db,
        book_data.title,
        book_data.author
    )

#전체 조회
@router.get(
    "/",
    response_model=list[BookResponse]
)
def read_books(
    db:Session = Depends(get_db)
):
    
    return get_books(db)
#단일 조회
@router.get(
    "/{book_id}",
    response_model=BookResponse
)
def read_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    
    book = get_book(db, book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    
    return book

#삭제
@router.delete("/{book_id}")
def remove_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    
    book = delete_book(db, book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    
    return {
        "messge": "Book deleted"
    }