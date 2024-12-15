"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""

import subprocess
import sys

from ubuntu_keyboard_macros.event_handler._event_handler_base import EventHandlerBase
from ubuntu_keyboard_macros.macros import move_window_to_left_monitor


class MoveWindowToLeftMonitor(EventHandlerBase):
    def __init__(self):
        super().__init__()

    def do_handle(self):
        subprocess.run([sys.executable, move_window_to_left_monitor.__file__], check=False)


if __name__ == "__main__":
    handler = MoveWindowToLeftMonitor()
    handler.do_handle()
