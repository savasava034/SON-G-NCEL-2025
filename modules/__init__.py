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

# Integration modules
from .elasticsearch_integration import search as es_search, ElasticSearchModule
from .ai_integration import generate_embedding, analyze as ai_analyze, AIModule

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
    
    # Integration modules
    'es_search',
    'ElasticSearchModule',
    'generate_embedding',
    'ai_analyze',
    'AIModule',
]
