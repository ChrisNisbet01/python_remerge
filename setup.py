import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Chris Nisbet",
    version="1.0.0",
    author="Unknown",
    description="Deep merge two dictionaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChrisNisbet01/python_remerge",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: None",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
