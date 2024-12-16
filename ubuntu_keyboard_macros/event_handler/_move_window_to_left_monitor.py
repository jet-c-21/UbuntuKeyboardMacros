"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""

from pynput.keyboard import Controller

from ubuntu_keyboard_macros.event_handler._event_handler_base import EventHandlerBase
from ubuntu_keyboard_macros.macros.pynput.move_window_to_left_monitor import simulate_super_shift_left_arrow

class MoveWindowToLeftMonitor(EventHandlerBase):
    def __init__(self, keyboard_controller:Controller=None):
        super().__init__(keyboard_controller=keyboard_controller)

    def do_handle(self):
        # subprocess.run(["python3", move_window_to_left_monitor.__file__], check=False)
        simulate_super_shift_left_arrow(keyboard_controller=self.keyboard_controller)


if __name__ == "__main__":
    handler = MoveWindowToLeftMonitor()
    handler.do_handle()
