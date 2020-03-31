import pyautogui

HealthPositions = [0, 0]


def GetHealthPosition():
    health = pyautogui.locateOnScreen('images/PlayerSettings/health.png', grayscale=True, confidence=0.9)
    if health[0] != 0 and health[1] != 0:
        HealthPositions[0], HealthPositions[1] = pyautogui.center(health)
        return HealthPositions[0], HealthPositions[1]

