"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-16
"""
import time
import pyautogui
from pprint import pp
from pyautogui import KEYBOARD_KEYS

if __name__ == '__main__':
    # pp(KEYBOARD_KEYS)
    # print(KEYBOARD_KEYS)
    pyautogui.hotkey("win", "shift", "left")

    time.sleep(3)

    pyautogui.hotkey("win", "shift", "right")