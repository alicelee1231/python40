import pyautogui
import os


print(os.getcwd())
#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
picPosition = pyautogui.locateOnScreen('/Users/isaemmi/Desktop/pyProject/pic1.png')

picPosition = pyautogui.locateOnScreen('pic1.png')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic2.png')
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic3.png')
    print(picPosition)