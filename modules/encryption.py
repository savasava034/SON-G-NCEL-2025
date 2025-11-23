#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARISTO Module: Encryption
Data encryption and security module
"""

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import os
from typing import Optional


class EncryptionModule:
    """Data encryption and security module"""
    
    def __init__(self, key: Optional[bytes] = None):
        """
        Initialize encryption module
        
        Args:
            key: Encryption key (generates new if not provided)
        """
        self.key = key or self._generate_key()
        self.cipher = Fernet(self.key)
    
    @staticmethod
    def _generate_key() -> bytes:
        """
        Generate a new encryption key
        
        Returns:
            bytes: Generated encryption key
        """
        return Fernet.generate_key()
    
    @staticmethod
    def derive_key_from_password(password: str, salt: Optional[bytes] = None) -> tuple:
        """
        Derive encryption key from password
        
        Args:
            password: User password
            salt: Salt for key derivation (generates new if not provided)
        
        Returns:
            tuple: (key, salt)
        """
        if salt is None:
            salt = os.urandom(16)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key, salt
    
    def encrypt_text(self, plaintext: str) -> str:
        """
        Encrypt text
        
        Args:
            plaintext: Text to encrypt
        
        Returns:
            str: Encrypted text (base64 encoded)
        """
        encrypted = self.cipher.encrypt(plaintext.encode('utf-8'))
        return base64.urlsafe_b64encode(encrypted).decode('utf-8')
    
    def decrypt_text(self, ciphertext: str) -> str:
        """
        Decrypt text
        
        Args:
            ciphertext: Encrypted text (base64 encoded)
        
        Returns:
            str: Decrypted plaintext
        """
        encrypted_bytes = base64.urlsafe_b64decode(ciphertext.encode('utf-8'))
        decrypted = self.cipher.decrypt(encrypted_bytes)
        return decrypted.decode('utf-8')
    
    def encrypt_file(self, input_path: str, output_path: str) -> bool:
        """
        Encrypt a file
        
        Args:
            input_path: Path to file to encrypt
            output_path: Path to save encrypted file
        
        Returns:
            bool: Success status
        """
        try:
            with open(input_path, 'rb') as f:
                data = f.read()
            
            encrypted = self.cipher.encrypt(data)
            
            with open(output_path, 'wb') as f:
                f.write(encrypted)
            
            return True
        except Exception as e:
            print(f"Encryption error: {e}")
            return False
    
    def decrypt_file(self, input_path: str, output_path: str) -> bool:
        """
        Decrypt a file
        
        Args:
            input_path: Path to encrypted file
            output_path: Path to save decrypted file
        
        Returns:
            bool: Success status
        """
        try:
            with open(input_path, 'rb') as f:
                encrypted_data = f.read()
            
            decrypted = self.cipher.decrypt(encrypted_data)
            
            with open(output_path, 'wb') as f:
                f.write(decrypted)
            
            return True
        except Exception as e:
            print(f"Decryption error: {e}")
            return False
    
    def get_key(self) -> str:
        """
        Get encryption key (base64 encoded)
        WARNING: This method exposes the encryption key. Use with caution.
        Only use in secure contexts where the key needs to be exported.
        
        Returns:
            str: Base64 encoded key
        """
        return base64.urlsafe_b64encode(self.key).decode('utf-8')
    
    def set_key(self, key: str):
        """
        Set encryption key from base64 encoded string
        
        Args:
            key: Base64 encoded key
        """
        self.key = base64.urlsafe_b64decode(key.encode('utf-8'))
        self.cipher = Fernet(self.key)


# Module instance
encryption_module = EncryptionModule()


def encrypt(data: str, key: Optional[str] = None) -> str:
    """
    Encrypt data
    
    Args:
        data: Data to encrypt
        key: Optional encryption key
    
    Returns:
        str: Encrypted data
    """
    if key:
        module = EncryptionModule(base64.urlsafe_b64decode(key.encode('utf-8')))
        return module.encrypt_text(data)
    return encryption_module.encrypt_text(data)


def decrypt(data: str, key: Optional[str] = None) -> str:
    """
    Decrypt data
    
    Args:
        data: Encrypted data
        key: Optional encryption key
    
    Returns:
        str: Decrypted data
    """
    if key:
        module = EncryptionModule(base64.urlsafe_b64decode(key.encode('utf-8')))
        return module.decrypt_text(data)
    return encryption_module.decrypt_text(data)
