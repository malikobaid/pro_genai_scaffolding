FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1     PIP_NO_CACHE_DIR=1     UVICORN_WORKERS=2

RUN apt-get update && apt-get install -y --no-install-recommends     build-essential curl ca-certificates  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY genai_scaffolding_pro ./genai_scaffolding_pro
COPY pyproject.toml pytest.ini README.md ./.

EXPOSE 8000

CMD ["uvicorn", "genai_scaffolding_pro.api.server:app", "--host", "0.0.0.0", "--port", "8000"]
