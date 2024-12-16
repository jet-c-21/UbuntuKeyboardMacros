
from pynput.keyboard import Controller, Key


def simulate_super_shift_left_arrow(keyboard_controller:Controller=None, debug: bool = True):
    if keyboard_controller is None:
        keyboard_controller = Controller()

    # Press and hold Super + Shift
    keyboard_controller.press(Key.cmd)  # Super key
    keyboard_controller.press(Key.shift)  # Shift key
    keyboard_controller.press(Key.left)

    if debug:
        msg = f"[*DEBUG*] - pressed keys: {Key.cmd} + {Key.shift} + {Key.left}"
        print(msg)

    keyboard_controller.release(Key.left)
    keyboard_controller.release(Key.shift)
    keyboard_controller.release(Key.cmd)

    if debug:
        msg = f"[*DEBUG*] - released keys: {Key.cmd} + {Key.shift} + {Key.left}"
        print(msg)


if __name__ == "__main__":
    simulate_super_shift_left_arrow()

    # how to refactor it with pyautogui?
