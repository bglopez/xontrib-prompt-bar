#!/usr/bin/env python
from setuptools import setup

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setup(
    name='xontrib-theme-bar',
    version='0.0.1',
    license='BSD',
    author='anki',
    author_email='author@example.com',
    description="The bar theme for xonsh shell.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=[
        'xonsh',
    ],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    url='https://github.com/anki-code/xontrib-theme-bar',
    project_urls={
        "Documentation": "https://github.com/anki-code/xontrib-theme-bar/blob/master/README.md",
        "Code": "https://github.com/anki-code/xontrib-theme-bar",
        "Issue tracker": "https://github.com/anki-code/xontrib-theme-bar/issues",
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Unix Shell",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: BSD License"
    ]
)