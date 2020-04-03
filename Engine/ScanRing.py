import pyautogui

RingLocate = [0, 0]


def ScanRing(RingPositions):
    NoHasRing = pyautogui.locateOnScreen('images/PlayerStats/NoRing.png', confidence=0.9, region=(
        RingPositions[0], RingPositions[1], RingPositions[2], RingPositions[3]))
    if NoHasRing:
        return True
    else:
        return False


def SearchForRing(Ring):
    FoundRing = pyautogui.locateCenterOnScreen('images/Rings/' + Ring + '.png', confidence=0.9)
    if FoundRing:
        return FoundRing[0], FoundRing[1]
    else:
        return 0, 0

