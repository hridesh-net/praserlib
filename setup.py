import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UniParse",
    version="0.1.0",
    author="Hridesh",
    author_email="hridesh.khandal@gmail.com",
    description="A library to parse PDF, DOCX, and TXT files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "PyMuPDF>=1.18.0",
        "python-docx>=0.8.10",
    ]
)