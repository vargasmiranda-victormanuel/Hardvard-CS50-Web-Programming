# Wiki Application Testing Guide

## Test Scenario: Create New Selenium Wiki Page

This document describes the comprehensive testing scenario for creating a new wiki page with the title "Selenium" and detailed application description.

### Test Overview

**Test Name:** `test_create_new_selenium_wiki_page`  
**Purpose:** Verify that users can successfully create new wiki pages through the web interface  
**Target URL:** http://127.0.0.1:8000/  
**Test Type:** End-to-end UI automation using Selenium WebDriver  

### Test Steps

1. **Navigate to Homepage**
   - Open browser and navigate to `http://127.0.0.1:8000/`
   - Verify the wiki homepage loads successfully
   - Confirm page title contains "Wiki"

2. **Access New Page Creation**
   - Locate and click "Create New Page" link
   - Verify navigation to new page creation form
   - Confirm page title shows "New Wiki Page"

3. **Enter Page Details**
   - Enter "Selenium" as the page title
   - Fill in comprehensive content about Selenium application including:
     - Overview and description
     - Key components (WebDriver, Grid, IDE)
     - Common use cases
     - Advantages
     - Getting started code example

4. **Submit Form**
   - Click "Create New Page" button
   - Wait for form submission to complete

5. **Verify Page Creation**
   - Confirm redirect to newly created page (`/wiki/Selenium`)
   - Verify page heading displays "Selenium"
   - Check that content is properly rendered from Markdown

6. **Validate Content**
   - Verify key content sections are present:
     - Overview
     - Key Components
     - Common Use Cases
     - Advantages
     - Getting Started
   - Confirm specific keywords appear in content

### Expected Results

- ✅ New wiki page created successfully
- ✅ Page accessible at `/wiki/Selenium` URL
- ✅ Content properly formatted and displayed
- ✅ Page persists and can be accessed later
- ✅ All sections and key information visible

### Test Data

**Page Title:** Selenium

**Page Content:** Comprehensive description including:
- Definition as open-source web automation framework
- Component breakdown (WebDriver, Grid, IDE)
- Use cases (testing, scraping, automation)
- Advantages (open source, cross-platform, multi-browser)
- Python code example

### Prerequisites

1. **Django Server Running**
   ```bash
   python manage.py runserver
   ```
   Server should be accessible at `http://127.0.0.1:8000/`

2. **Chrome Browser & ChromeDriver**
   - Chrome browser installed
   - ChromeDriver installed and in system PATH
   - Compatible versions of Chrome and ChromeDriver

3. **Python Environment**
   - Virtual environment activated
   - Required packages installed:
     ```bash
     pip install selenium pytest django
     ```

### Running the Tests

#### Method 1: Using Test Runner Script
```bash
# Navigate to project directory
cd c:\Users\Vargas\Documents\GitHub\Hardvard-CS50-Web-Programming\Projects\Project1-Wiki\wiki

# Activate virtual environment
wiki_venv\Scripts\activate

# Run the test runner
python run_tests.py
```

#### Method 2: Direct pytest Execution
```bash
# Navigate to project directory and activate environment
cd c:\Users\Vargas\Documents\GitHub\Hardvard-CS50-Web-Programming\Projects\Project1-Wiki\wiki
wiki_venv\Scripts\activate

# Run specific test
python -m pytest tests/test_selenium.py::test_create_new_selenium_wiki_page -v

# Run all tests in the file
python -m pytest tests/test_selenium.py -v
```

#### Method 3: Individual Test Functions
```bash
# Test creating the Selenium page
python -m pytest tests/test_selenium.py::test_create_new_selenium_wiki_page -v

# Test accessing the created page
python -m pytest tests/test_selenium.py::test_verify_selenium_page_exists -v
```

### Additional Test Cases

The test file also includes:

1. **`test_verify_selenium_page_exists`**
   - Verifies the created page persists
   - Tests direct URL access
   - Confirms content remains intact

2. **Original Tests**
   - `test_selenium`: Basic Selenium.dev website test
   - `test_wiki`: Basic wiki homepage test

### Troubleshooting

#### Common Issues

1. **ChromeDriver Not Found**
   ```
   Solution: Download ChromeDriver and add to PATH
   - Download from: https://chromedriver.chromium.org/
   - Place in system PATH or project directory
   ```

2. **Django Server Not Running**
   ```
   Error: Connection refused to 127.0.0.1:8000
   Solution: Start Django development server
   python manage.py runserver
   ```

3. **Import Errors**
   ```
   Error: ModuleNotFoundError: No module named 'selenium'
   Solution: Activate virtual environment and install packages
   wiki_venv\Scripts\activate
   pip install selenium pytest
   ```

4. **Page Already Exists Error**
   ```
   Error: "the wiki page Selenium already exists"
   Solution: Delete existing Selenium.md file from entries/ directory
   or modify test to use a different page name
   ```

### Test Validation Points

The test validates:
- ✅ Form submission functionality
- ✅ Page creation workflow
- ✅ Markdown to HTML conversion
- ✅ URL routing for new pages
- ✅ Content persistence
- ✅ Navigation flow
- ✅ Error handling (duplicate pages)

### Files Modified/Created

1. **`tests/test_selenium.py`** - Main test file with comprehensive test scenarios
2. **`run_tests.py`** - Test runner script with environment checks
3. **`TEST_DOCUMENTATION.md`** - This documentation file

### Future Enhancements

Consider adding tests for:
- Edit existing page functionality
- Delete page capability
- Search functionality
- Random page feature
- Error handling scenarios
- Mobile responsiveness
- Performance testing