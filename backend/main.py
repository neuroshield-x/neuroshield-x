from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import random
import datetime
from datetime import datetime as dt
from models import SessionLocal, Log

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

alerts = [
    {
        "event": "Failed login attempts",
        "explanation": "Unusual number of failed logins from a single IP address.",
        "recommendation": "Temporarily block IP and enforce MFA."
    },
    {
        "event": "Port scanning detected",
        "explanation": "Multiple ports accessed in short time by same host.",
        "recommendation": "Monitor the IP or block if behavior continues."
    },
    {
        "event": "Sudden traffic spike",
        "explanation": "A service is receiving 5x its normal traffic.",
        "recommendation": "Investigate source and scale service."
    },
    {
        "event": "New executable uploaded",
        "explanation": "An unrecognized binary was added to system.",
        "recommendation": "Scan uploaded file and check user activity."
    },
]

@app.get("/api/detect")
def get_alert():
    chosen = random.choice(alerts)
    return {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": f"192.168.1.{random.randint(1, 255)}",
        "event": chosen["event"],
        "anomalyScore": round(random.uniform(0.8, 0.99), 2),
        "explanation": chosen["explanation"],
        "recommendation": chosen["recommendation"]
    }

@app.post("/analyze")
async def analyze_log(log: dict):
    print("🔍 Received log:", log)
    db = SessionLocal()
    try:
        db_log = Log(
            timestamp=dt.strptime(log.get("timestamp"), "%Y-%m-%d %H:%M:%S"),
            ip=log.get("ip"),
            event=log.get("event"),
            anomalyScore=log.get("anomalyScore"),
            explanation=log.get("explanation"),
            recommendation=log.get("recommendation")
        )
        db.add(db_log)
        db.commit()
        print("✅ Log saved to DB.")
    except Exception as e:
        print("❌ DB insert error:", e)
    finally:
        db.close()
    return {"status": "received"}

@app.get("/api/logs")
def get_logs():
    db = SessionLocal()
    logs = db.query(Log).order_by(Log.timestamp.desc()).limit(20).all()
    db.close()
    return [
        {
            "timestamp": log.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "ip": log.ip,
            "event": log.event,
            "anomalyScore": log.anomalyScore,
            "explanation": log.explanation,
            "recommendation": log.recommendation
        }
        for log in logs
    ]
