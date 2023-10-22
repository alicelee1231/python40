import pyautogui
import time
import pyperclip

pyautogui.moveTo(1230,868,0.2)

pyautogui.click()
time.sleep(0.5)

# a =pyautogui.position()
# print(a)

pyperclip.copy("weather")
pyautogui.hotkey("ctrl","v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)