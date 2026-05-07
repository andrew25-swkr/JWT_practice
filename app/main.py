from fastapi import FastAPI
from app.routers import auth, book, reading_log
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(book.router)
app.include_router(reading_log.router)
