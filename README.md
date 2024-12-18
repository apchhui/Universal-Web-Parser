# Universal Web Parser
You can parse every web-page and partially launch interface

Universal Web Parser: A Guide to Libraries and Methods  
This project is a Universal Web Parser designed to scrape web pages, save the HTML content, and provide additional utility features like cookie handling and troubleshooting. Below, we’ll explore the libraries and methods used in this project, complete with examples to guide your understanding. Python based.  


# Libraries Used  
1. requests  

A powerful HTTP library for sending requests and handling responses.  
Used here to fetch web pages with or without cookies.  
Example:  
```python
import requests

url = "https://example.com"
response = requests.get(url)
if response.status_code == 200:
    print("Page fetched successfully!")
```
2. cloudscraper  

Specifically designed to bypass anti-bot mechanisms like Cloudflare.  
Used in this script as a fallback when requests fails.  
Example:  
```python
import cloudscraper

scraper = cloudscraper.create_scraper()
response = scraper.get("https://example.com")
print(response.content)
```
3. BeautifulSoup (from bs4)  

Parses HTML content to enable easy manipulation and extraction.  
Used here to prettify the HTML content.  
Example:  
```python
from bs4 import BeautifulSoup

html_content = "<html><body><h1>Hello, World!</h1></body></html>"
soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())
```
4. re  

Provides regular expressions for pattern matching.  
Used to validate URLs in the script.  
Example:  
```python
import re

url = "https://example.com"
if re.match(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$', url):
    print("Valid URL")
else:
    print("Invalid URL")
```
5. os  

Provides utilities for interacting with the operating system.  
Used to clear the console and check the operating system type.  
Example:  
```python
import os

os.system('cls' if os.name == 'nt' else 'clear')
```
6. json  

Used to parse and manage JSON files, such as cookies.  
Example:  
```python
import json

with open('cookies.json', 'r') as file:
    cookies = json.load(file)
print(cookies)
```
7. pathlib.Path  

Provides an object-oriented interface for file system paths.  
Used here to handle file paths more effectively.  
Example:  
```python
from pathlib import Path

directory = Path(__file__).parent
print(directory)
```
# Method Overview
is_valid_url(url)

Validates a URL using regex.  
Returns True for valid URLs, otherwise False.  
Example:  

```python
url = "https://example.com"
print(is_valid_url(url))  # Output: True
```
clear_console()

Clears the terminal screen based on the operating system.  
Example:  

```python
clear_console()
```
log(message)

Prints a log message in a standardized format.  
Example:  

```python
log("This is a log message.")
```
load_cookies()

Loads cookies from a cookies.json file.  
Logs an error if the file does not exist.  
Example:  

```python
cookies = load_cookies()
print(cookies)
```
fetch_page(url, cookies=None)

Fetches a webpage using requests or cloudscraper as a fallback.  
Returns prettified HTML content or logs an error if unsuccessful.  
Example:  

```python
content = fetch_page("https://example.com")
print(content)
```
save_to_file(content, filename="index.html")

Saves content to an HTML file.  
Example:  

```python
save_to_file("<html><body>Hello!</body></html>", "output.html")
```
main()

The main driver function that provides a user interface for the script.  
Offers options for parsing websites, viewing instructions, and restarting the session.  

# Usage Examples
Basic Flow:  

1. Run the script.  
2. Choose option 1 to parse a website.  
3. Enter the website URL.  
4. If cookies are required, ensure cookies.json is present in the directory.  
5. The script fetches and saves the page content as index.html.  
6. Optionally launch the saved HTML file in your default browser.  

# Example Cookies File
Example Cookies File  
If a website requires authentication, save cookies in cookies.json:  

```json
{
    "session": "your_session_cookie",
    "auth": "your_auth_cookie"
}
```
# Troubleshooting
Access Denied (403):

Load cookies using a browser extension like Cookie-Editor.  
Save the cookies as a JSON file named cookies.json.  
Invalid URL:  

Ensure the URL is properly formatted (e.g., https://example.com).  
# Example
example.py includes instruments  
Visit: https://pypi.org/project/cloudscraper/
https://requests.readthedocs.io/en/latest/

# Features
