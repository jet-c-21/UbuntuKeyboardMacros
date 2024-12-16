"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-15
"""
import contextlib
from typing import Union

from Xlib import display


def xev_keycode_to_keysym(keycode, return_decimal_keysym=False) -> Union[Union[str, int], None]:
    """

    decimal keycode to hex keysym

    :param keycode:
    :return:
    """
    disp = display.Display()
    with contextlib.suppress(Exception):
        keysym = hex(disp.keycode_to_keysym(keycode, 0))
    disp.close()

    if return_decimal_keysym:
        return int(keysym, 16)

    else:
        return keysym

if __name__ == "__main__":
    _keysym = xev_keycode_to_keysym(156)
    msg = f"[*DEBUG*] - KeySym: {_keysym}, type: {type(_keysym)}"
    print(msg)


