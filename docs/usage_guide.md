# ARISTO Usage Guide

Complete guide for using the ARISTO Quran Research & Discovery System.

## Table of Contents

1. [Getting Started](#getting-started)
2. [API Usage](#api-usage)
3. [Web UI Usage](#web-ui-usage)
4. [Modules Guide](#modules-guide)
5. [Advanced Features](#advanced-features)
6. [Troubleshooting](#troubleshooting)

## Getting Started

### First Time Setup

1. **Install Dependencies**
```bash
# Python dependencies
pip install -r requirements.txt

# UI dependencies
cd ui && npm install && cd ..
```

2. **Configure Environment**

Create a `.env` file in the project root:

```env
# Flask Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True
PORT=5000

# Database
DATABASE_URL=sqlite:///aristo.db

# ElasticSearch (optional)
ELASTICSEARCH_URL=http://localhost:9200
ELASTICSEARCH_INDEX=aristo_quran

# AI Integration (optional)
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key

# Security
JWT_SECRET_KEY=your-jwt-secret
```

3. **Start Services**

```bash
# Terminal 1: Start API
python api/app.py

# Terminal 2: Start UI
cd ui && npm run dev
```

## API Usage

### Authentication

Currently, the API is open for development. In production, add JWT authentication:

```python
# Example with JWT
headers = {
    'Authorization': 'Bearer YOUR_JWT_TOKEN'
}
```

### Search Endpoints

#### 1. Keyword Search

```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "prayer",
    "type": "keyword"
  }'
```

**Response:**
```json
{
  "status": "success",
  "query": "prayer",
  "results": [
    {
      "verse_id": "2:45",
      "text_arabic": "...",
      "translation": "...",
      "score": 95
    }
  ],
  "total": 10
}
```

#### 2. Semantic Search

```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "patience in hardship",
    "type": "semantic"
  }'
```

#### 3. Advanced Search

```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "charity",
    "type": "advanced",
    "filters": {
      "surah": 2,
      "theme": "charity"
    }
  }'
```

### Analysis Endpoints

#### Analyze Verse

```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "verse_id": "2:255",
    "modules": ["ebced", "semantic", "theme"]
  }'
```

**Response:**
```json
{
  "status": "success",
  "verse_id": "2:255",
  "analyses": {
    "ebced": {
      "total_value": 1234,
      "patterns": ["Prime number"]
    },
    "semantic": {
      "themes": ["Divine attributes", "Protection"]
    }
  }
}
```

### Report Generation

#### Generate Report

```bash
curl -X POST http://localhost:5000/api/report \
  -H "Content-Type: application/json" \
  -d '{
    "verse_id": "2:255",
    "mode": "long",
    "include_external": true
  }'
```

**Modes:**
- `short`: Basic information and translation
- `medium`: Includes tafsir, root analysis, themes
- `long`: Comprehensive with all modules and external sources

### Discovery Engine

```bash
curl -X POST http://localhost:5000/api/discover \
  -H "Content-Type: application/json" \
  -d '{
    "query": "water as a symbol",
    "depth": "deep"
  }'
```

### Module Management

#### List Modules

```bash
curl http://localhost:5000/api/modules
```

**Response:**
```json
{
  "status": "success",
  "modules": [
    {
      "name": "search",
      "status": "active",
      "description": "Full-text search"
    },
    {
      "name": "ebced",
      "status": "active",
      "description": "Ebced calculation"
    }
  ]
}
```

## Web UI Usage

### Search Interface

1. **Basic Search**
   - Enter search query in the search bar
   - Select search type (Keyword, Semantic, Advanced)
   - Click "Search" button

2. **View Results**
   - Results show verse ID, Arabic text, and translation
   - Click on a result for detailed analysis

3. **Module Status**
   - Scroll down to see available modules
   - Green badge indicates active modules
   - Click on a module for more information

### Navigation

- **Header**: Shows connection status to API
- **Search Bar**: Main search interface
- **Results Panel**: Displays search results
- **Module Status**: Shows available analysis modules

## Modules Guide

### Search Module

```python
from modules import search

# Keyword search
results = search.search("prayer", mode='keyword')

# Semantic search
results = search.search("patience", mode='semantic', top_k=10)

# Get specific verse
verse = search.search_module.get_verse(2, 255)
```

### Grouping Module

```python
from modules import group_verses

# Group by theme
grouped = group_verses(verses, by='theme')

# Group by surah
grouped = group_verses(verses, by='surah')

# Group by revelation type
grouped = group_verses(verses, by='revelation_type')
```

### Encryption Module

```python
from modules import encrypt, decrypt

# Encrypt data
encrypted = encrypt("sensitive data")

# Decrypt data
decrypted = decrypt(encrypted)

# Encrypt file
from modules import EncryptionModule
enc = EncryptionModule()
enc.encrypt_file('input.txt', 'output.enc')
```

### Backup Module

```python
from modules import create_backup, restore_backup

# Create backup
backup_path = create_backup([
    'data/',
    'models/',
    'config/'
], name='backup_20250123')

# Restore backup
restore_backup(backup_path, 'restore_path/')
```

### Report Module

```python
from modules import generate_report

# Generate short report
report = generate_report('2:255', mode='short')

# Generate comprehensive report
report = generate_report('2:255', mode='long', include_external=True)

# Export report
from modules import ReportModule
rm = ReportModule()
json_export = rm.export_report(report, format='json')
```

### Ebced Module

```python
from modules import calculate_ebced, analyze_ebced

# Calculate Ebced value
result = calculate_ebced("بسم الله")

# Analyze verse
analysis = analyze_ebced("قل هو الله أحد")
print(analysis['total_value'])
print(analysis['patterns'])
```

### AI Integration

```python
from modules import generate_embedding, ai_analyze

# Generate embedding
embedding = generate_embedding("text to embed", model='local')

# AI analysis
analysis = ai_analyze(
    text="verse text",
    prompt="Analyze the themes",
    provider='openai'
)
```

### ElasticSearch Integration

```python
from modules import es_search, ElasticSearchModule

# Search using ElasticSearch
results = es_search("prayer", size=10)

# Create index
es = ElasticSearchModule()
es.create_index('quran_verses')

# Index verses
es.bulk_index(verses_list)

# Vector search
results = es.vector_search(query_vector, size=10)
```

## Advanced Features

### Custom Module Development

Create custom analysis modules:

```python
# modules/custom_module.py
class CustomModule:
    def __init__(self):
        pass
    
    def analyze(self, verse_data):
        # Your custom analysis
        return results

# Export module
custom_module = CustomModule()

def analyze(verse_data):
    return custom_module.analyze(verse_data)
```

### Batch Processing

```python
# Process multiple verses
verses = ['2:255', '3:18', '4:1']
results = []

for verse_id in verses:
    report = generate_report(verse_id, mode='medium')
    results.append(report)
```

### Integration with External APIs

```python
import requests

def fetch_external_data(query):
    # Wikipedia API
    wiki_url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': query
    }
    response = requests.get(wiki_url, params=params)
    return response.json()
```

### Performance Optimization

1. **Use Caching**
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def cached_search(query):
    return search(query)
```

2. **Async Processing**
```python
import asyncio

async def process_verses(verses):
    tasks = [analyze_verse(v) for v in verses]
    return await asyncio.gather(*tasks)
```

## Troubleshooting

### Common Issues

#### 1. API Not Starting

**Problem**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
pip install -r requirements.txt
```

#### 2. UI Not Loading

**Problem**: `Cannot GET /`

**Solution**:
```bash
cd ui
npm install
npm run dev
```

#### 3. ElasticSearch Connection Failed

**Problem**: `ConnectionError: Cannot connect to ElasticSearch`

**Solution**:
- Check if ElasticSearch is running: `curl http://localhost:9200`
- Start ElasticSearch or disable it in config

#### 4. AI Integration Not Working

**Problem**: `OpenAI API key not found`

**Solution**:
- Add API keys to `.env` file
- Or disable AI features in config

### Debug Mode

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Getting Help

- Check logs in `logs/` directory
- Open an issue on GitHub
- Contact support team

## Best Practices

1. **Always validate input**: Use helper functions for validation
2. **Handle errors gracefully**: Use try-except blocks
3. **Cache frequently accessed data**: Reduce API calls
4. **Use appropriate search modes**: Semantic for concepts, keyword for exact matches
5. **Regular backups**: Schedule automated backups
6. **Monitor logs**: Check logs regularly for issues
7. **Keep dependencies updated**: Run `pip install -U` periodically

## Performance Tips

- Use batch processing for multiple queries
- Enable caching for repeated searches
- Use ElasticSearch for large datasets
- Optimize vector embeddings storage
- Consider using Redis for session management

## Security Considerations

- Never commit API keys to version control
- Use environment variables for secrets
- Enable JWT authentication in production
- Regularly update dependencies
- Use HTTPS in production
- Implement rate limiting

---

For more information, see the [README.md](../README.md) or open an issue on GitHub.
