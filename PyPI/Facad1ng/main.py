#!/usr/bin/env python

import argparse
import pyshorteners
from urllib.parse import urlparse
import re
import sys
import time

# Author and project details
twitter_url = 'https://spyboy.in/twitter'
discord = 'https://spyboy.in/Discord'
website = 'https://spyboy.in/'
blog = 'https://spyboy.blog/'
github = 'https://github.com/spyboy-productions/Facad1ng'

VERSION = '1.0.1'

# Terminal colors
R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

# Banner
banner = r'''
███████╗ █████╗  ██████╗ █████╗ ██████╗  ██╗███╗   ██╗ ██████╗ 
██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗███║████╗  ██║██╔════╝ 
█████╗  ███████║██║     ███████║██║  ██║╚██║██╔██╗ ██║██║  ███╗
██╔══╝  ██╔══██║██║     ██╔══██║██║  ██║ ██║██║╚██╗██║██║   ██║
██║     ██║  ██║╚██████╗██║  ██║██████╔╝ ██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
    The Ultimate URL Masking Tool
'''

def print_banners():
    """ Prints the program banners """
    print(f'{R}{banner}{W}\n')
    print(f'{G}╰➤ {C}Version      : {W}{VERSION}')
    print(f'{G}╰➤ {C}Creator      : {W}Spyboy')
    print(f'{G}╰➤ {C}Twitter      : {W}{twitter_url}')
    print(f'{G}╰➤ {C}Discord      : {W}{discord}')
    print(f'{G}╰➤ {C}Website      : {W}{website}')
    print(f'{G}╰➤ {C}Blog         : {W}{blog}')
    print(f'{G}╰➤ {C}Github       : {W}{github}\n')

def show_loading_screen():
    """Display an animated loading screen with varied messages"""
    frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    for _ in range(10):  # Loop for a few seconds
        for frame in frames:
            sys.stdout.write(f"\r{Y}Processing... {frame}{W}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r\033[K")  # Clear line after animation

def validate_web_url(url):
    url_pattern = re.compile(r'^(https?://)([a-zA-Z0-9-]+\.)*([a-zA-Z]{2,})(:\d{1,5})?(/.*)?$')
    if not url_pattern.match(url):
        raise ValueError("Invalid URL format. Please provide a valid web URL.")

def validate_custom_domain(domain):
    domain_pattern = re.compile(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not domain_pattern.match(domain):
        raise ValueError("Invalid custom domain. Please provide a valid domain name.")

def format_phish_keywords(keywords):
    if " " in keywords:
        raise ValueError("Phishing keywords should not contain spaces. Use '-' to separate them.")
    if len(keywords) > 15:
        raise ValueError("Phishing keywords should not exceed 15 characters.")
    return "-".join(keywords.split())

def mask_url(domain, keyword, url):
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{domain}-{keyword}@{parsed_url.netloc}{parsed_url.path}"

def main():
    print_banners()
    parser = argparse.ArgumentParser(description='Facad1ng: The Ultimate URL Masking Tool')
    parser.add_argument('original_url', nargs='?', help='The original URL (e.g., https://www.example.com)')
    parser.add_argument('custom_domain', nargs='?', help='Your custom domain (e.g., example.com)')
    parser.add_argument('phishing_keywords', nargs='?', help='Phishing keywords (e.g., free-stuff-login)')

    args = parser.parse_args()

    if not args.original_url or not args.custom_domain or not args.phishing_keywords:
        print(f"{R}Error: {W}Missing required arguments!\n")
        print("Example Usage:")
        print(f"{G}python main.py https://www.google.com example.com free-gift{W}\n")
        parser.print_help()
        exit(1)

    try:
        validate_web_url(args.original_url)
        validate_custom_domain(args.custom_domain)
        phishing_keywords = format_phish_keywords(args.phishing_keywords)
    except ValueError as e:
        print(f"{R}Error: {W}{str(e)}")
        exit(1)
    
    print(f"{Y}Shortening URL...{W}")
    show_loading_screen()
    
    shorteners = [
        pyshorteners.Shortener().tinyurl,
        pyshorteners.Shortener().dagd,
        pyshorteners.Shortener().clckru,
        pyshorteners.Shortener().osdb,
    ]
    
    short_urls = []
    for i, shortener in enumerate(shorteners):
        try:
            short_urls.append(shortener.short(args.original_url))
        except Exception as e:
            print(f"{R}Error with Shortener {i + 1}: {W}{str(e)}")

    print(f"\n{Y}Original URL:{W}", args.original_url, "\n")
    print(f"{G}[~] {R}Masked URL (using multiple shorteners):{W}")
    for i, short_url in enumerate(short_urls):
        print(f"{G}╰➤ {C}Shortener {W} {i + 1}: {mask_url(args.custom_domain, phishing_keywords, short_url)}")

if __name__ == '__main__':
    main()
