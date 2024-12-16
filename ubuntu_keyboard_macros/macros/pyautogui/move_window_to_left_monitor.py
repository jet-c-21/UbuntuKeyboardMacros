
import pyautogui


def simulate_super_shift_left_arrow(debug=True):
    if debug:
        print("[*DEBUG*] - [pyautogui] - pressed keys: super + shift + left")

    pyautogui.hotkey("super", "shift", "left")

    if debug:
        print("[*DEBUG*] - [pyautogui] - released keys: super + shift + left")



if __name__ == "__main__":
    simulate_super_shift_left_arrow()
