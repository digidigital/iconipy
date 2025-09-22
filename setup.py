#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="iconipy",
    version="0.5.1",
    author="Björn Seipel",
    author_email="support@digidigital.de",
    description="Create icons for user interfaces directly from your Python code.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/digidigital/iconipy",
    package_dir={"": "src"},
    packages=find_packages(where="src"),  
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pillow>=10.0.0",
    ],
    entry_points={
        "pyinstaller40": [
            "hook-dirs = iconipy.__pyinstaller:get_hook_dirs",
        ],
    },
)
