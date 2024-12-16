"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""

import pathlib

# from ubuntu_keyboard_macros import KeyboardEventListener
from ubuntu_keyboard_macros.ult.file_tool import create_file_from_template, read_yaml

THIS_FILE_PATH = pathlib.Path(__file__).absolute().resolve()
THIS_FILE_PARENT_DIR = THIS_FILE_PATH.parent
PROJECT_DIR = THIS_FILE_PARENT_DIR


from pynput.keyboard import Controller

from ubuntu_keyboard_macros import PYNPUTEventListener


def _main():
    pynput_el = PYNPUTEventListener(settings_yaml, keyboard_controller=keyboard_controller)
    pynput_el.launch()


if __name__ == "__main__":
    SETTING_TPL_FILE = PROJECT_DIR / "settings-templates" / "settings.yaml"
    SETTING_FILE = PROJECT_DIR / "settings" / "settings.yaml"

    if not SETTING_FILE.is_file():
        create_file_from_template(SETTING_FILE, SETTING_TPL_FILE)

    settings_yaml = read_yaml(SETTING_FILE)
    keyboard_controller = Controller()
    _main()
