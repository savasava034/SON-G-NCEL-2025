#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARISTO Module: Backup
System backup and restore functionality
"""

import os
import shutil
import json
from datetime import datetime
from typing import List, Dict, Optional
import tarfile
import zipfile


class BackupModule:
    """Backup and restore module"""
    
    def __init__(self, backup_path: str = None):
        """
        Initialize backup module
        
        Args:
            backup_path: Path to store backups
        """
        self.backup_path = backup_path or os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'backups'
        )
        os.makedirs(self.backup_path, exist_ok=True)
    
    def create_backup(self, 
                     paths: List[str], 
                     backup_name: Optional[str] = None,
                     compress: bool = True) -> str:
        """
        Create a backup
        
        Args:
            paths: List of paths to backup
            backup_name: Name for backup (auto-generated if not provided)
            compress: Whether to compress the backup
        
        Returns:
            str: Path to backup file
        """
        if backup_name is None:
            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        if compress:
            backup_file = os.path.join(self.backup_path, f"{backup_name}.tar.gz")
            return self._create_compressed_backup(paths, backup_file)
        else:
            backup_dir = os.path.join(self.backup_path, backup_name)
            return self._create_directory_backup(paths, backup_dir)
    
    def _create_compressed_backup(self, paths: List[str], backup_file: str) -> str:
        """
        Create compressed backup using tar.gz
        
        Args:
            paths: Paths to backup
            backup_file: Output backup file path
        
        Returns:
            str: Backup file path
        """
        with tarfile.open(backup_file, 'w:gz') as tar:
            for path in paths:
                if os.path.exists(path):
                    tar.add(path, arcname=os.path.basename(path))
        
        # Create metadata
        metadata = {
            'created': datetime.now().isoformat(),
            'paths': paths,
            'size': os.path.getsize(backup_file)
        }
        
        metadata_file = backup_file + '.meta.json'
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return backup_file
    
    def _create_directory_backup(self, paths: List[str], backup_dir: str) -> str:
        """
        Create uncompressed directory backup
        
        Args:
            paths: Paths to backup
            backup_dir: Output backup directory
        
        Returns:
            str: Backup directory path
        """
        os.makedirs(backup_dir, exist_ok=True)
        
        for path in paths:
            if os.path.exists(path):
                dest = os.path.join(backup_dir, os.path.basename(path))
                if os.path.isdir(path):
                    shutil.copytree(path, dest)
                else:
                    shutil.copy2(path, dest)
        
        # Create metadata
        metadata = {
            'created': datetime.now().isoformat(),
            'paths': paths
        }
        
        metadata_file = os.path.join(backup_dir, 'backup.meta.json')
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return backup_dir
    
    def restore_backup(self, backup_file: str, restore_path: str) -> bool:
        """
        Restore from backup
        
        Args:
            backup_file: Path to backup file
            restore_path: Path to restore to
        
        Returns:
            bool: Success status
        """
        try:
            if backup_file.endswith('.tar.gz'):
                return self._restore_compressed_backup(backup_file, restore_path)
            else:
                return self._restore_directory_backup(backup_file, restore_path)
        except Exception as e:
            print(f"Restore error: {e}")
            return False
    
    def _restore_compressed_backup(self, backup_file: str, restore_path: str) -> bool:
        """
        Restore from compressed backup
        
        Args:
            backup_file: Backup file path
            restore_path: Restore destination
        
        Returns:
            bool: Success status
        """
        with tarfile.open(backup_file, 'r:gz') as tar:
            tar.extractall(restore_path)
        return True
    
    def _restore_directory_backup(self, backup_dir: str, restore_path: str) -> bool:
        """
        Restore from directory backup
        
        Args:
            backup_dir: Backup directory
            restore_path: Restore destination
        
        Returns:
            bool: Success status
        """
        shutil.copytree(backup_dir, restore_path, dirs_exist_ok=True)
        return True
    
    def list_backups(self) -> List[Dict]:
        """
        List all available backups
        
        Returns:
            list: List of backup information
        """
        backups = []
        
        for item in os.listdir(self.backup_path):
            item_path = os.path.join(self.backup_path, item)
            
            if item.endswith('.tar.gz'):
                meta_file = item_path + '.meta.json'
                if os.path.exists(meta_file):
                    with open(meta_file, 'r') as f:
                        metadata = json.load(f)
                    backups.append({
                        'name': item,
                        'path': item_path,
                        'type': 'compressed',
                        'metadata': metadata
                    })
            elif os.path.isdir(item_path):
                meta_file = os.path.join(item_path, 'backup.meta.json')
                if os.path.exists(meta_file):
                    with open(meta_file, 'r') as f:
                        metadata = json.load(f)
                    backups.append({
                        'name': item,
                        'path': item_path,
                        'type': 'directory',
                        'metadata': metadata
                    })
        
        return sorted(backups, key=lambda x: x['metadata']['created'], reverse=True)
    
    def delete_backup(self, backup_name: str) -> bool:
        """
        Delete a backup
        
        Args:
            backup_name: Name of backup to delete
        
        Returns:
            bool: Success status
        """
        backup_path = os.path.join(self.backup_path, backup_name)
        
        try:
            if os.path.isfile(backup_path):
                os.remove(backup_path)
                # Remove metadata file if exists
                meta_file = backup_path + '.meta.json'
                if os.path.exists(meta_file):
                    os.remove(meta_file)
            elif os.path.isdir(backup_path):
                shutil.rmtree(backup_path)
            
            return True
        except Exception as e:
            print(f"Delete error: {e}")
            return False


# Module instance
backup_module = BackupModule()


def create_backup(paths: List[str], name: Optional[str] = None) -> str:
    """
    Create a backup
    
    Args:
        paths: Paths to backup
        name: Backup name
    
    Returns:
        str: Backup file path
    """
    return backup_module.create_backup(paths, name)


def restore_backup(backup_file: str, restore_path: str) -> bool:
    """
    Restore from backup
    
    Args:
        backup_file: Backup file
        restore_path: Restore destination
    
    Returns:
        bool: Success status
    """
    return backup_module.restore_backup(backup_file, restore_path)
