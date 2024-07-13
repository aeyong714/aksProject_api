# Flask API Server
> 이 레포지토리는 Flask로 구현된 간단한 CRUD 기능을 제공하는 API 서버를 구현했습니다.

## 설정 방법
1. 필요한 패키지 설치
    ```sh
    pip3 install -r requirements.txt
    ```

2. Flask 애플리케이션 실행
    ```sh
    python3 app.py
    ```

<br>

## API 엔드포인트
- `GET /health`: API 서버의 상태 확인
- `POST /records`: 새로운 레코드 생성
- `GET /records`: 레코드 목록 조회
- `GET /records/<id>`: 특정 레코드 조회
- `PUT /records/<id>`: 특정 레코드 수정
- `DELETE /records/<id>`: 특정 레코드 삭제

<br>

## 데이터베이스 설정
- MySQL
- SQLAlchemy