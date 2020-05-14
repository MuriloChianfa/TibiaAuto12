def ScanRing(RingPositions, HOOK_OPTION):
    NoHasRing = [0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        NoHasRing = pyautogui.locateOnScreen('images/PlayerStats/NoRing.png', confidence=0.9, region=(
            RingPositions[0], RingPositions[1], RingPositions[2], RingPositions[3]))
        if NoHasRing:
            return True
        else:
            return False

    elif HOOK_OPTION == 1:
        from Engine.HookWindow import LocateImage

        NoHasRing[0], NoHasRing[1] = LocateImage('images/PlayerStats/NoRing.png', Precision=0.9, Region=(
            RingPositions[0], RingPositions[1], RingPositions[2], RingPositions[3]))
        if NoHasRing[0] != 0 and NoHasRing[1] != 0:
            return True
        else:
            return False


def SearchForRing(Ring, HOOK_OPTION):
    FoundRing = [0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        FoundRing = pyautogui.locateCenterOnScreen('images/Rings/' + Ring + '.png', confidence=0.9)
        if FoundRing:
            return FoundRing[0], FoundRing[1]
        else:
            return 0, 0

    elif HOOK_OPTION == 1:
        from Engine.HookWindow import LocateCenterImage

        FoundRing[0], FoundRing[1] = LocateCenterImage('images/Rings/' + Ring + '.png', Precision=0.9)
        if FoundRing[0] != 0 and FoundRing[1] != 0:
            return FoundRing[0], FoundRing[1]
        else:
            return 0, 0
