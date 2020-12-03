import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="n2yoasync",
    version="0.0.5",
    author="Tim Empringham",
    author_email="tim.empringham@live.ca",
    description="Async Python wrapper for the N2YO API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djtimca/n2yo-api",
    packages=setuptools.find_packages(),
    keywords=['N2YO','Satellite'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)