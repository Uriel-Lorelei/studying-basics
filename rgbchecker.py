import pyautogui
import time

for i in range(10, 0, -1):
    print(f"Checking the rgb where the mouse is in {i}...")
    time.sleep(1)
x, y = pyautogui.position()
rgb = pyautogui.pixel(x, y)
print(rgb)

print(x, y)
