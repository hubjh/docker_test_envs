FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    vim \
    net-tools \
    iputils-ping \
    tesseract-ocr \
    tesseract-ocr-kor \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python packages
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install jupyter

RUN python3 --version

# Tesseract 버전 확인
RUN tesseract --version


# Set the working directory
WORKDIR /workspace
COPY . /workspace

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]