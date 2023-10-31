import pyautogui
import pyperclip
import time
import os


# print(os.getcwd())
#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
a=os.path.abspath(__file__)
print(a)

picPosition = pyautogui.locateAllOnScreen(r'/Users/isaemmi/Desktop/pyProject/12.오토마우스를 활용한 pc카카오톡 자동화/pic1.png')

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('/Users/isaemmi/Desktop/pyProject/12.오토마우스를 활용한 pc카카오톡 자동화/pic2.png')
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('/Users/isaemmi/Desktop/pyProject/12.오토마우스를 활용한 pc카카오톡 자동화/pic3.png')
    print(picPosition)
print(picPosition)

clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)
print(clickPosition)
# pyperclip.copy("this is the auto message function")
# pyautogui.hotkey("ctrl", "v")
# time.sleep(1.0)

# pyautogui.write(["enter"])
# time.sleep(1.0)

# pyautogui.write(["escape"])
# time.sleep(1.0)