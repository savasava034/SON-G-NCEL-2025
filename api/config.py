#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARISTO API Configuration
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Base configuration"""
    
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY', 'aristo-secret-key-change-in-production')
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    # API Settings
    API_VERSION = '1.0.0'
    API_TITLE = 'ARISTO Quran Research API'
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///aristo.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # ElasticSearch
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL', 'http://localhost:9200')
    ELASTICSEARCH_INDEX = os.environ.get('ELASTICSEARCH_INDEX', 'aristo_quran')
    
    # AI Configuration
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
    
    # Models Path
    MODELS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'models')
    
    # Vector Store
    VECTOR_STORE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'vectorstore')
    
    # Data Path
    DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    
    # Cache Settings
    CACHE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cache')
    CACHE_TIMEOUT = 3600  # 1 hour
    
    # Memory/History
    MEMORY_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'memory')
    
    # Logs
    LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    
    # Module Settings
    MODULES_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'modules')
    
    # ARISTO Modules Configuration
    MODULES_ENABLED = [
        'search',       # Full-text search
        'grouping',     # Verse grouping
        'encryption',   # Data encryption
        'backup',       # Backup system
        'report',       # Report generation
        'priority',     # Priority management
        'ebced',        # Ebced calculation
        'cifr',         # Cifr analysis
        'huruf',        # Letter analysis
        'semantic',     # Semantic analysis
        'numeral',      # Numerology
        'tasavvuf',     # Sufi interpretation
        'tafsir',       # Tafsir integration
        'kroot',        # Root analysis
        'theme',        # Theme extraction
    ]
    
    # External API Configuration
    WIKIPEDIA_API = 'https://en.wikipedia.org/w/api.php'
    WIKIDATA_API = 'https://www.wikidata.org/w/api.php'
    ARCHIVE_API = 'https://archive.org/services/search/v1/scrape'
    
    # Report Settings
    REPORT_MODES = ['short', 'medium', 'long']
    DEFAULT_REPORT_MODE = 'medium'
    
    # Security
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-change-in-production')
    JWT_ALGORITHM = 'HS256'
    JWT_EXPIRATION_HOURS = 24
    
    # Rate Limiting
    RATELIMIT_ENABLED = True
    RATELIMIT_DEFAULT = "100 per hour"
    
    # CORS
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*').split(',')


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
