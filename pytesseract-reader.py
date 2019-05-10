import pytesseract
import PIL
from PIL import Image
from pdf2image import convert_from_path
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


pages = convert_from_path('ReadME-Pytesseract-reader.pdf', 500)
for page in pages:
    page.save('out.jpg', 'JPEG')

input = "out.jpg"
output = pytesseract.image_to_string(Image.open(input))
print(output)
