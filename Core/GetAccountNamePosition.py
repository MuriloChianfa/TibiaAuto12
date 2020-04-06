import pyautogui

AccountName = [0, 0]


def GetAccountNamePosition():
    login = pyautogui.locateOnScreen('images/TibiaSettings/AccountName.png', grayscale=True, confidence=0.9)
    if login is not None:
        AccountName[0], AccountName[1] = pyautogui.center(login)
        return AccountName[0], AccountName[1]
    else:
        return 0, 0

