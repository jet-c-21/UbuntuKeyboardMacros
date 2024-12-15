from pynput.keyboard import Controller, Key


def simulate_super_shift_left_arrow():
    keyboard = Controller()
    # Press and hold Super + Shift
    keyboard.press(Key.cmd)  # Super key
    keyboard.press(Key.shift)  # Shift key
    # Simulate LeftArrow key press
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    # Release Super + Shift
    keyboard.release(Key.shift)
    keyboard.release(Key.cmd)

if __name__ == "__main__":
    simulate_super_shift_left_arrow()
