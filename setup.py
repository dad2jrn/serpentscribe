from setuptools import setup, find_packages

setup(
    name="serpentscribe",
    version="0.3",
    packages=find_packages(),
    license="MIT",
    description="A fast, simple, and yet powerful Python logging library designed to make function call logging effortless. No longer do you have to instantiate logging multiple times within a function or class. This module provides a simple decorator to automatically log the details of function calls, including arguments and return values to stdout and optionally to a JSON file specified.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ron Meck",
    author_email="dad2jrn@gmail.com",
    url="https://github.com/dad2jrn/serpentscribe",
    install_requires=[
        # Dependencies, if any
    ],
)
