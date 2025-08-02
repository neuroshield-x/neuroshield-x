# <img width="60" height="60" src="https://github.com/user-attachments/assets/a3175ffd-df64-4466-b1e0-2a1a62c6a6fb" /> NeuroShield-X

**AI-powered SIEM system** with real-time log anomaly detection and self-explaining alerts.

---

[🌐 Live Demo Page on Lovable.dev](https://neuroshieldx-landing-ai.lovable.app)

<img width="300" alt="UI screenshot" src="https://github.com/user-attachments/assets/26818570-8330-4f06-b396-083cea1f253d" />
<img width="300" alt="UI screenshot" src="https://github.com/user-attachments/assets/034f7abb-2529-480f-b019-c48b5c5d6364" />

---

## 🔍 Problem

Traditional SIEM tools flood analysts with technical alerts that lack context and clarity. Security teams often struggle to understand what’s urgent and what’s noise.

---

## 💡 Solution

**NeuroShield-X** enhances SIEMs with:

- Real-time log ingestion and display  
- AI-generated **natural-language alerts**  
- Clear **recommendations** for action  
- Simulated log activity for PoC testing  

---

## 🎯 PoC Achievements

- ✅ FastAPI backend with REST endpoints (`/analyze`, `/api/logs`, `/api/detect`)  
- ✅ Log producer script sending logs every 10 seconds  
- ✅ React frontend showing alert cards and log history  
- ✅ Live dashboard layout  
- ✅ All components runnable via `run.sh`  
- 🚧 **Next:** Real anomaly model, database, Kafka streaming  

---

## 🧠 Architecture

<img width="955" alt="architecture" src="https://github.com/user-attachments/assets/cda43871-0328-4b3b-90ba-7b8df61b5817" />

[ producer.py ] ---> POST /analyze (FastAPI) ---> [ stored logs / generated alerts ]
↘
/api/logs
/api/detect
↘
[ React UI ]

---

### 🖥️ Live Demo Screenshot

<img width="955" height="952" alt="Screenshot 2025-08-02 at 15 02 06" src="https://github.com/user-attachments/assets/152a6dec-7f76-4c18-93f5-9205ef53e6aa" />

---

## ⚙️ Tech Stack

- **Backend**: Python, FastAPI, Uvicorn, CORS  
- **Frontend**: React, Bootstrap  
- **Log Generator**: Python (`producer.py`)  
- **AI Alerts**: Currently mock logic; future → PyTorch  
- **Planned**: Kafka, MongoDB/Postgres, Docker, NGINX

---

## 📂 Folder Structure
```
neuroshield-poc/
├── backend/
│   ├── main.py              # FastAPI app with /analyze, /api/logs, /api/detect
│   ├── producer.py          # Sends synthetic logs to backend every 10s
│   ├── requirements.txt
│   └── venv/                # Python virtual environment
│
├── frontend/
│   ├── src/
│   │   ├── App.js           # Main alert UI
│   │   └── components/
│   │       └── LogList.jsx
│   └── public/
│
├── run.sh                  # Script to start backend, producer, frontend
├── README.md
└── plan.md                # One-page product overview
```


---

## 👥 Who Is It For?

- SOC teams needing faster alert triage  
- DevOps teams handling infrastructure security  
- Startups and researchers building open SIEM tooling

---

## 🚀 What’s Next?

- [ ] Integrate real AI anomaly detection (PyTorch)  
- [ ] Store logs in database (MongoDB/Postgres)  
- [ ] Add Kafka for scalable log ingestion  
- [ ] Containerize with Docker + NGINX gateway  
- [ ] Enable user-configurable alert filters and severity  