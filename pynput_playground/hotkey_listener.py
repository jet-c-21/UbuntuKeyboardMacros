"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-16
"""
from pynput import keyboard


def on_activate_h():
    print("<ctrl>+<alt>+h pressed")

def on_activate_i():
    print("<ctrl>+<alt>+i pressed")

def on_active_mod3():
    print("<mod3>+left pressed")

listener = keyboard.GlobalHotKeys(
    {
        "<ctrl>+<alt>+h": on_activate_h,
        "<ctrl>+<alt>+i": on_activate_i,
        "<269025089>+left": on_active_mod3,
    }
)

listener.start()

while True:
    pass
