# My-Little-Forest-2024Hackathon
My-Little-Forest

# 설치 및 실행 방법
1. 레포지토리 클론
clone https://github.com/ryuryuryuk/My-Little-Forest-2024Hackathon.git

2. mylittleforest_server 폴더로 이동
cd mylittleforest_server

3. python 가상환경 설치
python - venv venv

4. 가상환경 활성화
(Window 버전) venv\Scripts\active 
(MacOS 버전) source venv\bin\activate

3. 의존성 설치
pip install -r requirements.txt

4. 데이터베이스 초기화
python manage.py migrate

5. 개발 서버 실행
python manage.py runserver 127.0.0.1:8080

6. 브라우저에 접속
http://localhost:8080/start
