import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Similarity",
    version="0.9.9",
    author="Batu Berk Sahin",
    author_email="batuberkshn@gmail.com",
    description="It checks word similarity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/batuberksahin/word-similarity",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)