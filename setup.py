from setuptools import setup
with open("README.MD", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Radha Agarwal'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
      name = SRC_REPO,
    version = '1.0.0',
    author = AUTHOR_NAME,
    author_email= 'radhaagrwal.380@gmail.com',
    description= 'Asmall example package for movie recommendation ',
    long_description= long_description,
    long_description_content_type= 'text/markdown',
    package = [SRC_REPO],
    python_requires= '>=3.7',
    install_requires= LIST_OF_REQUIREMENTS ,
)
  
