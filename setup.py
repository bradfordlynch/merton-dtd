import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="merton-dtd", # Replace with your own username
    version="0.0.1",
    author="Bradford Lynch",
    author_email="blynch41@gmail.com",
    description="A library for computing a company's distance to default using the Merton model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bradfordlynch/merton-dtd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)