import pyautogui


def ScanAmulet(AmuletPositions, Amulet):
    HasAmulet = pyautogui.locateOnScreen('images/Amulets/' + Amulet + '.png', confidence=0.9, region=(
        AmuletPositions[0], AmuletPositions[1], AmuletPositions[2], AmuletPositions[3]))
    if HasAmulet:
        return False
    else:
        return True


def SearchForAmulet(Amulet):
    FoundAmulet = pyautogui.locateCenterOnScreen('images/Amulets/' + Amulet + '.png', confidence=0.9)
    if FoundAmulet:
        return FoundAmulet[0], FoundAmulet[1]
    else:
        return 0, 0
