from pynput.mouse import Listener

# coord = []

# def click(x,y,button,pressed):
#     if pressed:
#         x = int(x)
#         y = int(y)
#         coord.append(x)
#         coord.append(y)
#         print(coord)


import pyautogui

# Get the current mouse cursor position
current_position = pyautogui.position()

with Listener(on_click=current_position) as Lis :
    print(current_position)


# Print the X and Y coordinates
