def GetHealthPosition(HOOK_OPTION):
    HealthPositions = [0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        health = pyautogui.locateOnScreen('images/PlayerSettings/health.png', grayscale=True, confidence=0.9)
        if health[0] != 0 and health[1] != 0:
            HealthPositions[0], HealthPositions[1] = pyautogui.center(health)
            return HealthPositions[0], HealthPositions[1]
    elif HOOK_OPTION == 1:
        from HookWindow import LocateCenterImage

        HealthPositions = LocateCenterImage('images/PlayerSettings/health.png', Precision=0.8)
        if HealthPositions[0] != 0 and HealthPositions[1] != 0:
            return HealthPositions[0], HealthPositions[1]
        else:
            return 0, 0
