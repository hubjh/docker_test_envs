# 베이스 이미지를 Ubuntu 22.04로 설정
FROM ubuntu:22.04

# 시스템 패키지 업데이트 및 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk-headless \
    python3 \
    python3-dev \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Apache Spark 설치
ENV SPARK_VERSION=3.2.1
RUN curl -o spark.tgz https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.2.tgz \
    && tar -xzf spark.tgz -C /opt/ \
    && mv /opt/spark-$SPARK_VERSION-bin-hadoop3.2 /opt/spark \
    && rm spark.tgz

# 환경 변수 설정
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# 필요한 Python 패키지 설치
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Jupyter Notebook 설치
RUN pip3 install notebook

# 작업 디렉토리 설정
WORKDIR /workspace

# Jupyter Notebook 실행
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]

# # 베이스 이미지를 Ubuntu 22.04로 설정
# FROM ubuntu:22.04

# # 시스템 패키지 업데이트 및 필요한 패키지 설치
# RUN apt-get update && apt-get install -y \
#     python3 \
#     python3-dev \
#     python3-pip \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # 필요한 Python 패키지 설치
# COPY requirements.txt /tmp/requirements.txt
# RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# # Jupyter Notebook 설치
# RUN pip3 install notebook

# # 작업 디렉토리 설정
# WORKDIR /workspace

# # Jupyter Notebook 실행
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]