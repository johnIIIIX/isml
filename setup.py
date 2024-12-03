
from setuptools import setup, find_packages

setup(
    name="isml_library",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn"
    ],
)