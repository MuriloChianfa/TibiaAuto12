import pyautogui

StatsPositions = [0, 0, 0, 0]


def GetStatsPosition():
    health = pyautogui.locateOnScreen('images/TibiaSettings/Stop.png', grayscale=True, confidence=0.9)
    if health[0] != 0 and health[1] != 0:
        StatsPositions[0] = health[0] - 117
        StatsPositions[1] = health[1] + 1
        StatsPositions[2] = StatsPositions[0] + 105
        StatsPositions[3] = StatsPositions[1] + 10
        return StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3]

