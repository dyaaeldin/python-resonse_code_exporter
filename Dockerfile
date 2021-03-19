FROM python
MAINTAINER dyaa ahmed
WORKDIR /app
RUN pip install prometheus-client
COPY ./exporter.py ./
