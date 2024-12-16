"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-16
"""
import subprocess
from typing import Dict, List

from pynput import keyboard
from pynput.keyboard import Controller

from ubuntu_keyboard_macros.ult.keycode_tool import xev_keycode_to_keysym


class PYNPUTEventListener:
    def __init__(self, settings_yaml: Dict, keyboard_controller: Controller=None):
        self.settings_yaml = settings_yaml
        if keyboard_controller is None:
            keyboard_controller = Controller()
        self.keyboard_controller = keyboard_controller

        self.combination_trigger_key_info = self.settings_yaml["combination_trigger_key"]
        self.ctk_event_code = self.combination_trigger_key_info["event_code"]
        self.ctk_keycode = self.combination_trigger_key_info["keycode"]
        self.ctk_keycode_hex: str = xev_keycode_to_keysym(self.ctk_keycode)
        self.ctk_keycode_decimal: int = int(self.ctk_keycode_hex, 16)
        self.ctk_modifier_name = self.combination_trigger_key_info["modifier_name"]

        msg = (f"[*INFO*] - ctk event code: {self.ctk_event_code}, "
               f"ctk keycode: {self.ctk_keycode}, "
               f"ctk keycode hex: {self.ctk_keycode_hex}, "
               f"ctk keycode decimal: {self.ctk_keycode_decimal}, "
               f"ctk modifier name: {self.ctk_modifier_name}\n")
        print(msg)

        self.global_hotkeys_handle_dict: Dict = {
            f"<{self.ctk_keycode_decimal}>+<left>": self.move_window_to_left_monitor,
            f"<{self.ctk_keycode_decimal}>+<right>": self.move_window_to_right_monitor,
        }
        self.global_hotkeys_listeners = keyboard.GlobalHotKeys(self.global_hotkeys_handle_dict)

        msg = f"[*INFO*] - {self.__class__.__name__} initialized\n"
        print(msg)

    @classmethod
    def run_pyautogui_hotkey_subprocess(cls, hotkey_str_ls: List[str]):
        """
        Runs pyautogui hotkey commands in a subprocess.
        :param hotkey_str_ls: List of strings representing hotkey keys.
        """
        hotkey_str = ", ".join(f'"{key}"' for key in hotkey_str_ls)  # Format as string literals
        command = f"import pyautogui; pyautogui.hotkey({hotkey_str})"
        subprocess.run(["python3", "-c", command], check=False)

    @classmethod
    def move_window_to_left_monitor(cls):
        msg = "[*DEBUG*] - ctk + <left> detected, start moving window to left monitor ..."
        print(msg)

        cls.run_pyautogui_hotkey_subprocess(["win", "shift", "left"])

        msg = "[*DEBUG*] - finish moving window to left monitor\n"
        print(msg)

    @classmethod
    def move_window_to_right_monitor(cls):
        msg = "[*DEBUG*] - ctk + <right> detected, start moving window to right monitor ..."
        print(msg)

        cls.run_pyautogui_hotkey_subprocess(["win", "shift", "right"])

        msg = "[*DEBUG*] - finish moving window to right monitor\n"
        print(msg)


    def launch(self):
        with self.global_hotkeys_listeners as listener:
            msg = f"[*INFO*] - start listening to global hotkeys combinations ..."
            print(msg)
            listener.join()
