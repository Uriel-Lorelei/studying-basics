import pyautogui
import time

time.sleep(7)
x, y = pyautogui.position()
rgb = pyautogui.pixel(x, y)
print(rgb)
print(x, y)