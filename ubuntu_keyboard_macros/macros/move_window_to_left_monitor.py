from pynput.keyboard import Controller, Key


def simulate_super_shift_left_arrow():
    keyboard = Controller()
    # Press and hold Super + Shift
    keyboard.press(Key.cmd)  # Super key
    keyboard.press(Key.shift)  # Shift key
    keyboard.press(Key.left)

    msg = f"[*DEBUG*] - pressed keys: {Key.cmd} + {Key.shift} + {Key.left}"
    print(msg)

    keyboard.release(Key.left)
    keyboard.release(Key.shift)
    keyboard.release(Key.cmd)
    msg = f"[*DEBUG*] - released keys: {Key.cmd} + {Key.shift} + {Key.left}"
    print(msg)

    msg = "[*INFO*] - finish simulating Super + Shift + LeftArrow"
    print(msg)


if __name__ == "__main__":
    simulate_super_shift_left_arrow()
