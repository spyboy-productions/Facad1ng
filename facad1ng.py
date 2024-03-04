#Facad1ng: The Ultimate URL Masking Tool

import pyshorteners
from urllib.parse import urlparse
import re

twitter_url = 'https://spyboy.in/twitter'
discord = 'https://spyboy.in/Discord'
website = 'https://spyboy.in/'
blog = 'https://spyboy.blog/'
github = 'https://github.com/spyboy-productions/Facad1ng'

VERSION = '1.0.0'

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

################
print_banners()

# Initialize the URL shorteners
s = pyshorteners.Shortener()

# Add the additional URL shortener to the list
shorteners = [
    s.tinyurl,
    s.dagd,
    s.clckru,
    s.osdb,
]

# Input validation functions
def validate_web_url(url):
    url_pattern = re.compile(
    r'^(https?://)'  # starts with 'https://'
    r'([a-zA-Z0-9-]+\.)*'  # optional subdomains
    r'([a-zA-Z]{2,})'  # domain
    r'(:\d{1,5})?'  # optional port
    r'(/.*)?$')

    if not url_pattern.match(url):
        raise ValueError("Invalid URL format. Please provide a valid web URL.")

def validate_custom_domain(domain):
    domain_pattern = re.compile(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    if not domain_pattern.match(domain):
        raise ValueError("Invalid custom domain. Please provide a valid domain name.")

def format_phish_keywords(keywords):
    max_length = 15
    if not isinstance(keywords, str):
        raise TypeError("Input must be a string.")

    if " " in phish:
        raise TypeError("Phishing keywords should not contain spaces. Use '-' to separate them.")

    if len(keywords) > max_length:
        raise ValueError("Input string exceeds the maximum allowed length.")

    return "-".join(keywords.split())

# Input from the user with validation
try:
    while True:
        web_url = input(f"{G}Enter the original link {W}(ex: https://www.ngrok.com): {W}")
        try:
            validate_web_url(web_url)
            break
        except ValueError as e:
            print(e)

    while True:
        custom_domain = input(f"\n{Y}Enter your custom domain {W}(ex: gmail.com): {W}")
        try:
            validate_custom_domain(custom_domain)
            break
        except ValueError as e:
            print(e)

    while True:
        phish = input(f"\n{C}Enter phishing keywords {W}(ex: free-stuff, login): {W}")
        try:
            phish = format_phish_keywords(phish)
            break
        except TypeError as e:
            print(e)

    # Prepare the data for the request
    data = {
        'url': web_url,
        'shorturl': '',
    }

    # Shorten the original URL with multiple URL shorteners
    short_urls = []
    for i, shortener in enumerate(shorteners):
        try:
            short_url = shortener.short(web_url)
            short_urls.append(short_url)
        except pyshorteners.exceptions.ShorteningErrorException as e:
            print(f"{R}Error shortening URL with Shortener {i + 1}: {W}{str(e)}")
            continue
        except Exception as e:
            print(f"{R}An unexpected error occurred with Shortener {i + 1}: {W}{str(e)}")
            continue

    # Mask the URLs with custom domain and phishing keywords
    def mask_url(domain, keyword, url):
        # Use urlparse to properly split the URL
        parsed_url = urlparse(url)

        # Reconstruct the URL with the custom domain and phishing keyword
        return f"{parsed_url.scheme}://{domain}-{keyword}@{parsed_url.netloc}{parsed_url.path}"

    # Print the results
    print(f"\n{Y}Original URL:{W}", web_url, "\n")
    print(f"{G}[~] {R}Masked URL (using multiple shorteners):{W}")
    for i, short_url in enumerate(short_urls):
        masked_url = mask_url(custom_domain, phish, short_url)
        print(f"{G}╰➤ {C}Shortener {W} {i + 1}: {masked_url}")


except Exception as e:
    print(f"{R}An error occurred: {W}{str(e)}")
