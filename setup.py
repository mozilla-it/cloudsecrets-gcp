import os
import setuptools
from setuptools import setup, find_packages

setup(
    name="cloudsecrets",
    version="0.2.0",
    description="Python tool for accessing mozilla cloud secrets",
    python_requires=">=3.7",
    author="Mozilla IT Service Engineering",
    author_email="afrank@mozilla.com",
    packages=find_packages(),
    entry_points={"console_scripts": ["cloud-secrets=cloudsecrets.cli:main",],},
    install_requires=["google-cloud-secret-manager", "simplejson"],
    extras_require={"test": ["coverage", "pytest", "nose", "simplejson"],},
    project_urls={"Source": "https://github.com/mozilla-it/cloudsecrets",},
    test_suite="tests.unit",
)
