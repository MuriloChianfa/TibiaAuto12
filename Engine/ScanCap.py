import pyautogui


def ScanCap(NumberBox, EndNumberBox):
    for i in range(9, -1, -1):
        FirstNumber = pyautogui.locateOnScreen('images/PlayerStats/Numbers/' + str(i) + '.png', region=(
            NumberBox[0], NumberBox[1], EndNumberBox[0], EndNumberBox[1]),
                                               confidence=0.93)
        if FirstNumber:
            return int(i)
