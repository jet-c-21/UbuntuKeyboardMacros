"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2024-12-16
"""
from pynput.keyboard import HotKey

def try_parse(key_str:str):
    try:
        hotkey = HotKey.parse(key_str)
        msg = f"[*DEBUG*] - key str: {key_str} -> parsed hotkey: {hotkey}"
        print(msg)
    except Exception as e:
        msg = f"[*DEBUG*] - failed to parse hotkey: {key_str}, Error: {e}"
        print(msg)

if __name__ == '__main__':
    s = "left"
    try_parse(s)

    s = "Left"
    try_parse(s)

    s = f"<left>"
    try_parse(s)

