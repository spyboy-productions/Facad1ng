#Facad1ng: The Ultimate URL Masking Tool

import pyshorteners
from urllib.parse import urlparse

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
    s.osdb,
    s.dagd,
    s.clckru,
]

# Input validation functions
def validate_web_url(url):
    if not url.startswith("https://") or url.endswith("/"):
        raise ValueError("Invalid URL format. It should start with 'https://' and not end with '/'.")

def validate_custom_domain(domain):
    if "://" in domain or "/" in domain:
        raise ValueError("Invalid custom domain. It should be just the domain name without 'http://' or '/'.")

def format_phish_keywords(keywords):
    return "-".join(keywords.split())

# Input from the user with validation
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
    phish = format_phish_keywords(phish)
    if " " not in phish:
        break
    else:
        print("Phishing keywords should not contain spaces. Use '-' to separate them.")

# Prepare the data for the request
data = {
    'url': web_url,
    'shorturl': '',
}

# Shorten the original URL with multiple URL shorteners
short_urls = [shortener.short(web_url) for shortener in shorteners]

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
