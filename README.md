# Logging_project (with Docker, AWS)

# ๐ฃ Introduction

- This is repository for Building Web_Development_Project. using Python & Django with Docker & AWS
- 2022.05.23 ~ 2022.06.17
- BE : ์ก์ฌ๊ด, ์์์ฐ, ์ต์ง์(PM)
<br/>

# ๐ฉโ๐ป Technologies

- Python, Django
- Docker, AWS (EC2, RDS, Lambda, SQS), RESTful API
- Git
- Slack, Notion
<br/>

# ๐งโ๐ป Features

## Docker

Docker ๊ธฐ๋ฐ, ๋ธ๋ผ์ฐ์  ์ ์์ ์ ์ ๋ก๊ทธ ๊ธฐ๋ก ๋ฐ ๋ชจ๋ํฐ๋ง <br/>
Docker Container๊ฐ์ ์ข์๊ด๊ณ๊ฐ ํํ๋ Architecture๋ฅผ ๊ทธ๋ฆฌ๋ฉฐ ํ๋ก์ ํธ ์งํ

![dockerproject](https://user-images.githubusercontent.com/95554757/173224541-5cc23f89-e1d7-4114-a885-a10e0d995c73.PNG)

- Django Container ์์ฑ
  - DB ์ฐ๊ฒฐ์ ์ํด  Django Web Framework ์ฌ์ฉ

- PostgreSQL Container ์์ฑ
  - ์ ์ log๋ฅผ ๋จ๊ธฐ๋ DB

- ์ ์ log ์ ๋ณด
  - Client IP
  - Request time
    
<br/>

## AWS

์๋ง์กด AWS ํ๊ฒฝ์ ์ด์ฉํ ๋ฐ์ดํฐ ์์ง ๋ฐ ๋ถ์ํ๊ฒฝ, Client log ์ ์ ๊ธฐ๋ก ๋ฐ ๋ชจ๋ํฐ๋ง
<img width=100% alt="KakaoTalk_Photo_2022-06-15-18-04-26" src="https://user-images.githubusercontent.com/48621061/173789161-910061c1-340e-4326-87be-fc26a0316f9d.png">

  - AWS ๊ฐ๋ฐ์ ๊ถํ ์ฒด๊ณ ๊ตฌ์ถ (IAM)
  - Lambda ๋ฐ REST API (API Gateway) ๊ตฌํ
  - PostgreSQL DB ์ฌ์ฉ ๋ฐ ์คํค๋ง ์ค๊ณ
  - SQS์ Lambda Function์ ํ์ฉํด ๋์ฉ๋ ๋ฉ์์ง ๋ฑ๋ก, ์กฐํ ์ฒ๋ฆฌ (Batch Insert)
 
<br/>

# ๐โโ๏ธ Achievement

### Docker
  - AWS EC2 Instance๋ฅผ ํ์ฉํ์ฌ Dockerfile ์์ฑ
  - Docker Compose๋ฅผ ์ด์ฉํด ๋ค์ค Container ๊ด๋ฆฌ ๋ฐ ์๋น์ค ํ๊ฒฝ ๊ตฌ์ถ

### AWS
  - AWS Lambda๋ฅผ ์ด์ฉํด event๋ด log ์ ๋ณด ์์ฒญ์ Queue ๋๊ธฐ์ด๋ก ์ ์ก
  - Queue ๋๊ธฐ์ด์ ์๋ ๋ฉ์์ง ๋ชฉ๋ก์ ์กฐํํ์ฌ ๋์ฉ๋ ๋ฉ์์ง๋ฅผ Lambda์์ ์ฒ๋ฆฌํ  ์ ์๋๋ก ์คํ
  - Lambda์ RDS๋ฅผ ์ฐ๊ฒฐํด log ์ ๋ณด ์ ์ฅ
 
