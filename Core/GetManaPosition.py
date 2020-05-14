def GetManaPosition(HOOK_OPTION):
    ManaPositions = [0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        manaLocation = pyautogui.locateOnScreen('images/PlayerSettings/mana.png', grayscale=True, confidence=0.9)
        if manaLocation[0] != 0 and manaLocation[1] != 0:
            ManaPositions[0], ManaPositions[1] = pyautogui.center(manaLocation)
            return ManaPositions[0], ManaPositions[1]

    elif HOOK_OPTION == 1:
        from Engine.HookWindow import LocateCenterImage

        ManaPositions = LocateCenterImage('images/PlayerSettings/mana.png', Precision=0.9)
        if ManaPositions[0] != 0 and ManaPositions[1] != 0:
            return ManaPositions[0], ManaPositions[1]

