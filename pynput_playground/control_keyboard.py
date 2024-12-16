"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-16
"""
import time

from pynput.keyboard import Key, Controller
from pynput.keyboard import HotKey


if __name__ == '__main__':
    keyboard_controller = Controller()

    keyboard_controller.press(Key.cmd)
    keyboard_controller.press(Key.shift)
    keyboard_controller.press(Key.left)
    keyboard_controller.release(Key.left)
    keyboard_controller.release(Key.shift)
    keyboard_controller.release(Key.cmd)

