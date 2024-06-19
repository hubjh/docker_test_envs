FROM jupyter/pyspark-notebook:python-3.10.11

USER root

RUN apt-get update && apt-get install -y poppler-utils

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

USER jovyan
