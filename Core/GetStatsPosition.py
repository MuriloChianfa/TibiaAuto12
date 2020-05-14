def GetStatsPosition(HOOK_OPTION):
    StatsPositions = [0, 0, 0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        stats = pyautogui.locateOnScreen('images/TibiaSettings/Stop.png', grayscale=True, confidence=0.9)
        if stats[0] != 0 and stats[1] != 0:
            StatsPositions[0] = stats[0] - 117
            StatsPositions[1] = stats[1] + 1
            StatsPositions[2] = StatsPositions[0] + 105
            StatsPositions[3] = StatsPositions[1] + 10
            return StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3]

    elif HOOK_OPTION == 1:
        from Engine.HookWindow import LocateImage

        StatsPositions[0], StatsPositions[1] = LocateImage('images/TibiaSettings/Stop.png', Precision=0.8)
        if StatsPositions[0] != 0 and StatsPositions[1] != 0:
            StatsPositions[0] = StatsPositions[0] - 117
            StatsPositions[1] = StatsPositions[1] + 1
            StatsPositions[2] = StatsPositions[0] + 105
            StatsPositions[3] = StatsPositions[1] + 10
            return StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3]
        else:
            return 0, 0, 0, 0
