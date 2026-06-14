FROM python:3.12-slim-bullseye

WORKDIR /gateway

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./src /gateway/src

#CMD ["uvicorn", "src.gateway:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "80"]
