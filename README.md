
# NoShowIQ

A prediction API for medical appointment no-shows.

## Live API Endpoints

- `GET /health` — Health check
- `POST /predict` — Predict no-show risk
- `GET /history` — Last 20 predictions
- `GET /stats` — Aggregated stats

## CI Badge
![CI/CD](https://github.com/sunilakiran/noshow-iq--62671-/actions/workflows/ci-cd.yml/badge.svg)

# NoShowIQ 🏥

A production-grade ML API that predicts whether a patient will miss their clinic appointment.

## Live URL
🚀 [https://sunilakiran-noshow-iq.hf.space](https://sunilakiran-noshow-iq.hf.space)

## CI Status
![CI](https://github.com/sunilakiran/noshow-iq-62671/actions/workflows/ci-cd.yml/badge.svg)

## Setup

```bash
pip install -r requirements.txt
```

## Run API

```bash
python -m noshow_iq.api
```

## Endpoints

- `GET /health` — API status
- `POST /predict` — Predict no-show risk
- `GET /history` — Last 20 predictions
- `GET /stats` — Aggregated stats

## Docker Hub
🐳 [sunilakiran/noshow-iq-62671](https://hub.docker.com/r/sunilakiran/noshow-iq-62671)

## TestPyPI
📦 [noshow-iq-62671](https://test.pypi.org/project/noshow-iq-62671/)

## Dataset
[Medical Appointment No-Shows — Kaggle](https://www.kaggle.com/datasets/joniarroba/noshowappointments)