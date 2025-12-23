from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="xpowl",
    version="1.0.3",
    author="Morax",
    author_email="bloodlustedx@gmail.com",
    description="https://github.com/ownermorax/xpowl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://xpowl.ru",
    packages=["xpowl"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)