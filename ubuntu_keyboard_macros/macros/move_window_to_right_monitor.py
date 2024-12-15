from pynput.keyboard import Controller, Key


def simulate_super_shift_right_arrow(debug: bool = True):
    keyboard = Controller()
    # Press and hold Super + Shift
    keyboard.press(Key.cmd)  # Super key
    keyboard.press(Key.shift)  # Shift key
    keyboard.press(Key.right)

    if debug:
        msg = f"[*DEBUG*] - pressed keys: {Key.cmd} + {Key.shift} + {Key.right}"
        print(msg)

    keyboard.release(Key.right)
    keyboard.release(Key.shift)
    keyboard.release(Key.cmd)

    if debug:
        msg = f"[*DEBUG*] - released keys: {Key.cmd} + {Key.shift} + {Key.right}"
        print(msg)


if __name__ == "__main__":
    simulate_super_shift_right_arrow()
