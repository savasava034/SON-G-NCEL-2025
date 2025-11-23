#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARISTO API Utilities - Helper Functions
"""

import hashlib
import json
from datetime import datetime
from typing import Any, Dict, List, Optional


def generate_hash(data: str) -> str:
    """
    Generate SHA256 hash of data
    
    Args:
        data: String to hash
    
    Returns:
        str: Hexadecimal hash string
    """
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def format_timestamp(dt: Optional[datetime] = None) -> str:
    """
    Format datetime to ISO string
    
    Args:
        dt: Datetime object (defaults to now)
    
    Returns:
        str: ISO formatted timestamp
    """
    if dt is None:
        dt = datetime.now()
    return dt.isoformat()


def validate_verse_id(verse_id: str) -> bool:
    """
    Validate Quran verse ID format (e.g., "2:255" for Surah 2, Ayah 255)
    
    Args:
        verse_id: Verse identifier
    
    Returns:
        bool: True if valid format
    """
    try:
        parts = verse_id.split(':')
        if len(parts) != 2:
            return False
        
        surah = int(parts[0])
        ayah = int(parts[1])
        
        # Basic validation (1-114 surahs)
        if not (1 <= surah <= 114):
            return False
        if ayah < 1:
            return False
        
        return True
    except (ValueError, AttributeError):
        return False


def parse_verse_id(verse_id: str) -> Dict[str, int]:
    """
    Parse verse ID into surah and ayah numbers
    
    Args:
        verse_id: Verse identifier (e.g., "2:255")
    
    Returns:
        dict: Dictionary with 'surah' and 'ayah' keys
    """
    if not validate_verse_id(verse_id):
        raise ValueError(f"Invalid verse ID format: {verse_id}")
    
    parts = verse_id.split(':')
    return {
        'surah': int(parts[0]),
        'ayah': int(parts[1])
    }


def create_response(status: str, data: Any = None, message: str = None) -> Dict:
    """
    Create standardized API response
    
    Args:
        status: Response status ('success' or 'error')
        data: Response data
        message: Optional message
    
    Returns:
        dict: Standardized response dictionary
    """
    response = {
        'status': status,
        'timestamp': format_timestamp()
    }
    
    if data is not None:
        response['data'] = data
    
    if message is not None:
        response['message'] = message
    
    return response


def sanitize_query(query: str) -> str:
    """
    Sanitize user query input
    
    Args:
        query: User query string
    
    Returns:
        str: Sanitized query
    """
    # Remove excessive whitespace
    query = ' '.join(query.split())
    
    # Remove potentially dangerous characters
    dangerous_chars = ['<', '>', '&', '"', "'", ';', '--', '/*', '*/']
    for char in dangerous_chars:
        query = query.replace(char, '')
    
    return query.strip()


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """
    Split text into chunks with overlap
    
    Args:
        text: Text to chunk
        chunk_size: Size of each chunk
        overlap: Overlap between chunks
    
    Returns:
        list: List of text chunks
    """
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    
    return chunks


def load_json_file(filepath: str) -> Dict:
    """
    Load JSON file safely
    
    Args:
        filepath: Path to JSON file
    
    Returns:
        dict: Loaded JSON data
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def save_json_file(filepath: str, data: Dict) -> bool:
    """
    Save data to JSON file
    
    Args:
        filepath: Path to save file
        data: Data to save
    
    Returns:
        bool: True if successful
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False
