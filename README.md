# ARISTO - Quran Research & Discovery System

**SON-G-NCEL-2025** - Advanced Research and Intelligence System for Textual Observation

## 🌟 Overview

ARISTO is a comprehensive, multi-dimensional Quran research and discovery system that combines traditional Islamic scholarship with modern AI and data analysis technologies. The system enables deep exploration of Quranic verses through 30+ specialized analytical modules.

## 🎯 Core Features

- **Full-Text Search**: Advanced keyword, semantic, and multilingual search
- **Multi-Dimensional Analysis**: 30+ analytical modules including:
  - Ebced (Abjad) numerical analysis
  - Cifr analysis
  - Root (Kök) analysis
  - Semantic analysis
  - Thematic analysis
  - Symbolic interpretation
  - And many more...
- **AI Integration**: OpenAI, Anthropic, and local model support
- **ElasticSearch Integration**: Fast, scalable search engine
- **External Sources**: Integration with Wikipedia, Wikidata, Archive.org
- **Modern Web UI**: React-based responsive interface
- **REST API**: Flask-based backend API
- **Security**: Built-in encryption and secure data handling
- **Backup System**: Automated backup and restore functionality

## 📁 Project Structure

```
SON-G-NCEL-2025/
├── api/                    # Flask API Backend
│   ├── app.py             # Main Flask application
│   ├── config.py          # Configuration
│   ├── routes.py          # API routes
│   └── utils/             # Utility functions
│       ├── logger.py      # Logging utilities
│       └── helpers.py     # Helper functions
├── modules/               # ARISTO Modules
│   ├── search.py          # Full-text search
│   ├── grouping.py        # Verse grouping
│   ├── encryption.py      # Data encryption
│   ├── backup.py          # Backup system
│   ├── report.py          # Report generation
│   ├── priority.py        # Priority management
│   ├── ebced.py           # Ebced analysis
│   ├── ai_integration.py  # AI integration
│   └── elasticsearch_integration.py
├── ui/                    # React Web UI
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── App.jsx        # Main App component
│   │   └── main.jsx       # Entry point
│   ├── package.json
│   └── vite.config.js
├── data/                  # Data storage
├── models/                # AI models
├── vectorstore/           # Vector embeddings
├── config/                # Configuration files
├── cache/                 # Cache storage
├── memory/                # Query history
├── logs/                  # System logs
├── docs/                  # Documentation
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Node.js 18 or higher
- ElasticSearch 8.x (optional, for advanced search)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/savasava034/SON-G-NCEL-2025.git
cd SON-G-NCEL-2025
```

2. **Set up Python environment**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Create .env file
cp .env.example .env

# Edit .env with your configuration
# Add API keys for OpenAI, Anthropic if using AI features
```

4. **Install UI dependencies**
```bash
cd ui
npm install
cd ..
```

### Running the Application

#### Backend API

```bash
# From project root
python api/app.py

# API will be available at http://localhost:5000
```

#### Frontend UI

```bash
# In a new terminal
cd ui
npm run dev

# UI will be available at http://localhost:3000
```

## 📚 Usage Guide

See [docs/usage_guide.md](docs/usage_guide.md) for detailed usage instructions.

## 🔧 Configuration

### API Configuration

Edit `api/config.py` or set environment variables:

```python
# Flask settings
DEBUG = True
PORT = 5000

# Database
ELASTICSEARCH_URL = 'http://localhost:9200'

# AI Integration
OPENAI_API_KEY = 'your-key-here'
ANTHROPIC_API_KEY = 'your-key-here'

# Modules
MODULES_ENABLED = ['search', 'grouping', 'ebced', ...]
```

### UI Configuration

Edit `ui/vite.config.js` for development settings.

## 🧩 Modules

### Core Modules

1. **Search Module** - Full-text and semantic search
2. **Grouping Module** - Verse categorization and grouping
3. **Encryption Module** - Data security
4. **Backup Module** - System backup and restore
5. **Report Module** - Comprehensive report generation
6. **Priority Module** - Task priority management

### Analysis Modules

7. **Ebced Module** - Traditional Arabic numerology
8. **Cifr Module** - Cifr analysis
9. **Semantic Module** - Semantic analysis
10. **Theme Module** - Thematic extraction
11. **Root Module** - Arabic root analysis

### Integration Modules

12. **AI Integration** - OpenAI, Anthropic, local models
13. **ElasticSearch Integration** - Search engine
14. **External Sources** - Wikipedia, Wikidata, Archive.org

## 🔌 API Endpoints

### Main Endpoints

- `GET /` - API root and health check
- `GET /health` - System health status
- `POST /api/search` - Search verses
- `POST /api/analyze` - Analyze verse with modules
- `POST /api/report` - Generate comprehensive report
- `POST /api/discover` - Deep discovery engine
- `GET /api/modules` - List available modules
- `POST /api/external/search` - Search external sources
- `GET /api/history` - Query history

See [docs/usage_guide.md](docs/usage_guide.md) for detailed API documentation.

## 🧪 Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=api --cov=modules
```

## 📦 Docker Support

```bash
# Build Docker image
docker build -t aristo .

# Run container
docker run -p 5000:5000 -p 3000:3000 aristo
```

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines first.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built on the foundation of PrivateGPT architecture
- Inspired by traditional Islamic scholarship methods
- Powered by modern AI and search technologies

## 📞 Support

For support, please open an issue on GitHub or contact the development team.

## 🔒 Security

- All data is encrypted at rest
- API authentication via JWT tokens
- No data sent to external services without explicit permission
- Full GDPR compliance

## 🗺️ Roadmap

- [ ] Complete Quran database integration
- [ ] Advanced AI-powered discovery engine
- [ ] Multi-language support expansion
- [ ] Mobile application
- [ ] Community features
- [ ] Advanced visualization tools

## 📊 Status

**Version:** 1.0.0  
**Status:** Active Development  
**Last Updated:** 2025

---

Made with ❤️ for Quranic research and discovery
