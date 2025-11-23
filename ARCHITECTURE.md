# ARISTO System Architecture

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                    (React + Vite + Modern UI)                   │
│                     http://localhost:3000                       │
└───────────────────────────┬─────────────────────────────────────┘
                            │ HTTP/REST
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                         API LAYER                               │
│                    (Flask REST API)                             │
│                  http://localhost:5000                          │
│                                                                 │
│  Routes:                                                        │
│  ├─ GET  /                  (Health check)                     │
│  ├─ GET  /health           (System health)                     │
│  ├─ POST /api/search       (Search verses)                     │
│  ├─ POST /api/analyze      (Analyze verse)                     │
│  ├─ POST /api/report       (Generate report)                   │
│  ├─ POST /api/discover     (Deep discovery)                    │
│  ├─ GET  /api/modules      (List modules)                      │
│  ├─ POST /api/external/search (External search)                │
│  └─ GET  /api/history      (Query history)                     │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                    ARISTO MODULES LAYER                         │
│                 (10 Analysis Modules)                           │
│                                                                 │
│  Core Modules:                                                  │
│  ├─ search.py          Full-text & semantic search             │
│  ├─ grouping.py        Verse grouping & categorization         │
│  ├─ encryption.py      Data encryption & security              │
│  ├─ backup.py          Backup & restore system                 │
│  ├─ report.py          Report generation                       │
│  └─ priority.py        Task priority management                │
│                                                                 │
│  Analysis Modules:                                              │
│  ├─ ebced.py           Arabic numerology (Ebced/Abjad)         │
│  └─ (extensible)       Cifr, Huruf, Semantic, etc.            │
│                                                                 │
│  Integration Modules:                                           │
│  ├─ elasticsearch_integration.py  Search engine                │
│  └─ ai_integration.py             AI (OpenAI/Anthropic)        │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                      DATA LAYER                                 │
│                                                                 │
│  ┌────────────┐  ┌──────────────┐  ┌─────────────┐           │
│  │   Data     │  │   Models     │  │ Vector      │           │
│  │ (Quran)    │  │ (AI Models)  │  │ Store       │           │
│  └────────────┘  └──────────────┘  └─────────────┘           │
│                                                                 │
│  ┌────────────┐  ┌──────────────┐  ┌─────────────┐           │
│  │   Cache    │  │   Memory     │  │   Logs      │           │
│  │  (Temp)    │  │  (History)   │  │ (System)    │           │
│  └────────────┘  └──────────────┘  └─────────────┘           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    EXTERNAL SERVICES                            │
│                                                                 │
│  ┌──────────────┐  ┌────────────┐  ┌──────────────┐          │
│  │ElasticSearch │  │   Redis    │  │   OpenAI     │          │
│  │   (Search)   │  │  (Cache)   │  │    (AI)      │          │
│  └──────────────┘  └────────────┘  └──────────────┘          │
│                                                                 │
│  ┌──────────────┐  ┌────────────┐  ┌──────────────┐          │
│  │  Wikipedia   │  │ Wikidata   │  │ Archive.org  │          │
│  │  (Knowledge) │  │(Metadata)  │  │   (Books)    │          │
│  └──────────────┘  └────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

## Module Architecture

```
ARISTO Modules
├── Core Modules
│   ├── Search Module
│   │   ├── Keyword Search
│   │   ├── Semantic Search
│   │   ├── Advanced Search
│   │   └── Verse Retrieval
│   │
│   ├── Grouping Module
│   │   ├── Theme Grouping
│   │   ├── Surah Grouping
│   │   ├── Juz Grouping
│   │   └── Custom Groups
│   │
│   ├── Encryption Module
│   │   ├── Text Encryption
│   │   ├── File Encryption
│   │   └── Key Management
│   │
│   ├── Backup Module
│   │   ├── Create Backup
│   │   ├── Restore Backup
│   │   └── List Backups
│   │
│   ├── Report Module
│   │   ├── Short Report
│   │   ├── Medium Report
│   │   └── Long Report
│   │
│   └── Priority Module
│       ├── Task Queue
│       ├── Priority Levels
│       └── Task Management
│
├── Analysis Modules
│   ├── Ebced Module (Implemented ✓)
│   │   ├── Word Calculation
│   │   ├── Text Analysis
│   │   └── Pattern Detection
│   │
│   └── Extensible Modules (Stubs)
│       ├── Cifr Analysis
│       ├── Huruf Analysis
│       ├── Semantic Analysis
│       └── Theme Extraction
│
└── Integration Modules
    ├── ElasticSearch
    │   ├── Index Management
    │   ├── Full-text Search
    │   └── Vector Search
    │
    └── AI Integration
        ├── OpenAI (GPT-4)
        ├── Anthropic (Claude)
        └── Local Models
```

