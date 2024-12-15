"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""

import pathlib
from typing import Optional
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

from ubuntu_keyboard_macros.ult.file_tool import create_file_from_template, read_yaml
from ubuntu_keyboard_macros.ult.keycode_tool import xev_keycode_to_keysym

class KeyboardEventListener:
    def __init__(self,
                 settings_fp:Optional[pathlib.Path] = None):