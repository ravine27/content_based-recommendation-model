from setuptools import setup

AUTHOR_NAME = 'Radha Agarwal'
SRC_REPO = 'movie-recommendation'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='1.0.0',
    author=AUTHOR_NAME,
    author_email='radhaagrwal.380@gmail.com',
    description='A movie recommendation system',
    long_description="A movie recommendation system using machine learning",
    long_description_content_type='text/markdown',
    packages=['src'],
    package_dir={'src': 'src'},
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS,
)