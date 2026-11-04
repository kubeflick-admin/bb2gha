# Multi-stage-ish slim image. Interview point: small images = faster pulls,
# smaller attack surface, fewer CVEs for Trivy to flag.
FROM python:3.12-slim

# Don't run as root (security hardening - asked about in DevSecOps interviews)
RUN useradd --create-home appuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
USER appuser

EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app.main:app"]
