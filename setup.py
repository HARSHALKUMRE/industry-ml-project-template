from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
SRC_REPO = "src"
REPO_NAME = "industry-ml-project-template"
AUTHOR_USER_NAME = "HARSHALKUMRE"
LIST_OF_REQUIREMENTS = []    
VERSION = "0.0.2"
    
setup(
    name = SRC_REPO,
    version = VERSION,
    author = AUTHOR_USER_NAME,
    description = "This is our first release",
    long_description = long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    author_email = "kumreharshalkumar@gmail.com",
    packages = [SRC_REPO], 
    python_requires = ">=3.8",
    install_requires = LIST_OF_REQUIREMENTS
)