from pynput.keyboard import Controller, Key


def simulate_super_shift_right_arrow(keyboard_controller:Controller=None,debug: bool = True):
    if keyboard_controller is None:
        keyboard_controller = Controller()

    # Press and hold Super + Shift
    keyboard_controller.press(Key.cmd)  # Super key
    keyboard_controller.press(Key.shift)  # Shift key
    keyboard_controller.press(Key.right)

    if debug:
        msg = f"[*DEBUG*] - pressed keys: {Key.cmd} + {Key.shift} + {Key.right}"
        print(msg)

    keyboard_controller.release(Key.right)
    keyboard_controller.release(Key.shift)
    keyboard_controller.release(Key.cmd)

    if debug:
        msg = f"[*DEBUG*] - released keys: {Key.cmd} + {Key.shift} + {Key.right}"
        print(msg)


if __name__ == "__main__":
    simulate_super_shift_right_arrow()
