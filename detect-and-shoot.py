import pyautogui
import win32api
import win32con
import time
from PIL import ImageGrab
import numpy as np

# def check_color(current_color, target_color, tolerance=50):
#     r_diff = abs(current_color[0] - target_color[0])
#     g_diff = abs(current_color[1] - target_color[1])
#     b_diff = abs(current_color[2] - target_color[2])

#     if r_diff < tolerance and g_diff < tolerance and b_diff < tolerance:
#         return True
#     return False

def mouse_movement(x_delta, y_delta):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x_delta), int(y_delta), 0, 0)

def shoot():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

for i in range(5):
    print(f"Now Running in {i}...")
    time.sleep(1)

while True:
    # center = (960, 527) 
    left = 910
    right = 1010
    top = 487 
    bottom = 567
    smoothing = 0.25

    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    frame = np.array(screenshot)

    r_filter = frame[:, :, 0] > 180
    g_filter = frame[:, :, 1] < 100
    b_filter = frame[:, :, 2] < 100

    redmask = r_filter & g_filter & b_filter

    y_coords, x_coords = np.where(redmask)

    if x_coords.any():
        target_x = np.mean(x_coords)
        target_y = np.mean(y_coords)
        print(f"CENTER OF A RED MASS AT: ({target_x}, {target_y})")

        rel_x = int(target_x - 50)
        rel_y = int(target_y - 40)

        mouse_movement(rel_x * smoothing, rel_y * smoothing)
        shoot() 

# while True:
#     what_color = pyautogui.pixel(int(1920/2), int(1080/2))
#     if check_color(what_color, (255, 0, 0)):
#         print("RED AAAAHHH")
#         shoot()

#     time.sleep(0.01)
