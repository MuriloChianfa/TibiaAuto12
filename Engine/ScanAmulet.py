def ScanAmulet(AmuletPositions, Amulet, HOOK_OPTION):
    HasAmulet = [0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        HasAmulet = pyautogui.locateOnScreen('images/Amulets/' + Amulet + '.png', confidence=0.9, region=(
            AmuletPositions[0], AmuletPositions[1], AmuletPositions[2], AmuletPositions[3]))
        if HasAmulet:
            return False
        else:
            return True

    elif HOOK_OPTION == 1:
        from HookWindow import LocateImage

        HasAmulet[0], HasAmulet[1] = LocateImage('images/Amulets/' + Amulet + '.png', Precision=0.9, Region=(
            AmuletPositions[0], AmuletPositions[1], AmuletPositions[2], AmuletPositions[3]))
        if HasAmulet[0] != 0 and HasAmulet[1] != 0:
            return False
        else:
            return True


def SearchForAmulet(Amulet, HOOK_OPTION):
    FoundAmulet = [0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        FoundAmulet = pyautogui.locateCenterOnScreen('images/Amulets/' + Amulet + '.png', confidence=0.9)
        if FoundAmulet:
            return FoundAmulet[0], FoundAmulet[1]
        else:
            return 0, 0

    elif HOOK_OPTION == 1:
        from HookWindow import LocateCenterImage

        FoundAmulet[0], FoundAmulet[1] = LocateCenterImage('images/Amulets/' + Amulet + '.png', Precision=0.9)
        if FoundAmulet[0] != 0 and FoundAmulet[1] != 0:
            return FoundAmulet[0], FoundAmulet[1]
        else:
            return 0, 0
