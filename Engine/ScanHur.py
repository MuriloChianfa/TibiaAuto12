def ScanHur(StatsPositions, HOOK_OPTION):
    HasHur = [0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        HasHur = pyautogui.locateOnScreen('images/PlayerStats/Hur.png', confidence=0.9, region=(
            StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3]))
        if HasHur:
            return False
        else:
            return True

    elif HOOK_OPTION == 1:
        from HookWindow import LocateImage

        HasHur[0], HasHur[1] = LocateImage('images/PlayerStats/Hur.png', Precision=0.9, Region=(
            StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3]))
        if HasHur[0] != 0 and HasHur[1] != 0:
            return False
        else:
            return True

