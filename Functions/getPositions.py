import pyautogui


class GetHealthPosition:
    def __init__(self):
        self.health_location = [0, 0]

    def get_health_xy(self):
        health = pyautogui.locateOnScreen('images/PlayerSettings/health.png', grayscale=True, confidence=0.9)
        if health[0] != 0 and health[1] != 0:
            self.health_location[0], self.health_location[1] = pyautogui.center(health)
            return self.health_location[0], self.health_location[1]


class GetManaPosition:
    def __init__(self):
        self.mana_location = [0, 0]

    def get_mana_xy(self):
        manaLocation = pyautogui.locateOnScreen('images/PlayerSettings/mana.png', grayscale=True, confidence=0.9)
        if manaLocation[0] != 0 and manaLocation[1] != 0:
            self.mana_location[0], self.mana_location[1] = pyautogui.center(manaLocation)
            return self.mana_location[0], self.mana_location[1]

