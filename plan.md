# 🧠 NeuroShield-X – 1-Page Project Plan

## 🚨 What is it?

A lightweight AI-powered SIEM system that detects anomalies in logs and explains them in natural language. It helps security teams **understand** and **act on** alerts faster.

---

## 🔍 Problem

Traditional log monitoring systems:
- Overwhelm users with too many alerts
- Lack explanations and prioritization
- Don’t offer actionable recommendations

---

## 💡 Our Solution

NeuroShield-X:
- Uses ML to detect unusual behavior from logs
- Explains **why** the behavior is suspicious
- Suggests **what** the user should do (e.g., “Block IP”)

---

## 🧱 Architecture Overview

- **Frontend (React)**:
  - Displays real-time alerts with explanation
  - Includes log history and visualization

- **Backend (FastAPI)**:
  - `/analyze`: receives and stores logs
  - `/api/logs`: returns stored logs
  - `/api/detect`: returns mock AI alerts

- **Producer**:
  - Python script that sends fake logs every 10s

- **To Be Added**:
  - Kafka → real-time log ingestion
  - Database (Mongo/Postgres)
  - PyTorch model → real anomaly detection
  - NGINX gateway

---

## ✅ Current Status

- [x] GitHub repo, org, README, logo
- [x] PoC working:
  - FastAPI server
  - Producer log generator
  - React alert card
- [x] Lovable UI design done

---

## 📌 What’s Next

- [ ] Store logs in MongoDB/Postgres
- [ ] Replace mock AI with PyTorch model
- [ ] Kafka integration
- [ ] Docker + NGINX
- [ ] Final full-stack demo with metrics

---

## 🧠 Long-term Potential

Could be used by:
- SOCs with few analysts
- DevOps wanting quick log insight
- Open-source security tools