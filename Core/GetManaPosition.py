import pyautogui


class GetManaPosition:
    def __init__(self):
        self.mana_location = [0, 0]

    def GetManaPosition(self):
        manaLocation = pyautogui.locateOnScreen('images/PlayerSettings/mana.png', grayscale=True, confidence=0.9)
        if manaLocation[0] != 0 and manaLocation[1] != 0:
            self.mana_location[0], self.mana_location[1] = pyautogui.center(manaLocation)
            return self.mana_location[0], self.mana_location[1]

