"""Setup script for python-encrypting package."""

from setuptools import setup, find_packages

setup(
    name="python-encrypting",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
)
