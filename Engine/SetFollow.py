def SetFollow(HOOK_OPTION):
    Follow = [0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        LocateFollow = pyautogui.locateOnScreen('images/TibiaSettings/follow.png', confidence=0.8)
        if LocateFollow:
            Follow[0], Follow[1] = pyautogui.center(LocateFollow)
            print("Clicking in Follow")
            return Follow[0], Follow[1]
        else:
            return 0, 0

    elif HOOK_OPTION == 1:
        from Engine.HookWindow import LocateImage, LocateBoolRGBImage
        x, y = LocateImage('images/TibiaSettings/follow.png', Precision=0.8)
        if LocateBoolRGBImage('images/TibiaSettings/follow.png', Precision=0.8, Region=(x - 3, y - 3, x + 16, y + 16)):
            return False
        else:
            return True
