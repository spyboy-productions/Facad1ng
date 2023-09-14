from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.18'
DESCRIPTION = 'The Ultimate URL Masking Tool'

# Setting up
setup(
    name="Facad1ng",
    version=VERSION,
    author="Spyboy",
    author_email="spyboyblog@gmail.com",
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url="https://github.com/spyboy-productions/Facad1ng",
    Homepage="https://github.com/spyboy-productions/Facad1ng",
    Repository="https://github.com/spyboy-productions/Facad1ng",
    license="MIT",
    install_requires=['pyshorteners', 'argparse'],
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