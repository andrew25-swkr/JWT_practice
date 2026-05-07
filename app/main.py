from fastapi import FastAPI
from app.routers import auth, books, reading_logs
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(books.router)
app.include_router(reading_logs.router)
