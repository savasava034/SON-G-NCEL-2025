#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARISTO Main Runner
Quick start script for running the ARISTO system
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.9 or higher"""
    if sys.version_info < (3, 9):
        print("Error: Python 3.9 or higher is required")
        sys.exit(1)

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import flask
        print("✓ Flask is installed")
    except ImportError:
        print("✗ Flask not found. Installing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def create_directories():
    """Create necessary directories if they don't exist"""
    dirs = ['logs', 'cache', 'memory', 'data', 'models', 'vectorstore', 'backups', 'config']
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
    print("✓ Directories created/verified")

def check_env_file():
    """Check if .env file exists"""
    if not os.path.exists('.env'):
        print("⚠ .env file not found. Creating from .env.example...")
        if os.path.exists('.env.example'):
            subprocess.run(['cp', '.env.example', '.env'])
            print("✓ Created .env file. Please update it with your configuration.")
        else:
            print("✗ .env.example not found. Please create .env file manually.")

def start_api():
    """Start the Flask API"""
    print("\n" + "="*50)
    print("Starting ARISTO API...")
    print("="*50 + "\n")
    
    api_path = os.path.join(os.path.dirname(__file__), 'api', 'app.py')
    
    try:
        subprocess.run([sys.executable, api_path])
    except KeyboardInterrupt:
        print("\n\nShutting down ARISTO API...")
        sys.exit(0)

def main():
    """Main entry point"""
    print("""
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║              ARISTO SYSTEM LAUNCHER               ║
    ║     Quran Research & Discovery System            ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
    """)
    
    # Checks
    print("Running pre-flight checks...")
    check_python_version()
    print("✓ Python version OK")
    
    check_dependencies()
    create_directories()
    check_env_file()
    
    print("\n" + "="*50)
    print("All checks passed!")
    print("="*50)
    
    # Start services
    print("\nStarting services...")
    print("\nNote: To start the UI, open a new terminal and run:")
    print("  cd ui && npm install && npm run dev")
    print("\nThe UI will be available at: http://localhost:3000")
    print("The API will be available at: http://localhost:5000")
    print("\nPress Ctrl+C to stop the API\n")
    
    time.sleep(2)
    start_api()

if __name__ == '__main__':
    main()
