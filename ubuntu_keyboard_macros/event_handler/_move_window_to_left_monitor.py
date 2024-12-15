"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""

from ubuntu_keyboard_macros.event_handler._event_handler_base import EventHandlerBase
from ubuntu_keyboard_macros.macros import simulate_super_shift_left_arrow


class MoveWindowToLeftMonitor(EventHandlerBase):
    def __init__(self):
        super().__init__()

    def do_handle(self):
        simulate_super_shift_left_arrow()
        print("!!!!!!")
