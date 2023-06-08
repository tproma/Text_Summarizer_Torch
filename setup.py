import setuptools

with open("README.md", "r", encoding="utf-8") as f:
  long_description = f.read()
  
  
__version__ = "0.0.0"

REPO_NAME = "Text_Summarizer"
AUTHOR_USER_NAME = "Proma"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "tanjinaproma@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    deescription = "Pyhton package for NLP app",
    long_description = long_description,
    long_description_content = "text/markdown",
    
  
    package_dir = {"": "src"},
  
)