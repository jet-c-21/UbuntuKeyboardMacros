"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""

"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""

from pynput.keyboard import Controller

from ubuntu_keyboard_macros.event_handler._event_handler_base import EventHandlerBase
from ubuntu_keyboard_macros.macros.pynput.move_window_to_right_monitor import simulate_super_shift_right_arrow


class MoveWindowToRightMonitor(EventHandlerBase):
    def __init__(self, keyboard_controller:Controller=None):
        super().__init__(keyboard_controller=keyboard_controller)

    def do_handle(self):
        # subprocess.run([sys.executable, move_window_to_right_monitor.__file__], check=False)
        simulate_super_shift_right_arrow(keyboard_controller=self.keyboard_controller)

if __name__ == "__main__":
    handler = MoveWindowToRightMonitor()
    handler.do_handle()
