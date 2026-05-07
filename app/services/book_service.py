from sqlalchemy.orm import Session
from app.models.book import Book

#책 생성
def create_book(
    db: Session,
    title: str,
    author: str | None = None
):
    
    book = Book(
        title=title,
        author=author
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return


# 전체 책 조회
def get_books(db:Session):

    books = db.query(Book).all()

    return books

# 단일 책 조회
def get_book(
    db: Session,
    book_id: int
):
    book = (
        db.qurey(Book)
        .filter(Book.id == book_id)
        .frist()
    )

    return book

# 책 삭제
def delete_book(
    db: Session,
    book_id: int
):
    
    book = (
        db.qurey(Book)
        .filter(Book.id == book_id)
        .first()
    )

    if not book:
        return None
    
    db.delete(book)
    db.commit()

    return book
