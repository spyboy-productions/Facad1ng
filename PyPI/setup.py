from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.md")

if os.path.exists(readme_path):
    with codecs.open(readme_path, encoding="utf-8") as fh:
        long_description = "\n" + fh.read()
else:
    long_description = "The Ultimate URL Masking Tool"

VERSION = '1.0.1'
DESCRIPTION = 'The Ultimate URL Masking Tool'

setup(
    name="Facad1ng",
    version=VERSION,
    author="Spyboy",
    author_email="contact@spyboy.in",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url="https://github.com/spyboy-productions/Facad1ng",
    license="MIT",
    install_requires=['pyshorteners'],
    keywords=['masking', 'phishing', 'url-shortener', 'mask-phishing-url', 'hide-phishing-link', 'url-phishing'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': [
            'Facad1ng = Facad1ng.main:main',
        ],
    },    
)
