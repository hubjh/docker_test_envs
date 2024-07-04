# 베이스 이미지로 Node.js를 사용
FROM node:14

# 작업 디렉토리를 /app으로 설정
WORKDIR /app

# # 필요한 파일들을 컨테이너에 복사
# COPY package.json /app
# COPY package-lock.json /app

# 의존성 설치
RUN npm install

# 애플리케이션 포트 설정
EXPOSE 3000

# 컨테이너가 시작될 때 실행할 명령
CMD ["npm", "start"]
