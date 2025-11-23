#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARISTO Module: ElasticSearch Integration
Full-text search using ElasticSearch
"""

from typing import List, Dict, Optional
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError, NotFoundError


class ElasticSearchModule:
    """ElasticSearch integration module"""
    
    def __init__(self, host: str = 'localhost', port: int = 9200):
        """
        Initialize ElasticSearch connection
        
        Args:
            host: ElasticSearch host
            port: ElasticSearch port
        """
        self.host = host
        self.port = port
        self.es = None
        self.index_name = 'aristo_quran'
        self._connect()
    
    def _connect(self):
        """Establish connection to ElasticSearch"""
        try:
            self.es = Elasticsearch([f'http://{self.host}:{self.port}'])
            if self.es.ping():
                print(f"Connected to ElasticSearch at {self.host}:{self.port}")
            else:
                print("ElasticSearch connection failed")
                self.es = None
        except ConnectionError:
            print(f"Could not connect to ElasticSearch at {self.host}:{self.port}")
            self.es = None
    
    def create_index(self, index_name: Optional[str] = None):
        """
        Create ElasticSearch index
        
        Args:
            index_name: Index name (defaults to self.index_name)
        """
        if not self.es:
            return False
        
        index = index_name or self.index_name
        
        # Index mapping for Quran verses
        mapping = {
            'mappings': {
                'properties': {
                    'surah': {'type': 'integer'},
                    'ayah': {'type': 'integer'},
                    'verse_id': {'type': 'keyword'},
                    'text_arabic': {
                        'type': 'text',
                        'analyzer': 'arabic'
                    },
                    'text_english': {'type': 'text'},
                    'text_turkish': {'type': 'text'},
                    'translation_en': {'type': 'text'},
                    'translation_tr': {'type': 'text'},
                    'themes': {'type': 'keyword'},
                    'revelation_type': {'type': 'keyword'},
                    'juz': {'type': 'integer'},
                    'page': {'type': 'integer'},
                    'embedding': {
                        'type': 'dense_vector',
                        'dims': 384  # For sentence-transformers models
                    }
                }
            }
        }
        
        try:
            if not self.es.indices.exists(index=index):
                self.es.indices.create(index=index, body=mapping)
                print(f"Index '{index}' created successfully")
                return True
            else:
                print(f"Index '{index}' already exists")
                return True
        except Exception as e:
            print(f"Error creating index: {e}")
            return False
    
    def index_verse(self, verse_data: Dict):
        """
        Index a single verse
        
        Args:
            verse_data: Verse data dictionary
        """
        if not self.es:
            return False
        
        try:
            verse_id = verse_data.get('verse_id')
            self.es.index(index=self.index_name, id=verse_id, document=verse_data)
            return True
        except Exception as e:
            print(f"Error indexing verse: {e}")
            return False
    
    def bulk_index(self, verses: List[Dict]):
        """
        Index multiple verses
        
        Args:
            verses: List of verse data dictionaries
        """
        if not self.es:
            return False
        
        from elasticsearch.helpers import bulk
        
        actions = [
            {
                '_index': self.index_name,
                '_id': verse['verse_id'],
                '_source': verse
            }
            for verse in verses
        ]
        
        try:
            success, failed = bulk(self.es, actions)
            print(f"Indexed {success} verses, {failed} failed")
            return True
        except Exception as e:
            print(f"Error bulk indexing: {e}")
            return False
    
    def search(self, 
              query: str,
              fields: List[str] = None,
              size: int = 10) -> List[Dict]:
        """
        Search verses
        
        Args:
            query: Search query
            fields: Fields to search in
            size: Number of results
        
        Returns:
            list: Search results
        """
        if not self.es:
            return []
        
        if fields is None:
            fields = ['text_arabic', 'text_english', 'text_turkish']
        
        search_body = {
            'query': {
                'multi_match': {
                    'query': query,
                    'fields': fields
                }
            },
            'size': size
        }
        
        try:
            response = self.es.search(index=self.index_name, body=search_body)
            hits = response['hits']['hits']
            return [hit['_source'] for hit in hits]
        except Exception as e:
            print(f"Search error: {e}")
            return []
    
    def vector_search(self,
                     query_vector: List[float],
                     size: int = 10) -> List[Dict]:
        """
        Semantic search using vectors
        
        Args:
            query_vector: Query embedding vector
            size: Number of results
        
        Returns:
            list: Similar verses
        """
        if not self.es:
            return []
        
        search_body = {
            'query': {
                'script_score': {
                    'query': {'match_all': {}},
                    'script': {
                        'source': "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                        'params': {'query_vector': query_vector}
                    }
                }
            },
            'size': size
        }
        
        try:
            response = self.es.search(index=self.index_name, body=search_body)
            hits = response['hits']['hits']
            return [hit['_source'] for hit in hits]
        except Exception as e:
            print(f"Vector search error: {e}")
            return []
    
    def get_verse(self, verse_id: str) -> Optional[Dict]:
        """
        Get verse by ID
        
        Args:
            verse_id: Verse identifier
        
        Returns:
            dict: Verse data or None
        """
        if not self.es:
            return None
        
        try:
            response = self.es.get(index=self.index_name, id=verse_id)
            return response['_source']
        except NotFoundError:
            return None
        except Exception as e:
            print(f"Error getting verse: {e}")
            return None


# Module instance
es_module = ElasticSearchModule()


def search(query: str, **kwargs) -> List[Dict]:
    """
    Search using ElasticSearch
    
    Args:
        query: Search query
        **kwargs: Additional search parameters
    
    Returns:
        list: Search results
    """
    return es_module.search(query, **kwargs)
