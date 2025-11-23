#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARISTO Module: Grouping
Verse grouping and categorization system
"""

from typing import List, Dict, Set
from collections import defaultdict


class GroupingModule:
    """Verse grouping and categorization module"""
    
    def __init__(self):
        """Initialize grouping module"""
        self.groups = defaultdict(list)
        self.categories = {}
        
    def group_by_theme(self, verses: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Group verses by theme
        
        Args:
            verses: List of verse dictionaries
        
        Returns:
            dict: Verses grouped by theme
        """
        grouped = defaultdict(list)
        
        for verse in verses:
            theme = verse.get('theme', 'uncategorized')
            grouped[theme].append(verse)
        
        return dict(grouped)
    
    def group_by_surah(self, verses: List[Dict]) -> Dict[int, List[Dict]]:
        """
        Group verses by surah
        
        Args:
            verses: List of verse dictionaries
        
        Returns:
            dict: Verses grouped by surah number
        """
        grouped = defaultdict(list)
        
        for verse in verses:
            surah = verse.get('surah', 0)
            grouped[surah].append(verse)
        
        return dict(grouped)
    
    def group_by_juz(self, verses: List[Dict]) -> Dict[int, List[Dict]]:
        """
        Group verses by juz
        
        Args:
            verses: List of verse dictionaries
        
        Returns:
            dict: Verses grouped by juz number
        """
        grouped = defaultdict(list)
        
        for verse in verses:
            juz = verse.get('juz', 0)
            grouped[juz].append(verse)
        
        return dict(grouped)
    
    def group_by_revelation_type(self, verses: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Group verses by revelation type (Meccan/Medinan)
        
        Args:
            verses: List of verse dictionaries
        
        Returns:
            dict: Verses grouped by revelation type
        """
        grouped = {'meccan': [], 'medinan': []}
        
        for verse in verses:
            rev_type = verse.get('revelation_type', 'unknown')
            if rev_type in grouped:
                grouped[rev_type].append(verse)
        
        return grouped
    
    def create_custom_group(self, name: str, verses: List[Dict]) -> bool:
        """
        Create a custom group
        
        Args:
            name: Group name
            verses: Verses to include in group
        
        Returns:
            bool: Success status
        """
        self.groups[name] = verses
        return True
    
    def get_group(self, name: str) -> List[Dict]:
        """
        Get verses from a group
        
        Args:
            name: Group name
        
        Returns:
            list: Verses in the group
        """
        return self.groups.get(name, [])
    
    def list_groups(self) -> List[str]:
        """
        List all group names
        
        Returns:
            list: Group names
        """
        return list(self.groups.keys())
    
    def merge_groups(self, group_names: List[str], new_name: str) -> bool:
        """
        Merge multiple groups into one
        
        Args:
            group_names: Names of groups to merge
            new_name: Name for merged group
        
        Returns:
            bool: Success status
        """
        merged_verses = []
        
        for name in group_names:
            merged_verses.extend(self.groups.get(name, []))
        
        self.groups[new_name] = merged_verses
        return True
    
    def categorize_verse(self, verse: Dict, categories: List[str]) -> Dict:
        """
        Add categories to a verse
        
        Args:
            verse: Verse dictionary
            categories: List of category names
        
        Returns:
            dict: Updated verse with categories
        """
        verse_id = f"{verse.get('surah')}:{verse.get('ayah')}"
        self.categories[verse_id] = categories
        verse['categories'] = categories
        return verse


# Module instance
grouping_module = GroupingModule()


def group_verses(verses: List[Dict], by: str = 'theme') -> Dict:
    """
    Group verses by specified criterion
    
    Args:
        verses: List of verses
        by: Grouping criterion ('theme', 'surah', 'juz', 'revelation_type')
    
    Returns:
        dict: Grouped verses
    """
    if by == 'theme':
        return grouping_module.group_by_theme(verses)
    elif by == 'surah':
        return grouping_module.group_by_surah(verses)
    elif by == 'juz':
        return grouping_module.group_by_juz(verses)
    elif by == 'revelation_type':
        return grouping_module.group_by_revelation_type(verses)
    else:
        raise ValueError(f"Invalid grouping criterion: {by}")
