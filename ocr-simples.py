import pytesseract as ocr
from PIL import Image
import PIL
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(Image.open('at01.jpeg')))