# Dr.web 프로젝트

의료 정보 검색 및 커뮤니티 웹 애플리케이션

---

## 🛠️ 주요 기술 스택

-   **Backend**: Python 3, Flask
-   **Frontend**: HTML5, CSS3 (Jinja2 템플릿)
-   **Database**: PostgreSQL (psycopg2)
-   **Web Crawling**: requests, BeautifulSoup4
-   **환경 변수 관리**: python-dotenv

---

## 📚 프로젝트 소개

Dr.web은 병원, 약국, 응급실, 의약품 등 다양한 의료 정보를 쉽고 빠르게 검색할 수 있는 웹 서비스입니다.  
또한, 사용자 커뮤니티(게시판, 공지사항 등)를 통해 의료 관련 정보를 자유롭게 공유할 수 있습니다.

---

## 🏗️ 프로젝트 구조

```
Dr.web/
 ├── app.py                # Flask 앱 실행 및 블루프린트 등록
 ├── db.py                 # DB 연결 및 커서 관리 함수
 ├── requirements.txt      # 의존성 패키지 목록
 ├── routes/               # 주요 기능별 라우트 모듈
 │    ├── hospital.py      # 병원 검색
 │    ├── drugstore.py     # 약국 검색
 │    ├── emergency.py     # 응급실 검색
 │    ├── board.py         # 커뮤니티(게시판, 공지)
 │    └── main.py          # 메인페이지, 뉴스 크롤링, 기타
 ├── static/               # 정적 파일(css, image 등)
 ├── templates/            # HTML 템플릿
 └── ...
```

---

## 🚀 주요 기능

-   **실시간 의료 뉴스 크롤링**

    -   네이버 뉴스에서 최신 의료 뉴스를 크롤링하여 메인페이지에 자동 노출

-   **병원/약국/응급실 정보 검색**

    -   이름, 지역, 진료과목 등 다양한 조건으로 의료기관 검색
    -   DB 연동을 통한 실시간 결과 제공

-   **의약품 정보 검색**

    -   의약품명, 종류, 모양, 부위 등으로 상세 검색

-   **커뮤니티 게시판**

    -   자유게시판(글 작성/조회/댓글), 공지사항, 답글 기능

-   **검색어 외부 검색 지원**
    -   입력한 검색어로 구글 검색 리다이렉트

---

## 🖥️ 실행 방법

### 1. 필수 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env` 파일을 생성하고 아래와 같이 입력합니다.

```env
# Database Configuration
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_NAME=your_db_name
DB_PORT=5432

# Security
SECRET_KEY=your-secret-key-here

# News URL
NEWS_URL=웹크롤링 주소
```

### 3. 데이터베이스 준비

PostgreSQL에 필요한 테이블을 생성하세요.
예시 : `hos_table`, `drugstore`, `emergency`, `medi_table`, `board`, `reply`, `community`, `gongji`

### 4. 애플리케이션 실행

```bash
python app.py 또는 flask run
```

---

## 📸 주요 화면 예시

-   메인페이지: 실시간 의료 뉴스, 주요 메뉴
-   병원/약국/응급실/의약품 검색 결과
-   커뮤니티 게시판/공지사항/댓글

---

## ⚠️ 보안 및 주의사항

-   `.env` 파일은 절대 Git에 커밋하지 마세요! (이미 .gitignore에 등록됨)
-   실제 운영 환경에서는 강력한 SECRET_KEY를 사용하세요.
-   DB 비밀번호 등 민감 정보는 안전하게 관리하세요.

---

## 🙋 문의 및 개선 제안

이슈로 남겨주시면 언제든 환영합니다!
