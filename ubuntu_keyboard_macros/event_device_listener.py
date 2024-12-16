"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""

from typing import Dict

from evdev import InputDevice, categorize, ecodes
from pynput.keyboard import Controller

from ubuntu_keyboard_macros.event_handler import (
    MoveWindowToLeftMonitor,
    MoveWindowToRightMonitor,
)
from ubuntu_keyboard_macros.ult.console_tool import RichPrinter


class KeyboardEventListener:
    def __init__(self, settings_yaml: Dict, keyboard_controller:Controller=None):
        self.settings_yaml = settings_yaml

        if keyboard_controller is None:
            keyboard_controller = Controller()

        self.keyboard_controller = keyboard_controller
        self.listened_keyboard_event_file = self.settings_yaml["listened_keyboard_event_file"]
        self.input_device = InputDevice(self.listened_keyboard_event_file)
        self.combination_trigger_key = self.settings_yaml["combination_trigger_key"]
        self.rich_printer = RichPrinter()
        self.event_handlers_dict = {
            "KEY_LEFT": MoveWindowToLeftMonitor(keyboard_controller=keyboard_controller),
            "KEY_RIGHT": MoveWindowToRightMonitor(keyboard_controller=keyboard_controller),
        }

    def detect_key_combination(self):
        """
        Detect the key combination of KEY_PROG1 (mod3 key) + KEY_LEFT in sequence.
        """
        print("[INFO] - Listening for key combinations...")
        last_key = None  # Track the last pressed key
        for event in self.input_device.read_loop():
            if event.type == ecodes.EV_KEY:
                key_event = categorize(event)
                keycode = key_event.keycode

                if key_event.keystate == key_event.key_down:
                    print(f"[DEBUG] - Key Down: {keycode}")

                    if last_key == self.combination_trigger_key and keycode in self.event_handlers_dict:
                        self.rich_printer(
                            f"[*INFO*] - detected key combination: {self.combination_trigger_key} + {keycode}"
                        )

                        handler = self.event_handlers_dict[keycode]
                        print(f"[DEBUG] - handler: {handler}")
                        handler.do_handle()

                        # handle_script = self.event_handlers_dict[keycode]
                        # subprocess.run(
                        #     ["python3", handle_script],
                        #     check=False,
                        # )

                    last_key = keycode

    def launch(self):
        self.detect_key_combination()


if __name__ == "__main__":
    pass
