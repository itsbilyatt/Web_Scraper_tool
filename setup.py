from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='Webscraper',
    version='0.0.1',
    description='A tool which will help to reduce time for scrapping data.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/itsbilyatt/Web_Scraper_tool',
    author='prajyot birajdar',
    author_email='prajyotbirajadar1998@gmail.com',
    packages=['webscraper'],
    install_requires=[
        'bs4',
        'requests',
    ],
    classifiers=[
        'Development Status :: Alpha',
        'Intended Audience :: Science/Research/data scientis/data miner',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
