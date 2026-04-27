FROM python:3.11-slim

WORKDIR /app

RUN useradd -m -u 1000 appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY noshow_iq/ ./noshow_iq/
COPY train_model.py .
COPY smoke_test.py .
COPY data/ ./data/

ENV PYTHONPATH=/app

RUN python train_model.py

USER appuser

EXPOSE 7860

CMD ["python", "-m", "noshow_iq.api"]