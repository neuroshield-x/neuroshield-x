#!/bin/bash

echo "🚀 Starting NeuroShield X PoC..."

# Ensure we're in the project root
cd "$(dirname "$0")"

# Activate virtual environment
echo "🧪 Activating Python venv..."
source backend/venv/bin/activate

# Run FastAPI backend
echo "🔧 Starting FastAPI backend..."
cd backend
uvicorn main:app --reload > ../backend.log 2>&1 &
BACKEND_PID=$!
cd ..

# Run log producer
echo "📡 Starting log producer..."
python backend/producer.py > producer.log 2>&1 &
PRODUCER_PID=$!

# Run React frontend
echo "🌐 Starting React frontend..."
cd frontend
npm start > ../frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..

# Trap to clean up on exit
trap "echo '🛑 Stopping services...'; kill $BACKEND_PID $FRONTEND_PID $PRODUCER_PID" EXIT

# Wait for processes to finish
wait $BACKEND_PID $FRONTEND_PID $PRODUCER_PID
