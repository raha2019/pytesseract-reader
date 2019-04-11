from pdf2image import convert_from_path, convert_from bytes
from pdf2image.exceptions import (
    PDFInforNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

import pytesseract
import PIL
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

image = convert_from_path()

input = ""

output = pytesseract.image_to_string(Image.open(input))
print(output)
