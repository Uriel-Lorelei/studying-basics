import pyautogui
import random

def movements(x, y, z):
    pyautogui.moveTo(x, y, duration=z)

for i in range(400):
    x = random.randint(9, 1909)
    y = random.randint(9, 1000)
    z = random.random()

    movements(x, y, z)