import googletrans
from os import linesep

translator = googletrans.Translator()

read_file_path = r"/Users/isaemmi/Desktop/pyProject/9.영어로된문서를한글로자동번역/영어파일.txt"

with open(read_file_path,"r") as f :
    readlines = f.readlines()

for lines in readlines:
    result1 = translator.translate(lines, dest="ko")
    print(result1.text)
