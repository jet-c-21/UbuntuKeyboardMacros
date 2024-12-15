"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""
import contextlib
from typing import Union

from Xlib import display


def xev_keycode_to_keysym(keycode) -> Union[str, None]:
    disp = display.Display()
    with contextlib.suppress(Exception):
        keysym = hex(disp.keycode_to_keysym(keycode, 0))
    disp.close()
    return keysym

if __name__ == "__main__":
    _keysym = xev_keycode_to_keysym(156)
    msg = f"[*DEBUG*] - KeySym: {_keysym}, type: {type(_keysym)}"
    print(msg)


