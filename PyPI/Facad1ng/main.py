#!/usr/bin/env python

import argparse
import pyshorteners
from urllib.parse import urlparse

twitter_url = 'https://spyboy.in/twitter'
discord = 'https://spyboy.in/Discord'
website = 'https://spyboy.in/'
blog = 'https://spyboy.blog/'
github = 'https://github.com/spyboy-productions/Facad1ng'

VERSION = '0.0.18'

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

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
    """
    prints the program banners
    """
    print(f'{R}{banner}{W}\n')
    print(f'{G}╰➤ {C}Version      : {W}{VERSION}')
    print(f'{G}╰➤ {C}Creator      : {W}Spyboy')
    print(f'{G}╰➤ {C}Twitter      : {W}{twitter_url}')
    print(f'{G}╰➤ {C}Discord      : {W}{discord}')
    print(f'{G}╰➤ {C}Website      : {W}{website}')
    print(f'{G}╰➤ {C}Blog         : {W}{blog}')
    print(f'{G}╰➤ {C}Github       : {W}{github}\n')


def main():
    print_banners()
    print(f"{Y}[~] {G}Please Wait, It Is Masking & Shortening Your Link.")

    parser = argparse.ArgumentParser(description='Facad1ng: The Ultimate URL Masking Tool')
    parser.add_argument('original_url', help='The original URL (e.g., https://www.example.com)')
    parser.add_argument('custom_domain', help='Your custom domain (e.g., example.com)')
    parser.add_argument('phishing_keywords', help='Phishing keywords (e.g., free-stuff-login)')
    args = parser.parse_args()

    original_url = args.original_url
    custom_domain = args.custom_domain
    phishing_keywords = args.phishing_keywords

    # Input validation functions
    def validate_web_url(url):
        if not url.startswith("https://") or url.endswith("/"):
            raise ValueError("Invalid URL format. It should start with 'https://' and not end with '/'.")

    def validate_custom_domain(domain):
        if "://" in domain or "/" in domain:
            raise ValueError("Invalid custom domain. It should be just the domain name without 'http://' or '/'.")

    def format_phish_keywords(keywords):
        return "-".join(keywords.split())

    try:
        validate_web_url(original_url)
        validate_custom_domain(custom_domain)
        phishing_keywords = format_phish_keywords(phishing_keywords)
        if " " in phishing_keywords:
            raise ValueError("Phishing keywords should not contain spaces. Use '-' to separate them.")
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

    # Prepare the data for the request
    data = {
        'url': original_url,
        'shorturl': '',
    }

    # Shorten the original URL with multiple URL shorteners
    shorteners = [
        pyshorteners.Shortener().tinyurl,
        pyshorteners.Shortener().osdb,
        pyshorteners.Shortener().dagd,
        pyshorteners.Shortener().clckru,
    ]
    short_urls = [shortener.short(original_url) for shortener in shorteners]

    # Mask the URLs with custom domain and phishing keywords
    def mask_url(domain, keyword, url):
        parsed_url = urlparse(url)
        return f"{parsed_url.scheme}://{domain}-{keyword}@{parsed_url.netloc}{parsed_url.path}"

    # Print the results
    print(f"\n{Y}Original URL:{W}", original_url, "\n")
    print(f"[~] Masked URL (using multiple shorteners):")
    for i, short_url in enumerate(short_urls):
        masked_url = mask_url(custom_domain, phishing_keywords, short_url)
        print(f"╰➤ Shortener {i + 1}: {masked_url}")


if __name__ == '__main__':
    main()
