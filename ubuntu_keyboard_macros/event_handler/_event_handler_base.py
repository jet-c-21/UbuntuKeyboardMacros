"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""
from pynput.keyboard import Controller


class EventHandlerBase:
    def __init__(self, keyboard_controller:Controller=None):
        self.keyboard_controller = keyboard_controller

    def do_handle(self):
        pass
