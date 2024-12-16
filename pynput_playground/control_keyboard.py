"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-16
"""
from pynput.keyboard import Key, Controller
from pynput.keyboard import HotKey


if __name__ == '__main__':
    keyboard_controller = Controller()

    keyboard_controller.press(f"ctrl+<alt>+a")

