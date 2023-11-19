import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd=r"/opt/homebrew/bin/tesseract"
language = pytesseract.get_languages(config='')
image_path = r"/Users/isaemmi/Desktop/pyProject/19.이미지에서글자추출/스크린샷.png"

pytesseract.image_to_string(Image.open(image_path), lang="kor")
print(language)