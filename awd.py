import keyboard
import json

# def on_key(e):
#     print(f"\nKEY: {e.name}")

#keyboard.on_press(on_key)
#keyboard.add_hotkey('a', )
events = keyboard.record('esc')

with open("dest.txt", "w") as f:
    sss = [e.to_json() for e in events]
    json.dump(sss, f, indent=4)
keyboard.play(events)

with open("dest.txt", "r") as l:
    datae = json.load(l)

count = 0
for data in datae:
    print(str(data['name/']))

#keyboard.wait('esc')

