# Python 3.11 to match CI and local tooling
FROM python:3.11-slim

# Environment hygiene
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    UVICORN_WORKERS=2

# System deps (optional: add build tools if needed later)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# App directory
WORKDIR /app

# Install Python deps first for better Docker layer caching
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# Copy source
COPY genai_scaffolding_pro ./genai_scaffolding_pro
COPY pyproject.toml pytest.ini README.md ./

# Expose API port
EXPOSE 8000

# Default command: run FastAPI app via uvicorn
CMD ["uvicorn", "genai_scaffolding_pro.api.server:app", "--host", "0.0.0.0", "--port", "8000"]
