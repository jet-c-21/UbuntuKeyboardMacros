"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""

import pathlib
import subprocess
from typing import Dict

from pynput import keyboard

from ubuntu_keyboard_macros.ult.file_tool import create_file_from_template, read_yaml
from ubuntu_keyboard_macros.ult.keycode_tool import xev_keycode_to_keysym

# Paths and project directory setup
THIS_FILE_PATH = pathlib.Path(__file__).absolute().resolve()
THIS_FILE_PARENT_DIR = THIS_FILE_PATH.parent
PROJECT_DIR = THIS_FILE_PARENT_DIR

# Helper functions
def setup_settings_file(template_path, settings_path):
    if not settings_path.is_file():
        create_file_from_template(settings_path, template_path)

def load_settings(settings_path) -> Dict:
    return read_yaml(settings_path)

# def move_window_to_left_monitor():
#     print("[*DEBUG*] - ctk + <left> detected, start moving window to left monitor ...")
#     pyautogui.hotkey("win", "shift", "left")
#     print("[*DEBUG*] - finish moving window to left monitor\n")
#
# def move_window_to_right_monitor():
#     print("[*DEBUG*] - ctk + <right> detected, start moving window to right monitor ...")
#     pyautogui.hotkey("win", "shift", "right")
#     print("[*DEBUG*] - finish moving window to right monitor\n")

def move_window_to_left_monitor():
    print("[*DEBUG*] - ctk + <left> detected, start moving window to left monitor ...")
    subprocess.run(["python3", "-c", 'import pyautogui; pyautogui.hotkey("win", "shift", "left")'], check=False)
    print("[*DEBUG*] - finish moving window to left monitor\n")

def move_window_to_right_monitor():
    print("[*DEBUG*] - ctk + <right> detected, start moving window to right monitor ...")
    subprocess.run(["python3", "-c", 'import pyautogui; pyautogui.hotkey("win", "shift", "right")'], check=False)
    print("[*DEBUG*] - finish moving window to right monitor\n")

def configure_global_hotkeys(settings_yaml):
    combination_trigger_key_info = settings_yaml["combination_trigger_key"]

    ctk_event_code = combination_trigger_key_info["event_code"]
    ctk_keycode = combination_trigger_key_info["keycode"]
    ctk_keycode_hex = xev_keycode_to_keysym(ctk_keycode)
    ctk_keycode_decimal = int(ctk_keycode_hex, 16)
    ctk_modifier_name = combination_trigger_key_info["modifier_name"]

    print(f"[*INFO*] - ctk event code: {ctk_event_code}, "
          f"ctk keycode: {ctk_keycode}, "
          f"ctk keycode hex: {ctk_keycode_hex}, "
          f"ctk keycode decimal: {ctk_keycode_decimal}, "
          f"ctk modifier name: {ctk_modifier_name}\n")

    global_hotkeys_handle_dict = {
        f"<{ctk_keycode_decimal}>+<left>": move_window_to_left_monitor,
        f"<{ctk_keycode_decimal}>+<right>": move_window_to_right_monitor,
    }

    return keyboard.GlobalHotKeys(global_hotkeys_handle_dict)

def main():
    # Paths for settings
    SETTING_TPL_FILE = PROJECT_DIR / "settings-templates" / "settings.yaml"
    SETTING_FILE = PROJECT_DIR / "settings" / "settings.yaml"

    # Ensure settings file exists
    setup_settings_file(SETTING_TPL_FILE, SETTING_FILE)

    # Load settings
    settings_yaml = load_settings(SETTING_FILE)

    # Configure global hotkeys
    global_hotkeys_listeners = configure_global_hotkeys(settings_yaml)

    # Launch global hotkeys listener
    with global_hotkeys_listeners as listener:
        listener.join()

if __name__ == "__main__":
    main()
