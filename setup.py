import setuptools

with open("README_pypi.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PDFCode", # Replace with your own username
    version="0.1.0",
    author="xincoder",
    author_email="xincoder@gmail.com",
    description="Save code files into PDF format with syntax highlighting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xincoder/PDFCode",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['pdfcode=PDFCode:main'],
    },
    install_requires=[
        'pygments',
        'pdfkit',
        'file-magic',
      ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)