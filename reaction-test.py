import pyautogui

while True:
    try:
        x,y = pyautogui.position()
        rgb = pyautogui.pixel(x, y)
        
        if rgb == (75, 219, 106):
            pyautogui.click()
    
    except KeyboardInterrupt:
        break