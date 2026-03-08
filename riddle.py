import webbrowser
import pyautogui

# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # rickroll
url = "https://web.archive.org/web/20230717204942/https://pnrtscr.com/fep8be" #jeff the killer

# for jeff the killer
def accept_cookies():
    rgb = pyautogui.pixel(836, 687)
    if rgb == (132, 94, 194):
        pyautogui.moveTo(836, 687)
        pyautogui.click()
        return True

def game():
    answer = 'paris'
    print("----------------------------------------------")
    question = input("What is the capital city of France?\n-------->").lower()
    if question == answer:
        print("Correct")
        print("YOUR PRIZE IS HERE!")
        return True
    else:
        print("HOW DO YOU NOT EVEN KNOW THE CAPITAL CITY OF FRANCE.\nTRY AGAIN!!!(hint: starts with 'p')")
        game()

if game():
    webbrowser.open(url)
    while True:
        if accept_cookies():
            break


