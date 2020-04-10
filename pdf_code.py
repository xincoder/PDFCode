#! /usr/bin/env python
import argparse
import logging
import os
import sys
import pdfkit

import pygments
from pygments import lexers, formatters, styles

# try:
#     import pygments
#     from pygments import lexers, formatters, styles
# except ImportError as ex:
#     logging.warning('\nCould not import the required "pygments" module:\n{}'.format(ex))
#     sys.exit(1)

__version__ = '1.0.0'

class Code2pdf:
    """
        Convert a source file into a pdf with syntax highlighting.
    """
    def __init__(self, ifile=None, ofile=None, size="A4", margin=0.4):
        if not ifile:
            raise Exception("input file is required")
        self.input_file = ifile
        self.pdf_file = ofile or "{}.pdf".format(ifile.split('.')[0])
        self.size = size
        self.margin = '{}in'.format(margin)

    def highlight_file(self, linenos=True, style='default'):
        """ Highlight the input file, and return HTML as a string. """
        try:
            lexer = lexers.get_lexer_for_filename(self.input_file)
        except pygments.util.ClassNotFound:
            # Try guessing the lexer (file type) later.
            lexer = None

        try:
            formatter = formatters.HtmlFormatter(
                linenos=linenos,
                style=style,
                full=True)
        except pygments.util.ClassNotFound:
            logging.error("\nInvalid style name: {}\nExpecting one of:\n \
                {}".format(style, "\n    ".join(sorted(styles.STYLE_MAP))))
            sys.exit(1)

        try:
            with open(self.input_file, "r") as f:
                content = f.read()
                try:
                    lexer = lexer or lexers.guess_lexer(content)
                except pygments.util.ClassNotFound:
                    lexer = lexers.get_lexer_by_name("text")
        except EnvironmentError as exread:
            fmt = "\nUnable to read file: {}\n{}"
            logging.error(fmt.format(self.input_file, exread))
            sys.exit(2)

        return pygments.highlight(content, lexer, formatter)

    def save_pdf(self, linenos=True, style="default"):
        text = self.highlight_file(linenos=linenos, style=style)
        options = {
            'page-size': self.size.lower(),
            'margin-top': self.margin,
            'margin-right': self.margin,
            'margin-bottom': self.margin,
            'margin-left': self.margin,
            'encoding': "UTF-8",
            'custom-header' : [
                ('Accept-Encoding', 'gzip')
            ]
        }
        pdfkit.from_string(input=text, output_path=self.pdf_file, cover='', options=options)
        print('PDF created at {}'.format(self.pdf_file))


def get_output_file(inputname, outputname=None):
    """ If the output name is set, then return it.
        Otherwise, build an output name using the current directory,
        replacing the input name's extension.
    """
    if outputname:
        return outputname
    inputbase = os.path.split(inputname)[-1]
    outputbase = "{}.pdf".format(os.path.splitext(inputbase)[0])
    return os.path.join(os.getcwd(), outputbase)


def parse_arg():
    parser = argparse.ArgumentParser(
        description=(
            "Convert given source code into .pdf with syntax highlighting"),
        epilog="Author:tushar.rishav@gmail.com"
    )
    parser.add_argument(
        "filename",
        help="absolute path of the python file",
        type=str)
    parser.add_argument(
        "-l",
        "--linenos",
        help="include line numbers.",
        default=True,
        action="store_true")
    parser.add_argument(
        "outputfile",
        help="absolute path of the output pdf file",
        nargs="?",
        type=str)
    parser.add_argument(
        "-s",
        "--size",
        help="PDF size. A2,A3,A4,A5 etc",
        type=str,
        default="A3")
    parser.add_argument(
        "-S",
        "--style",
        help="the style name for highlighting.",
        type=str,
        default="default",
        metavar="NAME")
    parser.add_argument(
        "-m",
        "--margin",
        help="the layout margins in inch (default 0.4in).",
        type=float,
        default=0.4,
        )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s v. {}".format(__version__))
    return parser.parse_args()


def main():
    args = parse_arg()
    pdf_file = get_output_file(args.filename, args.outputfile)
    pdf = Code2pdf(args.filename, pdf_file, args.size, args.margin)
    pdf.save_pdf(linenos=args.linenos, style=args.style)
    return 0

if __name__ == "__main__":
    sys.exit(main())
