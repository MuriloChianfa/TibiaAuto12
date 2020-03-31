import pyautogui

gameWindow = [0, 0, 0, 0]
Player = [0, 0]


def GetPlayerPosition():
    left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption1.png", confidence=0.8)
    if left_gw is None:
        left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption2.png", confidence=0.8)
    elif left_gw is None:
        left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption3.png", confidence=0.8)
    else:
        gameWindow[0] = int(left_gw[0])
        gameWindow[1] = int(left_gw[1])

    right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption1.png", confidence=0.8)
    if right_gw is None:
        right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption2.png", confidence=0.8)
    elif right_gw is None:
        right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption3.png", confidence=0.8)
    elif right_gw is None:
        right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption4.png", confidence=0.8)
    else:
        gameWindow[2] = int(right_gw[0])

    button_gw = pyautogui.locateOnScreen("images/PlayerSettings/EndLocation.png", confidence=0.8)
    if button_gw is None:
        print("BUTTON GAME WINDOWS IS NONE")
    else:
        gameWindow[3] = int(button_gw[1])

    Player[0] = 0
    if gameWindow[0] != 0 and gameWindow[2] != 0:
        Player[0] = int(((gameWindow[2] - gameWindow[0]) / 2) + gameWindow[0])
    else:
        print("X GAME WINDOW ERROR")
        x, y = pyautogui.size()
        Player[0] = x / 2

    Player[1] = 0
    if gameWindow[1] != 0 and gameWindow[3] != 0:
        Player[1] = int(((gameWindow[3] - gameWindow[1]) / 2) + gameWindow[1])
    else:
        print("Y GAME WINDOW ERROR")
        x, y = pyautogui.size()
        Player[1] = y / 2

    if Player is not None:
        return Player[0], Player[1], gameWindow[0], gameWindow[1], gameWindow[2], gameWindow[3]
    else:
        print("Error To Get Player Position !!!")
        return 0, 0, 0, 0, 0, 0

