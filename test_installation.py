#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARISTO Installation Test
Quick test to verify the installation is working correctly
"""

import sys

def test_python_version():
    """Test Python version"""
    print("Testing Python version...")
    if sys.version_info >= (3, 9):
        print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} - OK")
        return True
    else:
        print(f"✗ Python {sys.version_info.major}.{sys.version_info.minor} - Need 3.9+")
        return False

def test_api_import():
    """Test API import"""
    print("\nTesting API import...")
    try:
        from api import app
        print(f"✓ API imports successfully")
        print(f"✓ Flask app: {app.name}")
        return True
    except ImportError as e:
        print(f"✗ API import failed: {e}")
        return False

def test_modules_import():
    """Test modules import"""
    print("\nTesting modules import...")
    try:
        from modules import (
            search, grouping, encryption, backup, 
            report, priority, calculate_ebced
        )
        print("✓ Core modules import successfully")
        return True
    except ImportError as e:
        print(f"✗ Modules import failed: {e}")
        return False

def test_ebced_functionality():
    """Test Ebced module functionality"""
    print("\nTesting Ebced module...")
    try:
        from modules import calculate_ebced
        result = calculate_ebced('الله')
        print(f"✓ Ebced calculation works")
        print(f"  Test: 'الله' = {result['total_value']}")
        return True
    except Exception as e:
        print(f"✗ Ebced test failed: {e}")
        return False

def test_api_routes():
    """Test API routes"""
    print("\nTesting API routes...")
    try:
        from api.app import app
        with app.test_client() as client:
            # Test health endpoint
            response = client.get('/health')
            if response.status_code == 200:
                print("✓ Health endpoint working")
            
            # Test root endpoint
            response = client.get('/')
            if response.status_code == 200:
                print("✓ Root endpoint working")
            
            # Test modules endpoint
            response = client.get('/api/modules')
            if response.status_code == 200:
                print("✓ Modules endpoint working")
            
            return True
    except Exception as e:
        print(f"✗ API routes test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("="*60)
    print("ARISTO Installation Test")
    print("="*60)
    
    tests = [
        test_python_version,
        test_api_import,
        test_modules_import,
        test_ebced_functionality,
        test_api_routes
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            results.append(False)
    
    print("\n" + "="*60)
    passed = sum(results)
    total = len(results)
    print(f"Test Results: {passed}/{total} passed")
    
    if all(results):
        print("✓ All tests passed! Installation is working correctly.")
        print("\nYou can now run:")
        print("  python run.py              # Start the API")
        print("  cd ui && npm run dev       # Start the UI")
        return 0
    else:
        print("✗ Some tests failed. Please check the output above.")
        print("\nMake sure you have installed dependencies:")
        print("  pip install -r requirements.txt")
        return 1

if __name__ == '__main__':
    sys.exit(main())
