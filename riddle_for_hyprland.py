import webbrowser, json
import wayland_automation as wa
import subprocess, time

# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # rickroll
url = "https://web.archive.org/web/20230717204942/https://pnrtscr.com/fep8be" #jeff the killer

def checkWindow():
    result = subprocess.run(["hyprctl", "clients", "-j"], capture_output=True, text=True)
    workspaces = json.loads(result.stdout)
    
    for win in workspaces:
        if win.get('class') == "librewolf":
            return win['workspace']['id']

def moveWindow(workspace):
    subprocess.run(["hyprctl", "dispatch", "workspace", workspace])

def acceptCookies():
    wa.click(int(723*1.2), int(622*1.2), "left")

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
    moveWindow(str(checkWindow()))
    for i in range(10):
        acceptCookies()
        time.sleep(0.7)