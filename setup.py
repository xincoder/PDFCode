import setuptools
from PDFCode.PDFCode import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

# with open("./PDFCode/version.txt", "r") as fh:
    # version = fh.read()

setuptools.setup(
    name="PDFCode", # Replace with your own username
    version=__version__, 
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
        'markdown',
        'pyhtml2pdf',
      ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)