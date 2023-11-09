from PIL import Image
import pytesseract

image_path = r"/Users/isaemmi/Desktop/pyProject/19.이미지에서글자추출/스크린샷.png"

pytesseract.pytesseract.tesseract_cmd=r"/opt/homebrew/bin/tesseract"
text = pytesseract.image_to_string(Image.open(image_path), lang="kor")

print(text)