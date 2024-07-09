# FROM ubuntu:22.04

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     python3 \
#     python3-pip \
#     vim \
#     net-tools \
#     iputils-ping \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements.txt and install Python packages
# COPY requirements.txt requirements.txt
# RUN python3 -m pip install --upgrade pip
# RUN python3 -m pip install -r requirements.txt
# # RUN python3 -m pip install jupyter

# RUN python3 --version

# # Set the working directory
# WORKDIR /app
# COPY . /app


# EXPOSE 8000

# # FastAPI 서버 실행
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

FROM ubuntu:22.04

# 기본 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3 \
    python3-pip \
    vim \
    net-tools \
    iputils-ping \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgomp1 \
    libgl1-mesa-glx \
    python3-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치
RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

# 모델 디렉토리 생성 및 모델 다운로드
RUN mkdir -p /root/.paddleocr/whl/det/ml/Multilingual_PP-OCRv3_det_infer \
    && mkdir -p /root/.paddleocr/whl/rec/korean/korean_PP-OCRv4_rec_infer

RUN wget -O /root/.paddleocr/whl/det/ml/Multilingual_PP-OCRv3_det_infer/Multilingual_PP-OCRv3_det_infer.tar \
    https://paddleocr.bj.bcebos.com/PP-OCRv3/multilingual/Multilingual_PP-OCRv3_det_infer.tar \
    && tar -xvf /root/.paddleocr/whl/det/ml/Multilingual_PP-OCRv3_det_infer/Multilingual_PP-OCRv3_det_infer.tar -C /root/.paddleocr/whl/det/ml/Multilingual_PP-OCRv3_det_infer

RUN wget -O /root/.paddleocr/whl/rec/korean/korean_PP-OCRv4_rec_infer/korean_PP-OCRv4_rec_infer.tar \
    https://paddleocr.bj.bcebos.com/PP-OCRv4/multilingual/korean_PP-OCRv4_rec_infer.tar \
    && tar -xvf /root/.paddleocr/whl/rec/korean/korean_PP-OCRv4_rec_infer/korean_PP-OCRv4_rec_infer.tar -C /root/.paddleocr/whl/rec/korean/korean_PP-OCRv4_rec_infer

# 작업 디렉토리 설정
WORKDIR /app
COPY . /app

# 포트 노출
EXPOSE 8000

# FastAPI 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

