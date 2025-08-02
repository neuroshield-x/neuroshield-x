import requests
import random
import time
from datetime import datetime

events = [
    ("Failed login attempts", "Unusual number of failed logins from a single IP address.", "Temporarily block IP {ip} and enforce MFA."),
    ("Port scanning detected", "Multiple ports accessed in short time by same host.", "Monitor the IP or block if behavior continues."),
    ("Suspicious file access", "Sensitive files accessed outside of work hours.", "Investigate the user activity."),
    ("High data exfiltration", "Large volume of data sent externally.", "Limit outbound traffic and verify the recipient."),
]

def generate_log():
    ip = f"192.168.1.{random.randint(1, 255)}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    event, explanation, recommendation_template = random.choice(events)
    score = round(random.uniform(0.7, 0.98), 2)
    recommendation = recommendation_template.format(ip=ip)

    return {
        "timestamp": timestamp,
        "ip": ip,
        "event": event,
        "anomalyScore": score,
        "explanation": explanation,
        "recommendation": recommendation
    }

while True:
    log = generate_log()
    try:
        response = requests.post("http://localhost:8000/analyze", json=log)
        print(f"✅ Sent log: {log['event']} → {response.status_code}")
    except Exception as e:
        print("❌ Failed to send log:", e)
    time.sleep(10)
