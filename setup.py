import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blackcurve_api",
    version="0.0.1",
    author="BlackCurve LTD.",
    author_email="george.rowberry@blackcurve.com",
    description="A Easy to use interface for BlackCurve's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://blackcurve.io/api/docs/index.html",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)