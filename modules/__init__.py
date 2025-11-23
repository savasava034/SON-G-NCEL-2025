#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARISTO Modules Package
Collection of specialized analysis and utility modules
"""

# Core modules
from .search import search, SearchModule
from .grouping import group_verses, GroupingModule
from .encryption import encrypt, decrypt, EncryptionModule
from .backup import create_backup, restore_backup, BackupModule
from .report import generate_report, ReportModule
from .priority import add_task, get_next_task, PriorityModule

# Analysis modules
from .ebced import calculate as calculate_ebced, analyze_verse as analyze_ebced, EbcedModule

# Integration modules (optional - may not be available without dependencies)
try:
    from .elasticsearch_integration import search as es_search, ElasticSearchModule
    _elasticsearch_available = True
except ImportError:
    _elasticsearch_available = False
    es_search = None
    ElasticSearchModule = None

try:
    from .ai_integration import generate_embedding, analyze as ai_analyze, AIModule
    _ai_available = True
except ImportError:
    _ai_available = False
    generate_embedding = None
    ai_analyze = None
    AIModule = None

__all__ = [
    # Core modules
    'search',
    'SearchModule',
    'group_verses',
    'GroupingModule',
    'encrypt',
    'decrypt',
    'EncryptionModule',
    'create_backup',
    'restore_backup',
    'BackupModule',
    'generate_report',
    'ReportModule',
    'add_task',
    'get_next_task',
    'PriorityModule',
    
    # Analysis modules
    'calculate_ebced',
    'analyze_ebced',
    'EbcedModule',
    
    # Integration modules (may be None if not available)
    'es_search',
    'ElasticSearchModule',
    'generate_embedding',
    'ai_analyze',
    'AIModule',
]
