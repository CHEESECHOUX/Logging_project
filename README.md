# Logging_project

# 🗣 Introduction

- This is repository for Building Web_Development_Project. using Python & Django with Docker & AWS
- 2022.05.23 ~ 2022.06.17
- BE : 송재관, 임수연, 최지수(PM)
<br/>

# 👩‍💻 Technologies

- Python, Django
- Docker, AWS (EC2, RDS, Lambda, SQS), RESTful API
- Git
- Slack, Notion
<br/>

# 🧑‍💻 Features

### Docker

Docker 기반, 브라우저 접속시 접속 로그 기록 및 모니터링 화면 제작 <br/>
Docker Container간의 종속관계가 표현된 Architecture를 그리며 프로젝트 진행

- Django Container 생성
  - DB 연결을 위해  Django Web Framework 사용
        
- PostgreSQL Container 생성
  - 접속 log를 남기는 DB
- 접속 log 정보
  - Client IP
  - Request time
    

### AWS

Docker 기반 서비스 환경, 아마존 AWS 환경을 이용한 데이터 수집 및 분석환경, Client log 접속 기록 및 모니터링 홈페이지 구축
  - AWS 개발자 권한 체계 구축 (IAM)
  - Lambda 및 REST API (API Gateway) 구현
  - PostgreSQL DB 사용 및 스키마 설계
  - SQS와 Lambda Function을 이용해 메시지 등록, 조회 처리
<br/>

# 🙋‍♀️ Achievement

### Docker
  - AWS EC2 Instance를 활용하여 Dockerfile 생성
  - Docker Compose를 이용해 다중 Container 관리 및 서비스 환경 구축

### AWS
  - AWS Lambda를 이용해 event 내 log 정보 요청
  - Lambda와 RDS 연결해 log 정보 저장

