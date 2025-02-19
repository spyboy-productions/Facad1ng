import sys
import time
import pyshorteners
from urllib.parse import urlparse
import re

def show_loading_screen():
    """Display an animated loading screen with varied messages"""
    frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    for _ in range(10):  # Loop for a few seconds
        for frame in frames:
            sys.stdout.write(f"\r{C}Processing... {frame}{W}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r\033[K")  # Clear line after animation

twitter_url = 'https://spyboy.in/twitter'
discord = 'https://spyboy.in/Discord'
website = 'https://spyboy.in/'
blog = 'https://spyboy.blog/'
github = 'https://github.com/spyboy-productions/Facad1ng'

VERSION = '1.0.1'

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

def mask_url(domain, keyword, url):
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{domain}-{keyword}@{parsed_url.netloc}{parsed_url.path}"

try:
    while True:
        web_url = input(f"{G}Enter the original link {W}(ex: https://www.ngrok.com): {W}")
        if re.match(r'^(https?://)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(:\d{1,5})?(/.*)?$', web_url):
            break
        print("Invalid URL format. Please provide a valid web URL.")

    while True:
        custom_domain = input(f"\n{Y}Enter your custom domain {W}(ex: gmail.com): {W}")
        if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', custom_domain):
            break
        print("Invalid custom domain. Please provide a valid domain name.")

    while True:
        phish = input(f"\n{Y}Enter phishing keywords {W}(ex: account, login): {W}")
        if " " not in phish and len(phish) <= 15:
            break
        print("Phishing keywords should not contain spaces and must be under 15 characters.")

    show_loading_screen()
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

    print(f"\n{R}Original URL:{W}", web_url, "\n")
    print(f"{G}[~] {G}Masked URL {Y}(using multiple shorteners):{W}")
    for i, short_url in enumerate(short_urls):
        masked_url = mask_url(custom_domain, phish, short_url)
        print(f"{G}╰➤ {C}Shortener {W} {i + 1}: {masked_url}")

except Exception as e:
    print(f"{R}An error occurred: {W}{str(e)}")
