import pyautogui

ManaPositions = [0, 0]


def GetManaPosition():
    manaLocation = pyautogui.locateOnScreen('images/PlayerSettings/mana.png', grayscale=True, confidence=0.9)
    if manaLocation[0] != 0 and manaLocation[1] != 0:
        ManaPositions[0], ManaPositions[1] = pyautogui.center(manaLocation)
        return ManaPositions[0], ManaPositions[1]

