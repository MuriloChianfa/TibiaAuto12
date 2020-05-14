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
        from Engine.HookWindow import LocateCenterImage

        Follow[0], Follow[1] = LocateCenterImage('images/TibiaSettings/follow.png', Precision=0.8, Gray=False)
        if Follow[0] != 0 and Follow[1] != 0:
            print("Clicking in Follow")
            return int(Follow[0]), int(Follow[1])
        else:
            return 0, 0
