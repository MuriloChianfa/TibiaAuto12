import pyautogui

Follow = [0, 0]


def SetFollow():
    LocateFollow = pyautogui.locateOnScreen('images/TibiaSettings/follow.png', confidence=0.8)
    if LocateFollow:
        Follow[0], Follow[1] = pyautogui.center(LocateFollow)
        print("Clicking in Follow")
        return Follow[0], Follow[1]
    else:
        return 0, 0

