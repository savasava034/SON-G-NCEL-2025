"""
Full-Text Search Module
Tam Metin Arama Modülü - Kuran ayetlerinde tam metin araması
"""

import re
from typing import List, Dict, Any


class FullTextSearch:
    """
    Full-text search functionality for Quran verses.
    Provides search capabilities with Turkish and Arabic text support.
    """
    
    def __init__(self):
        """Initialize the full-text search engine"""
        self.index = {}
        self.verses = {}
        
    def add_verse(self, verse_id: str, arabic: str, translation: str, 
                  surah: int, verse: int, **kwargs):
        """
        Add a verse to the search index
        
        Args:
            verse_id: Unique verse identifier (e.g., "1:1")
            arabic: Arabic text of the verse
            translation: Turkish/English translation
            surah: Surah number
            verse: Verse number
            **kwargs: Additional metadata
        """
        verse_data = {
            "id": verse_id,
            "arabic": arabic,
            "translation": translation,
            "surah": surah,
            "verse": verse,
            **kwargs
        }
        
        self.verses[verse_id] = verse_data
        self._index_verse(verse_id, verse_data)
    
    def _index_verse(self, verse_id: str, verse_data: Dict[str, Any]):
        """Create search index for a verse"""
        # Index Arabic text
        arabic_words = self._tokenize(verse_data['arabic'])
        for word in arabic_words:
            if word not in self.index:
                self.index[word] = []
            if verse_id not in self.index[word]:
                self.index[word].append(verse_id)
        
        # Index translation
        translation_words = self._tokenize(verse_data['translation'])
        for word in translation_words:
            word_lower = word.lower()
            if word_lower not in self.index:
                self.index[word_lower] = []
            if verse_id not in self.index[word_lower]:
                self.index[word_lower].append(verse_id)
    
    def _tokenize(self, text: str) -> List[str]:
        """
        Tokenize text into searchable words
        
        Args:
            text: Text to tokenize
            
        Returns:
            List of word tokens
        """
        # Remove punctuation and split
        text = re.sub(r'[^\w\s\u0600-\u06FF]', ' ', text)
        words = text.split()
        return [w.strip() for w in words if len(w.strip()) > 0]
    
    def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Search for verses matching the query
        
        Args:
            query: Search query (can be Arabic or translation)
            limit: Maximum number of results to return
            
        Returns:
            List of matching verses with relevance scores
        """
        if not query:
            return []
        
        query_words = self._tokenize(query)
        if not query_words:
            return []
        
        # Find verses matching query words
        verse_scores = {}
        
        for word in query_words:
            word_lower = word.lower()
            
            # Check both original and lowercase
            for search_term in [word, word_lower]:
                if search_term in self.index:
                    for verse_id in self.index[search_term]:
                        if verse_id not in verse_scores:
                            verse_scores[verse_id] = 0
                        verse_scores[verse_id] += 1
        
        # Sort by relevance score
        sorted_verses = sorted(
            verse_scores.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:limit]
        
        # Prepare results
        results = []
        for verse_id, score in sorted_verses:
            verse_data = self.verses[verse_id].copy()
            verse_data['relevance_score'] = score
            results.append(verse_data)
        
        return results
    
    def search_by_surah(self, surah_number: int) -> List[Dict[str, Any]]:
        """
        Get all verses from a specific surah
        
        Args:
            surah_number: Surah number to retrieve
            
        Returns:
            List of verses from the surah
        """
        results = []
        for verse_id, verse_data in self.verses.items():
            if verse_data['surah'] == surah_number:
                results.append(verse_data)
        
        # Sort by verse number
        results.sort(key=lambda x: x['verse'])
        return results
    
    def search_phrase(self, phrase: str) -> List[Dict[str, Any]]:
        """
        Search for exact phrase in verses
        
        Args:
            phrase: Exact phrase to search for
            
        Returns:
            List of verses containing the phrase
        """
        phrase_lower = phrase.lower()
        results = []
        
        for verse_id, verse_data in self.verses.items():
            # Check in both Arabic and translation
            if (phrase in verse_data['arabic'] or 
                phrase_lower in verse_data['translation'].lower()):
                results.append(verse_data)
        
        return results
    
    def get_verse(self, verse_id: str) -> Dict[str, Any]:
        """
        Get a specific verse by ID
        
        Args:
            verse_id: Verse identifier (e.g., "1:1")
            
        Returns:
            Verse data or None if not found
        """
        return self.verses.get(verse_id)
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get search index statistics
        
        Returns:
            Dictionary with index statistics
        """
        return {
            "total_verses": len(self.verses),
            "total_words_indexed": len(self.index),
            "average_words_per_verse": len(self.index) / max(len(self.verses), 1)
        }


# Demo usage
if __name__ == "__main__":
    # Create search engine
    search_engine = FullTextSearch()
    
    # Add sample verses
    search_engine.add_verse(
        "1:1",
        "بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ",
        "Rahman ve Rahim olan Allah'ın adıyla",
        1, 1
    )
    
    search_engine.add_verse(
        "2:255",
        "ٱللَّهُ لَآ إِلَـٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ",
        "Allah ki, O'ndan başka ilah yoktur. Diridir, Kayyum'dur",
        2, 255
    )
    
    search_engine.add_verse(
        "112:1",
        "قُلْ هُوَ ٱللَّهُ أَحَدٌ",
        "De ki: O, Allah'tır, bir tektir",
        112, 1
    )
    
    # Test search
    print("=== Full-Text Search Demo ===\n")
    
    # Search for "Allah"
    print("Searching for 'Allah':")
    results = search_engine.search("Allah")
    for result in results:
        print(f"  {result['id']}: {result['translation'][:50]}...")
        print(f"  Relevance: {result['relevance_score']}\n")
    
    # Get statistics
    stats = search_engine.get_statistics()
    print(f"Statistics: {stats}")
