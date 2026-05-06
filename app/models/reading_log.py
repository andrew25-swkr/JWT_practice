from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class ReadingLog(Base):
    __tablename__ = "reading_logs"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    review = Column(String)
    rating = Column(Integer)

    user = relationship("User")
    book = relationship("Book")