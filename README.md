# Reading Log API

독서 기록을 관리할 수 있는 REST API 프로젝트입니다.
사용자 인증(JWT), 독서 기록 관리, 관계형 데이터 설계를 중심으로 구현했습니다.

---

# Tech Stack

## Backend

* FastAPI
* SQLAlchemy
* Pydantic

## Database

* SQLite

## Authentication

* JWT (python-jose)
* Passlib (bcrypt)

---

# Project Structure

```bash
app/
 ├── core/             # 설정, 보안, DB 연결
 │    ├── config.py
 │    ├── database.py
 │    └── security.py
 │
 ├── models/           # SQLAlchemy 모델
 │    ├── user.py
 │    ├── book.py
 │    └── reading_log.py
 │
 ├── schemas/          # Request / Response 스키마
 │    ├── user.py
 │    ├── auth.py
 │    ├── book.py
 │    └── reading_log.py
 │
 ├── services/         # 비즈니스 로직
 │    ├── auth_service.py
 │    ├── book_service.py
 │    └── reading_log_service.py
 │
 ├── routers/          # API 라우터
 │    ├── auth.py
 │    ├── book.py
 │    └── reading_log.py
 │
 ├── dependencies/     # 공통 dependency
 │    └── auth.py
 │
 └── main.py
```

---

# Architecture

```text
Client
 ↓
Router
 ↓
Service
 ↓
Database
```

* Router → 요청/응답 처리
* Service → 비즈니스 로직 처리
* Model → 데이터베이스 구조 관리

도메인별(auth / book / reading_log)로 서비스를 분리하여 유지보수성과 확장성을 고려했습니다.

---

# Authentication

JWT 기반 인증을 구현했습니다.

## 인증 흐름

```text
회원가입
→ 로그인
→ JWT 발급
→ Authorization Header 인증
→ 보호된 API 접근
```

## 사용 기술

* bcrypt 기반 비밀번호 해싱
* JWT Access Token 발급
* OAuth2PasswordBearer 기반 인증 처리

---

# Main Features

## Auth

* 회원가입
* 로그인
* JWT 발급

## Books

* 책 생성
* 책 조회
* 책 삭제

## Reading Logs

* 독서 기록 생성
* 사용자별 독서 기록 조회
* 리뷰 수정
* 독서 기록 삭제

---

# 📡 API Example

## 회원가입

```http
POST /auth/signup
```

```json
{
  "username": "testuser",
  "password": "1234"
}
```

---

## 로그인

```http
POST /auth/login
```

```json
{
  "username": "testuser",
  "password": "1234"
}
```

---

## 독서 기록 생성

```http
POST /logs
Authorization: Bearer <token>
```

```json
{
  "book_id": 1,
  "review": "좋은 책이었다",
  "rating": 5
}
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository_url>
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv/Scripts/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run Server

```bash
uvicorn app.main:app --reload
```

---

# Learning Points

이 프로젝트를 통해 다음 내용을 학습했습니다.

* FastAPI 기반 REST API 설계
* SQLAlchemy ORM 관계 설계
* JWT 인증 및 사용자 인증 처리
* Service Layer 기반 구조 분리
* Dependency Injection 활용

---

# Future Improvements

* 외부 도서 검색 API 연동

  * 카카오 도서 검색 API
  * 네이버 도서 검색 API

* Docker 적용

* PostgreSQL 적용

* 테스트 코드 작성 (pytest)

* Refresh Token 구현

* Role 기반 권한 처리

---

# Why This Project?

단순 CRUD 구현을 넘어서
실제 서비스 구조와 인증 흐름을 고려한 백엔드 설계를 목표로 개발했습니다.

특히 Router / Service / Model 역할 분리와 JWT 인증 흐름을 직접 구현하며
실무에서 사용되는 백엔드 구조를 이해하는 데 집중했습니다.
