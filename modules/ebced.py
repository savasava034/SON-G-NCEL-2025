#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARISTO Module: Ebced (Abjad) Calculation
Traditional Arabic numerology system
"""

from typing import Dict, List


class EbcedModule:
    """Ebced (Abjad) calculation module"""
    
    # Ebced letter values
    EBCED_VALUES = {
        'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1,
        'ب': 2,
        'ج': 3,
        'د': 4,
        'ه': 5, 'ة': 5,
        'و': 6,
        'ز': 7,
        'ح': 8,
        'ط': 9,
        'ي': 10, 'ى': 10,
        'ك': 20,
        'ل': 30,
        'م': 40,
        'ن': 50,
        'س': 60,
        'ع': 70,
        'ف': 80,
        'ص': 90,
        'ق': 100,
        'ر': 200,
        'ش': 300,
        'ت': 400,
        'ث': 500,
        'خ': 600,
        'ذ': 700,
        'ض': 800,
        'ظ': 900,
        'غ': 1000
    }
    
    def __init__(self):
        """Initialize Ebced module"""
        pass
    
    def calculate_word(self, word: str) -> int:
        """
        Calculate Ebced value of a word
        
        Args:
            word: Arabic word
        
        Returns:
            int: Ebced value
        """
        total = 0
        for char in word:
            total += self.EBCED_VALUES.get(char, 0)
        return total
    
    def calculate_text(self, text: str) -> Dict:
        """
        Calculate Ebced values for text
        
        Args:
            text: Arabic text
        
        Returns:
            dict: Detailed Ebced analysis
        """
        words = text.split()
        word_values = []
        
        for word in words:
            value = self.calculate_word(word)
            word_values.append({
                'word': word,
                'value': value
            })
        
        total_value = sum(wv['value'] for wv in word_values)
        
        return {
            'text': text,
            'total_value': total_value,
            'word_count': len(words),
            'word_values': word_values,
            'average_value': total_value / len(words) if words else 0
        }
    
    def find_words_by_value(self, target_value: int, words: List[str]) -> List[str]:
        """
        Find words with specific Ebced value
        
        Args:
            target_value: Target Ebced value
            words: List of words to search
        
        Returns:
            list: Words matching the value
        """
        matching = []
        for word in words:
            if self.calculate_word(word) == target_value:
                matching.append(word)
        return matching
    
    def analyze_verse(self, verse_text: str) -> Dict:
        """
        Comprehensive Ebced analysis of a verse
        
        Args:
            verse_text: Verse text in Arabic
        
        Returns:
            dict: Detailed analysis
        """
        analysis = self.calculate_text(verse_text)
        
        # Additional analysis
        letter_freq = {}
        for char in verse_text:
            if char in self.EBCED_VALUES:
                letter_freq[char] = letter_freq.get(char, 0) + 1
        
        analysis['letter_frequency'] = letter_freq
        analysis['unique_letters'] = len(letter_freq)
        analysis['total_letters'] = sum(letter_freq.values())
        
        # Patterns
        analysis['patterns'] = self._find_patterns(analysis['total_value'])
        
        return analysis
    
    def _find_patterns(self, value: int) -> List[str]:
        """
        Find numerical patterns
        
        Args:
            value: Numerical value
        
        Returns:
            list: Identified patterns
        """
        patterns = []
        
        # Check if prime
        if self._is_prime(value):
            patterns.append(f"Prime number: {value}")
        
        # Check if perfect square
        sqrt = int(value ** 0.5)
        if sqrt * sqrt == value:
            patterns.append(f"Perfect square: {sqrt}²")
        
        # Check divisibility by significant numbers
        significant = [7, 19, 114]
        for num in significant:
            if value % num == 0:
                patterns.append(f"Divisible by {num}")
        
        return patterns
    
    @staticmethod
    def _is_prime(n: int) -> bool:
        """Check if number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


# Module instance
ebced_module = EbcedModule()


def calculate(text: str) -> Dict:
    """
    Calculate Ebced value
    
    Args:
        text: Arabic text
    
    Returns:
        dict: Ebced analysis
    """
    return ebced_module.calculate_text(text)


def analyze_verse(verse_text: str) -> Dict:
    """
    Analyze verse using Ebced
    
    Args:
        verse_text: Verse text
    
    Returns:
        dict: Analysis results
    """
    return ebced_module.analyze_verse(verse_text)
