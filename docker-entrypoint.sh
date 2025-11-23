#!/bin/bash
set -e

echo "Starting ARISTO Application..."

# Start Flask API in background
echo "Starting Flask API..."
python api/app.py &

# Wait for API to be ready
echo "Waiting for API to be ready..."
sleep 5

# Start UI (if in development mode)
if [ "$ENVIRONMENT" = "development" ]; then
    echo "Starting UI in development mode..."
    cd ui && npm run dev &
else
    echo "Serving built UI..."
    cd ui && npm run preview &
fi

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
