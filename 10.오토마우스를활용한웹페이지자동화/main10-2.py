import pyautogui
import pyperclip
import time
import clipboard

# Move the mouse to the desired position and click to focus the input area
pyautogui.moveTo(450, 263, duration=0.2)
pyautogui.click()
time.sleep(0.5)

# Copy the text to the clipboard
clipboard.copy("서울 날씨")

# Simulate a paste operation using Ctrl+V
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

# Simulate pressing Enter
pyautogui.press("enter")
time.sleep(1)
