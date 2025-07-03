# Dr.web 프로젝트

의료 정보 검색 및 커뮤니티 웹 애플리케이션입니다.

## 설치 및 설정

### 1. 필요한 패키지 설치

아래 명령어로 필요한 패키지를 직접 설치하세요:

```bash
pip install flask pymysql python-dotenv requests beautifulsoup4
```

### 2. 환경 변수 설정

`.env` 파일을 생성하고 다음 정보를 입력하세요:

```env
# Database Configuration
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_NAME=your_db_name
DB_CHARSET=utf8

# Flask Configuration
FLASK_HOST=0.0.0.0
FLASK_PORT=8080
FLASK_DEBUG=True

# Security
SECRET_KEY=your-secret-key-here
```

### 3. 데이터베이스 설정

MySQL 데이터베이스를 설정하고 필요한 테이블을 생성하세요.

### 4. 애플리케이션 실행

```bash
python app.py
```

## 프로젝트 구조

```
Dr.web/
  ├── app.py                # Flask 앱 실행 및 블루프린트 등록
  ├── db.py                 # DB 연결 함수
  ├── routes/               # 기능별 라우트 모듈
  │     ├── hospital.py
  │     ├── drugstore.py
  │     ├── emergency.py
  │     ├── board.py
  │     └── main.py
  ├── static/               # 정적 파일(css, image 등)
  ├── templates/            # HTML 템플릿
  ├── config.env            # (Git에 올리지 마세요!) 환경 변수 파일
  └── ...
```

## 주요 기능

-   병원 검색
-   약품 정보 검색
-   약국 검색
-   응급실 정보
-   커뮤니티 게시판
-   공지사항

## 보안 주의사항

-   `.env` 파일은 절대 Git에 커밋하지 마세요 (이미 .gitignore에 등록되어 있음)
-   실제 운영 환경에서는 강력한 SECRET_KEY를 사용하세요
-   데이터베이스 비밀번호 등 민감 정보는 안전하게 관리하세요

---

문의사항이나 개선 요청은 언제든 이슈로 남겨주세요!
