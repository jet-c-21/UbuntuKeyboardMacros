"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-16
"""
import pathlib
import sys
from pynput import keyboard
from pynput.keyboard import Key, KeyCode, Listener

THIS_FILE_PATH = pathlib.Path(__file__).absolute().resolve()
THIS_FILE_PARENT_DIR = THIS_FILE_PATH.parent
PROJECT_DIR = THIS_FILE_PARENT_DIR.parent
sys.path.append(str(PROJECT_DIR))

from ubuntu_keyboard_macros.ult.file_tool import create_file_from_template, read_yaml
from ubuntu_keyboard_macros.ult.keycode_tool import xev_keycode_to_keysym

def _single_key_on_press_handle(key):
    try:
        if key is None:
            msg = "[*WARN*] - Key is None!"
            print(msg)
            return

        elif isinstance(key, Key):
            msg = f"[*INFO*] - <Key> pressed: {key}"
            print(msg)
            return

        elif isinstance(key, KeyCode):
            # Print the key name
            print(f"[*DEBUG*] - KeyCode pressed: {key} | Type: {type(key)}")
            input_keysym = hex(key.vk)
            if input_keysym == MOD3_KEYSYM:
                print("[*INFO*] - Mod3 pressed!")

    except AttributeError as e:
        print(f"[*WARN*] - Special key pressed: {key}, Error: {e}")


def _on_press(key):
    pass


def _on_release(key):
    pass


def _main():
    # Start listening to keyboard events
    with keyboard.Listener(on_press=_single_key_on_press_handle, on_release=_on_release) as listener:
        msg = "[*INFO*] - Listening to keyboard events..."
        print(msg)
        listener.join()


if __name__ == "__main__":
    SETTING_TPL_FILE = PROJECT_DIR / "settings-templates" / "settings.yaml"
    SETTING_FILE = PROJECT_DIR / "settings" / "settings.yaml"

    if not SETTING_FILE.is_file():
        create_file_from_template(SETTING_FILE, SETTING_TPL_FILE)

    settings_yaml = read_yaml(SETTING_FILE)
    ctk_keycode = settings_yaml["combination_trigger_key"]["keycode"]
    MOD3_KEYSYM = xev_keycode_to_keysym(ctk_keycode)
    _main()

    # does the team of pynput treat this as "event"?