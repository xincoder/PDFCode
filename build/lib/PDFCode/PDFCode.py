#! /usr/bin/env python
import argparse
import logging
import os
import sys
import pdfkit
import magic
import pygments
from pygments import lexers, formatters, styles
import shutil

__version__ = '0.0.1'

class PDFCode:
    """
        Convert a source file into a pdf with syntax highlighting.
    """
    def __init__(self, input_file=None, output_file=None, size="A4", margin=0.4, input_root=''):
        if not input_file:
            raise Exception("input file is required")
        self.input_file = input_file
        self.pdf_file = output_file 
        self.size = size
        self.margin = '{}in'.format(margin)
        self.input_root = input_root

        now_folder = os.path.dirname(output_file)
        if not os.path.exists(now_folder):
            os.makedirs(now_folder)

    def highlight_code(self, linenos=True, style='default'):
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
                try:
                    content = f.read()
                except:
                    return None, False
                try:
                    lexer = lexer or lexers.guess_lexer(content)
                except pygments.util.ClassNotFound:
                    lexer = lexers.get_lexer_by_name("text")
        except EnvironmentError as exread:
            fmt = "\nUnable to read file: {}\n{}"
            logging.error(fmt.format(self.input_file, exread))
            sys.exit(2)

        return pygments.highlight(content, lexer, formatter), True

    def save_pdf(self, linenos=True, style="default", convert=False):
        print('Processing {} ...'.format(self.input_file))
        
        if convert:
            text, res = self.highlight_code(linenos=linenos, style=style)
            if not res: # if not successfully read the file
                self.pdf_file = self.pdf_file.replace('.pdf', '')
                shutil.copy(self.input_file, self.pdf_file)
            else:
                options = {
                    'page-size': self.size.lower(),
                    'margin-top': self.margin,
                    'margin-right': self.margin,
                    'margin-bottom': self.margin,
                    'margin-left': self.margin,
                    'encoding': "UTF-8",
                    'custom-header' : [
                        ('Accept-Encoding', 'gzip')
                    ],
                    # 'header-left':self.input_file.replace(self.input_root, './'),
                    'header-left':self.input_file,
                    'header-font-size': 7,
                    'footer-center': '[page]',
                    'footer-font-size': 7,
                    
                }
                pdfkit.from_string(input=text, output_path=self.pdf_file, cover='', options=options)
        else:
            shutil.copy(self.input_file, self.pdf_file)
        print('PDF saved at {}'.format(self.pdf_file))
        print('####################################################')


    
def get_path_list(path_src, path_dst):
    input_root = path_src
    input_file_list = []

    if os.path.isfile(path_src):
        input_file_list.append(path_src)    
        input_root = os.path.dirname(path_src)+'/'
    else:
        input_root = os.path.dirname(input_root+'/')+'/'
        for (current_path, subfolder, filenames) in os.walk(path_src):
            input_file_list += [os.path.join(current_path, x) for x in filenames]

    
    if path_dst is None:
        path_dst = os.path.join(input_root, 'PDFCode_Results/')
    else:
        path_dst = os.path.dirname(path_dst+'/')+'/'
        # print(input_root, path_dst)

    convert_mask_list = [any(mm in magic.detect_from_filename(x).mime_type for mm in ['text/', 'x-']) for x in input_file_list]

    # replace root path
    now_file_list = [x.replace(input_root, path_dst) for x in input_file_list] 
    
    # replace extension
    # now_ext_list = [os.path.splitext(x)[-1] for x in now_file_list]
    # output_file_list = [name.replace(ext, '.pdf') if ext else name for name, ext in zip(now_file_list, now_ext_list)] 

    # convert_mask_list = [magic.detect_from_filename(x).encoding!='binary' for x in input_file_list]    
    output_file_list = [name+'.pdf' if convert_mask else name for name, convert_mask in zip(now_file_list, convert_mask_list) ] 
    
    return input_file_list, output_file_list, convert_mask_list, input_root


def parse_arg():
    parser = argparse.ArgumentParser(
        description=(
            "Convert source files into .pdf with syntax highlighting"),
        epilog="Author:xincoder@gmail.com"
    )
    parser.add_argument(
        "src",
        help="the path of the file/folder",
        type=str)
    parser.add_argument(
        "--dst",
        help="the path of the saving target folder. Empty will save to PDFCode_Results/",
        nargs="?",
        type=str)
    parser.add_argument(
        "-l",
        "--linenos",
        help="include line numbers.",
        default=True,
        action="store_true")
    parser.add_argument(
        "-s",
        "--size",
        help="PDF size. Letter,A1,A2,A3,A4,A5 etc",
        type=str,
        default="A4")
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
    infile_list, outfile_list, convert_mask_list, input_root = get_path_list(args.src, args.dst)
    for in_path, out_path, convert_mask in zip(infile_list, outfile_list, convert_mask_list):
        pdf = PDFCode(input_file=in_path, output_file=out_path, size=args.size, margin=args.margin, input_root=input_root)
        pdf.save_pdf(linenos=args.linenos, style=args.style, convert=convert_mask)
    return 0

if __name__ == "__main__":
    sys.exit(main())
