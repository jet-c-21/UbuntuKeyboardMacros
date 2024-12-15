from pynput.keyboard import Controller, Key


def move_window_to_right_monitor():
    """Moves the current window to the right monitor using Super + Shift + RightArrow."""
    keyboard = Controller()

    # Log the start of the operation
    print("Moving window to the right monitor...")

    # Simulate pressing Super + Shift + RightArrow
    keyboard.press(Key.cmd)  # Super/Windows key
    keyboard.press(Key.shift)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.release(Key.shift)
    keyboard.release(Key.cmd)

    # Log the completion of the operation
    print("Window moved to the right monitor successfully.")

if __name__ == "__main__":
    move_window_to_right_monitor()
