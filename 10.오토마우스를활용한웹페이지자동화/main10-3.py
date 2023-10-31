# import pyautogui
# import time
# import pyperclip

# pyautogui.moveTo(1241,206,0.2)
# pyautogui.click()
# time.sleep(0.5)

# pyperclip.copy("서울 날씨")
# pyautogui.hotkey("ctrl","v")
# time.sleep(0.5)

# pyautogui.write(["enter"])
# time.sleep(1)

import pyautogui

start_x = 29
start_y = 311
end_x = 695
end_y = 722

# Calculate the width and height of the region
width = end_x - start_x
height = end_y - start_y

# Take a screenshot of the specified region
screenshot = pyautogui.screenshot(region=(start_x, start_y, width, height))

# Save the screenshot to a file with a valid file path
file_path = '10.오토마우스를활용한웹페이지자동화/서울날씨.png'
screenshot.save(file_path)

