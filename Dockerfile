# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js for UI
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY api/ ./api/
COPY modules/ ./modules/
COPY config/ ./config/
COPY data/ ./data/

# Copy UI and install dependencies
COPY ui/ ./ui/
WORKDIR /app/ui
RUN npm install
RUN npm run build

# Go back to app directory
WORKDIR /app

# Create necessary directories
RUN mkdir -p logs cache memory vectorstore models backups

# Expose ports
EXPOSE 5000 3000

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=api/app.py

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run script
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
