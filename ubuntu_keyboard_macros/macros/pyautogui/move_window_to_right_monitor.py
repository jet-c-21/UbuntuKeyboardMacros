
import pyautogui


def simulate_super_shift_right_arrow(debug=True):
    if debug:
        print("[*DEBUG*] - [pyautogui] - pressed keys: super + shift + right")

    pyautogui.hotkey("super", "shift", "right")

    if debug:
        print("[*DEBUG*] - [pyautogui] - released keys: super + shift + right")



if __name__ == "__main__":
    simulate_super_shift_right_arrow()
