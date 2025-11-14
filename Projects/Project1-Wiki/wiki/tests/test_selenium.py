from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


def test_wiki():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/")
    assert driver.title == "Encyclopedia"
    driver.quit()


def test_create_new_selenium_wiki_page():
    """
    Test scenario: Create a new wiki page with title 'Selenium' and application description
    
    Steps:
    1. Navigate to the wiki homepage
    2. Click on "Create New Page" link
    3. Enter title as "Selenium"
    4. Enter detailed description about Selenium application
    5. Submit the form
    6. Verify the page was created successfully
    7. Verify the content is displayed correctly
    """
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Step 1: Navigate to wiki homepage
        driver.get("http://127.0.0.1:8000/")
        assert "Encyclopedia" in driver.title
        
        # Step 2: Click on "Create New Page" link
        create_new_page_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Create New Page"))
        )
        create_new_page_link.click()
        
        # Verify we're on the new page creation form
        assert "New Wiki Page" in driver.title
        
        # Step 3: Enter title as "Selenium"
        title_input = driver.find_element(By.NAME, "title")
        title_input.clear()
        title_input.send_keys("Selenium")
        
        # Step 4: Enter detailed description about Selenium application
        selenium_description = """# Selenium

**Selenium** is a powerful open-source framework for automating web browsers and testing web applications.

## Overview

Selenium provides a suite of tools for web automation and testing across different browsers and platforms. It supports multiple programming languages including Python, Java, C#, Ruby, and JavaScript.

## Key Components

### Selenium WebDriver
- Direct communication with web browsers
- Supports Chrome, Firefox, Safari, Edge, and more
- Provides APIs for interacting with web elements

### Selenium Grid
- Enables parallel test execution
- Supports distributed testing across multiple machines
- Scales test execution efficiently

### Selenium IDE
- Record and playback tool for creating tests
- Browser extension for Chrome and Firefox
- Great for beginners and quick test creation

## Common Use Cases

1. **Automated Testing**: Create comprehensive test suites for web applications
2. **Web Scraping**: Extract data from websites programmatically
3. **Browser Automation**: Automate repetitive web tasks
4. **Cross-browser Testing**: Ensure compatibility across different browsers

## Advantages

- **Open Source**: Free to use with active community support
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Multi-browser Support**: Test across different browsers
- **Language Flexibility**: Choose from multiple programming languages
- **Extensive Documentation**: Well-documented with numerous examples

## Getting Started

```python
from selenium import webdriver

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://example.com")

# Find elements and interact with them
element = driver.find_element(By.ID, "example-id")
element.click()

# Close the browser
driver.quit()
```

Selenium is an essential tool for modern web development and quality assurance teams."""
        
        content_textarea = driver.find_element(By.NAME, "md_content")
        content_textarea.clear()
        content_textarea.send_keys(selenium_description)
        
        # Step 5: Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        submit_button.click()
        
        # Step 6: Verify the page was created successfully
        # Wait for page to load and check if we're redirected to the new page
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        
        # Verify we're on the Selenium page
        current_url = driver.current_url
        assert "wiki/Selenium" in current_url
        
        # Step 7: Verify the content is displayed correctly
        page_heading = driver.find_element(By.TAG_NAME, "h1")
        assert "Selenium" in page_heading.text
        
        # Check if the content contains key elements from our description
        page_content = driver.find_element(By.TAG_NAME, "body").text
        assert "open-source framework" in page_content
        assert "web browsers" in page_content
        assert "WebDriver" in page_content
        assert "Cross-platform" in page_content
        
        # Verify that specific sections are present
        assert "Overview" in page_content
        assert "Key Components" in page_content
        assert "Common Use Cases" in page_content
        assert "Advantages" in page_content
        
        print("✅ Test passed: Selenium wiki page created successfully!")
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        # Take a screenshot for debugging
        driver.save_screenshot("test_failure_screenshot.png")
        raise e
        
    finally:
        # Always close the browser
        driver.quit()


def test_verify_selenium_page_exists():
    """
    Additional test to verify that the Selenium page can be accessed directly
    and that it persists after creation
    """
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Navigate directly to the Selenium wiki page
        driver.get("http://127.0.0.1:8000/wiki/Selenium")
        
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        
        # Verify the page loads without error
        assert "Selenium" in driver.title or "Wiki" in driver.title
        
        # Check that the page content is displayed
        page_heading = driver.find_element(By.TAG_NAME, "h1")
        assert "Selenium" in page_heading.text
        
        # Verify key content is still present
        page_content = driver.find_element(By.TAG_NAME, "body").text
        assert "open-source framework" in page_content
        
        print("✅ Test passed: Selenium wiki page is accessible and persistent!")
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        driver.save_screenshot("verify_page_failure_screenshot.png")
        raise e
        
    finally:
        driver.quit()