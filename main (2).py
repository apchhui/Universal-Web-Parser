import requests
import cloudscraper
from bs4 import BeautifulSoup
import re
import os
import json
from pathlib import Path
import subprocess

directory = Path(__file__).parent
file_directory = directory
file_name = "index.html"
file_path = str(directory / file_name)
file_path = file_path.replace("/", "\\")


# Define your headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}


def is_valid_url(url):
    try:
        result = re.match(
            r'^(https?|ftp)://[^\s/$.?#].[^\s]*$', url
        )
        return result is not None
    except ValueError:
        return False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def log(message):
    print(f"[INFO] {message}")

def load_cookies():
    try:
        with open('cookies.json', 'r') as e:
            return json.load(e)
    except FileNotFoundError:
        log('Cookies file not found. Use instructions to load your cookies.')
        print('Press Enter to continue...')
        input()
        return {}

def fetch_page(url, cookies=None):
    try:
        if cookies:
            response = requests.get(url, cookies=cookies)
        else:                                               # headers optionally
            response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser').prettify()
        else:
            log(f"Failed to fetch website. Status code: {response.status_code}")
            log('Trying to get access with cloudscraper...')
            if cookies:
                response = cloudscraper.create_scraper().get(url, cookies=cookies)
            else:
                response = cloudscraper.create_scraper().get(url)
            if response.status_code == 200:
                return BeautifulSoup(response.content, 'html.parser').prettify()
            else:
                if response.status_code == 403:
                    log('Access Denied, try to load cookies and/or add headers')
                else:
                    log(f"Failed to fetch website. Status code: {response.status_code}")
                print('Press Enter to continue')
                input()
                return None
    except Exception as e:
        log(f"An error occurred")
        return None

def save_to_file(content, filename="index.html"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        log(f"HTML content saved as {filename}")
    except Exception as e:
        log(f"Error saving file\nTry to create file")

def main():
    clear_console()
    print(file_path)
    print('Choose a number from the list below:')
    print('1. Parse a website with default settings')
    print('2. Instructions')
    choice = input()

    if choice == '1':
        url = input('Input the URL of the website: ')
        if is_valid_url(url):
            cookie_flag = input('Use cookies (y/n): ')
            cookies = ''
            if cookie_flag.lower() == 'y':
                cookies = load_cookies()
            if cookies == {}:
                print('Cookies are Invalid!')
                print('Press Enter to continue...')
                input()
                main()
            clear_console()
            log('URL is valid! Starting...')
            result = fetch_page(url, cookies)

            if result:
                save_to_file(result)
                log('Successfully parsed the website')
                launch = input('Would you like to launch parsed code? (y/n)').lower()
                if launch == 'y':
                    subprocess.Popen(['start', file_path], shell=True)
                start = input('Start session again? (y/n): ').lower()
                if start == 'y':
                    main()
                else:
                    return
            else:
                clear_console()
                log('Failed to parse the website')
                input("Press Enter to continue...")
                main()
        else:
            log('Invalid URL')
            input("Press Enter to continue...")
            main()

    elif choice == '2':
        clear_console()
        print('Full manual there: https://github.com/apchhui/Universal-Web-Parser')
        instr = 'Choose the number from the list below\n1. Troubleshooting\n2. Info\n3. Detailed info'
        print(instr)
        selection = input('Your choice: ')
        if selection == '1':
            print('If you failed to parse website, try to load your cookies.\nDownload Cookie-Editor in your browser, export as json,\nСreate file "cookies.json" and paste your cookies.')
        elif selection == '2':
            print('Made by @apchhu1(Telegram)')
        elif selection == '3':
            print('Detailed information is available at the provided link.')
        else:
            print('Enter a valid number from the list')
        input("Press Enter to continue...")
        main()

    else:
        log('Invalid input, enter key 1 or 2')
        input("Press Enter to continue...")
        main()

if __name__ == '__main__':
    main()