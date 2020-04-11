### PDFCode

Save code files into PDF format with syntax highlighting. 

It can convert a single code file or all files in a project (folder) using one command. 

___

### 1. Installation

1. Install libraries
``` bash
> pip install pygments
> pip install pdfkit
> pip install file-magic
```

#### MacOS:
``` Bash
########################################
# install wkhtmltopdf
> brew install caskroom/cask/wkhtmltopdf
# or
# brew cask reinstall wkhtmltopdf
########################################


########################################
# install libmagic
> brew install libmagic
########################################
```

___

### 2. Usage
Open a terminal and type the following command:
``` bash
> pdfcode --help 

# usage: pdfcode [-h] [--src SRC] [--dst [DST]] [-l] [-s SIZE] [-S NAME]
#                    [-m MARGIN] [-v]
#
# Convert source files into .pdf with syntax highlighting
#
# optional arguments:
#  -h, --help            show this help message and exit
#  --src SRC             the path of the file/folder
#  --dst [DST]           the path of the saving target folder. Empty will save
#                        to PDFCode_Results/
#  -l, --linenos         include line numbers.
#  -s SIZE, --size SIZE  PDF size. Letter,A1,A2,A3,A4,A5 etc
#  -S NAME, --style NAME
#                        the style name for highlighting.
#  -m MARGIN, --margin MARGIN
#                        the layout margins in inch (default 0.4in).
#  -v, --version         show program's version number and exit
```

Example 
``` Bash
# process single file:
> pdfcode --src ./test/algol.py -s a4 -S colorful 

# process all files in a folder and its subfolders:
> pdfcode --src ./test -s a4 -S colorful 
```

Now, the code supports 36 styles:

|abap|algol|algol_nu|arduino|autumn|borland|
|:---:|:---:|:---:|:---:|:---:|:---:|
|![abap](quiver-image-url/abap.png)|![algol](quiver-image-url/algol.png)|![algol_nu](quiver-image-url/algol_nu.png)|![arduino](quiver-image-url/arduino.png)|![autumn](quiver-image-url/autumn.png)|![borland](quiver-image-url/borland.png)|
|bw|colorful|default|emacs|friendly|fruity|
|![bw](quiver-image-url/bw.png)|![colorful](quiver-image-url/colorful.png)|![default](quiver-image-url/default.png)|![emacs](quiver-image-url/emacs.png)|![friendly](quiver-image-url/friendly.png)|![fruity](quiver-image-url/fruity.png)|
|igor|inkpot|lovelace|manni|monokai|murphy|
|![igor](quiver-image-url/igor.png)|![inkpot](quiver-image-url/inkpot.png)|![lovelace](quiver-image-url/lovelace.png)|![manni](quiver-image-url/manni.png)|![monokai](quiver-image-url/monokai.png)|![murphy](quiver-image-url/murphy.png)|
|native|paraiso-dark|paraiso-light|pastie|perldoc|rainbow_dash|
|![native](quiver-image-url/native.png)|![paraiso-dark](quiver-image-url/paraiso-dark.png)|![paraiso-light](quiver-image-url/paraiso-light.png)|![pastie](quiver-image-url/pastie.png)|![perldoc](quiver-image-url/perldoc.png)|![rainbow_dash](quiver-image-url/rainbow_dash.png)|
|rrt|sas|solarized-dark|solarized-light|stata|stata-dark|
|![rrt](quiver-image-url/rrt.png)|![sas](quiver-image-url/sas.png)|![solarized-dark](quiver-image-url/solarized-dark.png)|![solarized-light](quiver-image-url/solarized-light.png)|![stata](quiver-image-url/stata.png)|![stata-dark](quiver-image-url/stata-dark.png)|
|stata-light|tango|trac|vim|vs|xcode|
|![stata-light](quiver-image-url/stata-light.png)|![tango](quiver-image-url/tango.png)|![trac](quiver-image-url/trac.png)|![vim](quiver-image-url/vim.png)|![vs](quiver-image-url/vs.png)|![xcode](quiver-image-url/xcode.png)|

___

### 3. Acknowledgements
- This code is modified from [code2pdf](https://pypi.org/project/Code2pdf/). I am holding this repository because the [code2pdf](https://pypi.org/project/Code2pdf/) had the following problems at the moment when I was trying to use.
    1. The generated PDF files did not have syntax highlighting (all black-white).
    2. The command only supported to process a single file. Sometime, I want to process multiple code files.
    3. The **code2pdf** used python2 and pyqt4. They were not easy to setup on my machine (especially pyqt4).
- This code is implemented based on libraries like pdfkit, magic, pygments, etc.
I appreciate the contributations of all of these authors.

___