## Data Flow

```
User Query → UI → API → Modules → Data/External → Results → UI
     ↓                     ↓                          ↑
  History              Cache                     Format
     ↓                     ↓                          ↑
  Memory               Optimize                  Display
```

## Component Interactions

```
┌──────────┐
│   User   │
└────┬─────┘
     │
     ▼
┌─────────────────┐
│   React UI      │
│  (Frontend)     │
└────┬────────────┘
     │ HTTP Request
     ▼
┌─────────────────┐
│  Flask API      │◄──── Configuration
│  (Backend)      │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│ Module Router   │
└────┬────────────┘
     │
     ├──► Search Module ────► ElasticSearch
     │
     ├──► Analysis Module ──► Ebced Calculator
     │
     ├──► Report Module ────► Generator
     │
     ├──► AI Module ────────► OpenAI/Anthropic
     │
     └──► Data Access ──────► Storage
          
```

## Technology Stack

### Frontend
- **React** 18.2 - UI framework
- **Vite** 5.0 - Build tool
- **Axios** 1.6 - HTTP client
- **Styled Components** - CSS-in-JS

### Backend
- **Flask** 3.0 - Web framework
- **Flask-CORS** - Cross-origin support
- **Python** 3.9+ - Programming language

### Database & Search
- **ElasticSearch** 8.11 - Search engine
- **FAISS** - Vector similarity
- **ChromaDB** - Vector database
- **SQLAlchemy** 2.0 - SQL toolkit

### AI & ML
- **OpenAI** API - GPT models
- **Anthropic** API - Claude models
- **Transformers** 4.36 - Hugging Face
- **Sentence Transformers** 2.2 - Embeddings
- **LangChain** 0.1 - LLM framework

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container
- **Redis** - Caching
- **Nginx** (future) - Reverse proxy

## Deployment Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Docker Compose                          │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────┐  │
│  │   aristo-ui  │  │  aristo-api  │  │ elasticsearch  │  │
│  │  (Port 3000) │  │ (Port 5000)  │  │  (Port 9200)   │  │
│  └──────────────┘  └──────────────┘  └────────────────┘  │
│                                                             │
│  ┌──────────────┐                                          │
│  │    redis     │                                          │
│  │  (Port 6379) │                                          │
│  └──────────────┘                                          │
│                                                             │
│  Volumes: data, models, logs, cache, memory, vectorstore   │
└─────────────────────────────────────────────────────────────┘
```

## Security Architecture

```
┌─────────────────────────────────────────────────┐
│              Security Layers                    │
│                                                 │
│  1. Input Validation                           │
│     └─ Sanitize queries (Arabic-aware)        │
│                                                 │
│  2. Authentication                             │
│     └─ JWT tokens (future)                    │
│                                                 │
│  3. Encryption                                 │
│     ├─ Data at rest (Fernet)                 │
│     └─ Data in transit (HTTPS)               │
│                                                 │
│  4. Access Control                             │
│     └─ API rate limiting                      │
│                                                 │
│  5. Audit Logging                              │
│     └─ All operations logged                  │
└─────────────────────────────────────────────────┘
```

## Scalability Considerations

- **Horizontal Scaling**: Multiple API instances behind load balancer
- **Caching**: Redis for frequently accessed data
- **Async Processing**: Celery for background tasks
- **Database Sharding**: For large Quran corpus
- **CDN**: For static assets
- **Microservices**: Module separation (future)

---

**Version**: 1.0.0  
**Last Updated**: 2025-11-23
