from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.reading_log import ReadingLogCreate, ReadingLogResponse
from app.services.reading_log_service import create_log, get_user_logs, update_review, delete_log

router = APIRouter(
    prefix="/logs",
    tags=["Reading Logs"]
)

#기록 생성
@router.post(
    "/",
    response_model=ReadingLogResponse
)
def create_reading_log(
    log_data: ReadingLogCreate,
    db: Session = Depends(get_db)
):
    
    #JWT 붙이면 current_user.id 사용 예정
    user_id = 1

    return create_log(
        db,
        user_id=user_id,
        book_id=log_data.book_id,
        review=log_data.review,
        rating=log_data.rating
    )

#사용자 기록 조회
@router.get(
    "/",
    response_model=list[ReadingLogResponse]
)
def read_my_log(
    db: Session = Depends(get_db)
):
    
    user_id = 1

    return get_user_logs(db, user_id)