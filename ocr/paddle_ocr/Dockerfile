# # 베이스 이미지로 Python 3.10을 사용
# FROM python:3.10-slim

# # 필수 패키지 설치
# RUN apt-get update && apt-get install -y \
#     vim \
#     net-tools \
#     iputils-ping \
#     libglib2.0-0 \
#     libsm6 \
#     libxrender1 \
#     libxext6 \
#     libgomp1 \
#     libgl1-mesa-glx \
#     && rm -rf /var/lib/apt/lists/*

# # 작업 디렉토리 설정
# WORKDIR /workspace

# # 패키지 종속성 파일 복사
# COPY requirements.txt requirements.txt

# # 패키지 설치
# RUN pip install --no-cache-dir -r requirements.txt
# RUN python3 -m pip install --upgrade pip
# RUN python3 -m pip install jupyter

# # 애플리케이션 코드 복사
# COPY . /workspace

# # 엔트리포인트 설정
# CMD ["python", "app.py"]

# ------------------------------------------------------------------------------------------

# FROM ubuntu:22.04

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     patch \
#     python3 \
#     python3-pip \
#     vim \
#     net-tools \
#     iputils-ping \
#     libglib2.0-0 \
#     libsm6 \
#     libxrender1 \
#     libxext6 \
#     libgomp1 \
#     libgl1-mesa-glx \
#     python3-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements.txt and install Python packages
# COPY requirements.txt requirements.txt
# RUN python3 -m pip install --upgrade pip
# RUN python3 -m pip install -r requirements.txt
# RUN python3 -m pip install jupyter

# RUN python3 --version

# # Set the working directory
# WORKDIR /workspace
# COPY . /workspace

# EXPOSE 8888

# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]




FROM ubuntu:22.04

# Install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3 \
    python3-pip \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgomp1 \
    libgl1-mesa-glx \
    python3-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install PaddleOCR and other Python packages
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install paddlepaddle paddleocr jupyter

# Create directories for models
RUN mkdir -p /root/.paddleocr/whl/det/ml/Multilingual_PP-OCRv3_det_infer \
    && mkdir -p /root/.paddleocr/whl/rec/korean/korean_PP-OCRv4_rec_infer

# Download models
RUN wget -O /root/.paddleocr/whl/det/ml/Multilingual_PP-OCRv3_det_infer/Multilingual_PP-OCRv3_det_infer.tar \
    https://paddleocr.bj.bcebos.com/PP-OCRv3/multilingual/Multilingual_PP-OCRv3_det_infer.tar \
    && tar -xvf /root/.paddleocr/whl/det/ml/Multilingual_PP-OCRv3_det_infer/Multilingual_PP-OCRv3_det_infer.tar -C /root/.paddleocr/whl/det/ml/Multilingual_PP-OCRv3_det_infer

RUN wget -O /root/.paddleocr/whl/rec/korean/korean_PP-OCRv4_rec_infer/korean_PP-OCRv4_rec_infer.tar \
    https://paddleocr.bj.bcebos.com/PP-OCRv4/multilingual/korean_PP-OCRv4_rec_infer.tar \
    && tar -xvf /root/.paddleocr/whl/rec/korean/korean_PP-OCRv4_rec_infer/korean_PP-OCRv4_rec_infer.tar -C /root/.paddleocr/whl/rec/korean/korean_PP-OCRv4_rec_infer

# Set the working directory
WORKDIR /workspace
COPY . /workspace

# Expose port
EXPOSE 8888

# Command to run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''"]
