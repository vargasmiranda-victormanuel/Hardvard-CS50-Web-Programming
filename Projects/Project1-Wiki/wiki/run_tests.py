#!/usr/bin/env python
"""
Test runner script for the Wiki application tests.
This script ensures tests run in the correct environment with proper setup.
"""

import os
import sys
import subprocess

def run_tests():
    """Run the Selenium tests for the Wiki application"""
    
    # Change to the project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    print("🚀 Starting Wiki Application Tests")
    print("=" * 50)
    
    # Check if virtual environment is activated
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment is active")
    else:
        print("⚠️  Virtual environment may not be active")
        print("   Please activate your virtual environment first:")
        print("   On Windows: wiki_venv\\Scripts\\activate")
        print("   On macOS/Linux: source wiki_venv/bin/activate")
    
    print("\n📋 Test Information:")
    print("   - Target URL: http://127.0.0.1:8000/")
    print("   - Test: Create new 'Selenium' wiki page")
    print("   - Browser: Chrome (ensure ChromeDriver is installed)")
    
    print("\n⚠️  Prerequisites:")
    print("   1. Django development server should be running on http://127.0.0.1:8000/")
    print("   2. ChromeDriver should be installed and in PATH")
    print("   3. Chrome browser should be installed")
    
    # Ask user to confirm server is running
    response = input("\n❓ Is the Django server running? (y/n): ").lower().strip()
    if response != 'y':
        print("\n🔧 To start the Django server, run:")
        print("   python manage.py runserver")
        print("   Then run this test script again.")
        return
    
    try:
        print("\n🧪 Running tests with pytest...")
        print("-" * 30)
        
        # Run the specific test file
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/test_selenium.py::test_create_new_selenium_wiki_page",
            "-v", "--tb=short"
        ], capture_output=False, text=True)
        
        if result.returncode == 0:
            print("\n✅ All tests passed successfully!")
        else:
            print("\n❌ Some tests failed. Check the output above for details.")
            
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error running tests: {e}")
        print("\n🔧 Try running the test manually:")
        print("   python -m pytest tests/test_selenium.py::test_create_new_selenium_wiki_page -v")
    
    except FileNotFoundError:
        print("\n❌ pytest not found. Install it with:")
        print("   pip install pytest")

if __name__ == "__main__":
    run_tests()