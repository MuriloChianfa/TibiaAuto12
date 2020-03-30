import pyautogui


class GetHealthPosition:
    def __init__(self):
        self.health_location = [0, 0]

    def GetHealthPosition(self):
        health = pyautogui.locateOnScreen('images/PlayerSettings/health.png', grayscale=True, confidence=0.9)
        if health[0] != 0 and health[1] != 0:
            self.health_location[0], self.health_location[1] = pyautogui.center(health)
            return self.health_location[0], self.health_location[1]
