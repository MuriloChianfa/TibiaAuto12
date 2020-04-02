import pyautogui


def ScanHur(StatsPositions):
    HasHur = pyautogui.locateOnScreen('images/PlayerStats/Hur.png', confidence=0.9, region=(
        StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3]))
    if HasHur:
        return False
    else:
        return True

