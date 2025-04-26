FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    gfortran \
    build-essential \
    libopenblas-dev \
    liblapack-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install Flask joblib scikit-learn==1.4.2 numpy==1.26.4 pandas

EXPOSE 5000

CMD ["python", "app.py"]
