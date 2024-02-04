import setuptools
from setuptools import Bug
with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ ="0.0.0"

REPO_NAME = "QuickSum - Text Summariser"
AUTHOR_USERNAME = "ornithophiliac"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "work.mukul24@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="QuickSum - Text Summariser",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir=("": "src"),
    packages=setuptools.findpackages(where="src"),
)