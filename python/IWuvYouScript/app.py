from pynput import keyboard
from time import sleep

is_love = False

print(f'quick controls: <Space Key>')
print("interval <seconds> default : .2")
interval = str(input())
if not interval:
    interval = .2
interval = float(interval)

print("Text/Message e.g 'I Wuv You' default : 'I Love You'")
message = str(input())
if not message:
    message = "I Love You"


def on_press(key):
    global is_love
    if key == keyboard.Key.space:
        is_love = not is_love

def print_iloveyou():
    sleep(interval)
    for c in message.split(" "):
        sleep(len(c) / 10)
        keyboard.Controller().type(c)
        keyboard.Controller().press(keyboard.Key.enter)
        keyboard.Controller().release(keyboard.Key.enter)


listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    if not is_love:
        continue
    print_iloveyou()