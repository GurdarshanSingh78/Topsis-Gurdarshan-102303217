from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Gurdarshan-102303217",
    version="1.0.5",                         
    author="Gurdarshan Singh",
    author_email="gurdarshan.singh@example.com",
    description="A Python package for TOPSIS method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['topsis_102303217'],           
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis_102303217.topsis:main",  
        ],
    },
)