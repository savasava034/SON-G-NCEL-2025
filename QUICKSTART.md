# ARISTO Quick Start Guide

Get up and running with ARISTO in 5 minutes!

## Prerequisites

- Python 3.9+ installed
- Node.js 18+ installed (for UI)
- 2GB free disk space

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/savasava034/SON-G-NCEL-2025.git
cd SON-G-NCEL-2025
```

### 2. Install Python Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your preferred editor
# Add API keys if you plan to use AI features (optional)
```

### 4. Test Installation

```bash
# Run installation test
python test_installation.py

# You should see: ✓ All tests passed!
```

### 5. Start the API

```bash
# Option 1: Using the launcher
python run.py

# Option 2: Direct start
python api/app.py
```

The API will start at: http://localhost:5000

### 6. Start the UI (Optional)

Open a new terminal:

```bash
# Navigate to UI directory
cd ui

# Install dependencies (first time only)
npm install

# Start development server
npm run dev
```

The UI will start at: http://localhost:3000

## Quick Test

### Test API

```bash
# Test health endpoint
curl http://localhost:5000/health

# Test modules endpoint
curl http://localhost:5000/api/modules
```

### Test in Browser

1. Open http://localhost:3000 (UI) or http://localhost:5000 (API)
2. Enter a search query
3. Select search type
4. Click Search

## Basic Usage

### Python API

```python
from modules import calculate_ebced, search, generate_report

# Calculate Ebced value
result = calculate_ebced("بسم الله الرحمن الرحيم")
print(f"Ebced value: {result['total_value']}")

# Search verses (when data is loaded)
results = search("prayer", mode='keyword')

# Generate report (when data is loaded)
report = generate_report("2:255", mode='short')
```

### REST API

```bash
# Search
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "prayer", "type": "keyword"}'

# List modules
curl http://localhost:5000/api/modules
```

## Next Steps

1. **Add Quran Data**: Place your Quran data files in the `data/` directory
2. **Configure ElasticSearch**: Install and configure ElasticSearch for advanced search
3. **Enable AI Features**: Add API keys to `.env` for AI-powered analysis
4. **Explore Modules**: Check `docs/usage_guide.md` for detailed module documentation
5. **Customize**: Modify modules and add your own analysis logic

## Troubleshooting

### Issue: ModuleNotFoundError

**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: API won't start

**Solution**: Check port 5000 is not in use
```bash
# Windows
netstat -ano | findstr :5000
# Linux/Mac
lsof -i :5000
```

### Issue: UI won't start

**Solution**: Install Node.js dependencies
```bash
cd ui
npm install
```

## Docker Deployment

For production deployment using Docker:

```bash
# Build and start all services
docker-compose up -d

# Stop services
docker-compose down
```

Services will be available at:
- API: http://localhost:5000
- UI: http://localhost:3000
- ElasticSearch: http://localhost:9200

## Getting Help

- Read the [full documentation](docs/usage_guide.md)
- Check the [README](README.md)
- Open an issue on GitHub
- Run the test script: `python test_installation.py`

## Project Structure

```
SON-G-NCEL-2025/
├── api/              # Backend API
├── modules/          # Analysis modules
├── ui/               # Frontend
├── data/             # Data storage
├── docs/             # Documentation
└── run.py            # Quick launcher
```

## Important Files

- `run.py` - Quick start launcher
- `test_installation.py` - Verify installation
- `.env.example` - Configuration template
- `requirements.txt` - Python dependencies
- `docker-compose.yml` - Docker deployment

---

**Ready to start?** Run `python run.py` and open http://localhost:5000 🚀
