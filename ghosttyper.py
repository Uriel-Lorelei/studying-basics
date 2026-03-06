import pyautogui
import keyboard

while True:
    if keyboard.is_pressed('r'):
        pyautogui.press('left')
        pyautogui.press('left')
        pyautogui.write("e")
    
    if keyboard.is_pressed('i'):
        pyautogui.press('left')
        pyautogui.write("oooo")
    
    if keyboard.is_pressed('v'):
        for i in range(5):
            pyautogui.press('left')
            pyautogui.write("cccccc")
            pyautogui.press('right')
            pyautogui.write("bbbbbb")
    
    if keyboard.is_pressed('ctrl'):
        pyautogui.hotkey('shift', 'esc')

    if keyboard.is_pressed('right'):
        pyautogui.press('left')
        pyautogui.press('left')

    if keyboard.is_pressed('e'):
        pyautogui.press('backspace')

        