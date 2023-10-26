import pyautogui
import time
import pyperclip
import webbrowser

weather = ["seoul weather", "daejeon weather"]

addr_x =156 
addr_y =109
start_x=24 
start_y=332
end_x=688 
end_y =757

webbrowser.open("https://www.google.com")
time.sleep(2)

for local in weather:
    # pyautogui.moveTo(addr_x,addr_y)
    # time.sleep(0.2)
    # pyautogui.write("www.google.com",interval=0.1)
    # pyautogui.write(["enter"])
    # time.sleep(1)
    
    pyperclip.copy(local)
    pyautogui.hotkey("ctrl","weather")
    pyautogui.hotkey("ctrl","v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)
    savePath='10.오토마우스를활용한웹페이지자동화//' + local + '.png'
    pyautogui.screenshot(savePath,region=(start_x,start_y,end_x-start_x,end_y-start_y))