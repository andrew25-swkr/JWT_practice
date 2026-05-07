from sqlalchemy.orm import Session
from app.models.reading_log import ReadingLog


# 독서 기록 생성
def create_log(
    db: Session,
    user_id: int,
    book_id: int,
    review: str | None = None,
    rating: int | None = None
):
    
    log = ReadingLog(
        user_id=user_id,
        book_id=book_id,
        review=review,
        rating=rating
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log

# 사용자 독서 기록 조회
def get_user_logs(
    db:Session,
    user_id: int
):
    logs = (
        db.query(ReadingLog)
        .filter(ReadingLog.user_id == user_id)
        .all()
    )

    return logs

# 리뷰 수정
def update_review(
    db: Session,
    log_id: int,
    review: str,
    rating: int
):
    
    log = (
        db.query(ReadingLog)
        .filter(ReadingLog.id == log_id)
        .frist()
    )

    if not log:
        return None
    log.review = review
    log.rating = rating

    db.commit()
    db.refresh(log)

    return log

# 독서 기록 삭제
def delete_log(
    db: Session,
    log_id: int
):
    log = (
        db.query(ReadingLog)
        .filter(ReadingLog.id == log_id)
        .first
    )

    if not log:
        return None
    
    db.delete(log)
    db.commit()

    return log