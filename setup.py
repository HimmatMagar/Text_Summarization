import setuptools

__version__ = '0.0.0.0'

REPO_NAME = "Text_Summarization"
AUTHOR_USER_NAME = "HimmatMagar"
SRC_REPO = "textSummerize"
AUTHOR_EMAIL = "himmatmagar007@gmail.com"

setuptools.setup(
      name="textSummerize",
      version=__version__,
      author=AUTHOR_USER_NAME,
      author_email=AUTHOR_EMAIL,
      description="End to End Deep Learning implementation or Fine tune BART for Text Summarization",
      long_description_content_type='text/markdown',
      url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
      project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
      },
      package_dir={"": "src"},
      packages=setuptools.find_packages(where='src')
)