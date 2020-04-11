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
|![abap](./images/abap.png)|![algol](./images/algol.png)|![algol_nu](./images/algol_nu.png)|![arduino](./images/arduino.png)|![autumn](./images/autumn.png)|![borland](./images/borland.png)|
|bw|colorful|default|emacs|friendly|fruity|
|![bw](./images/bw.png)|![colorful](./images/colorful.png)|![default](./images/default.png)|![emacs](./images/emacs.png)|![friendly](./images/friendly.png)|![fruity](./images/fruity.png)|
|igor|inkpot|lovelace|manni|monokai|murphy|
|![igor](./images/igor.png)|![inkpot](./images/inkpot.png)|![lovelace](./images/lovelace.png)|![manni](./images/manni.png)|![monokai](./images/monokai.png)|![murphy](./images/murphy.png)|
|native|paraiso-dark|paraiso-light|pastie|perldoc|rainbow_dash|
|![native](./images/native.png)|![paraiso-dark](./images/paraiso-dark.png)|![paraiso-light](./images/paraiso-light.png)|![pastie](./images/pastie.png)|![perldoc](./images/perldoc.png)|![rainbow_dash](./images/rainbow_dash.png)|
|rrt|sas|solarized-dark|solarized-light|stata|stata-dark|
|![rrt](./images/rrt.png)|![sas](./images/sas.png)|![solarized-dark](./images/solarized-dark.png)|![solarized-light](./images/solarized-light.png)|![stata](./images/stata.png)|![stata-dark](./images/stata-dark.png)|
|stata-light|tango|trac|vim|vs|xcode|
|![stata-light](./images/stata-light.png)|![tango](./images/tango.png)|![trac](./images/trac.png)|![vim](./images/vim.png)|![vs](./images/vs.png)|![xcode](./images/xcode.png)|

___

### 3. Acknowledgements
- This code is modified from [code2pdf](https://pypi.org/project/Code2pdf/). I am holding this repository because the [code2pdf](https://pypi.org/project/Code2pdf/) had the following problems at the moment when I was trying to use.
    1. The generated PDF files did not have syntax highlighting (all black-white).
    2. The command only supported to process a single file. Sometime, I want to process multiple code files.
    3. The **code2pdf** used python2 and pyqt4. They were not easy to setup on my machine (especially pyqt4).
- This code is implemented based on libraries like pdfkit, magic, pygments, etc.
I appreciate the contributations of all of these authors.

___

