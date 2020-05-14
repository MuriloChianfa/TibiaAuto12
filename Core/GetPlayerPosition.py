import pyautogui


def GetPlayerPosition(HOOK_OPTION):
    gameWindow = [0, 0, 0, 0]
    Player = [0, 0]
    left_gw = [0, 0]
    right_gw = [0, 0]
    button_gw = [0, 0]

    if HOOK_OPTION == 0:

        left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption1.png", confidence=0.8)
        if left_gw is None:
            left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption2.png", confidence=0.8)
    
        if left_gw is None:
            left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption3.png", confidence=0.8)
    
        try:
            gameWindow[0] = int(left_gw[0])
            gameWindow[1] = int(left_gw[1])
        except Exception as errno:
            print("?Error On ", errno)
    
        right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption1.png", confidence=0.8)
        if right_gw is None:
            right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption2.png", confidence=0.8)
    
        if right_gw is None:
            right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption3.png", confidence=0.8)
    
        if right_gw is None:
            right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption4.png", confidence=0.8)
        try:
            gameWindow[2] = int(right_gw[0])
        except Exception as errno:
            print("?Error On ", errno)
    
        button_gw = pyautogui.locateOnScreen("images/PlayerSettings/EndLocation.png", confidence=0.8)
        if button_gw is None:
            print("BUTTON GAME WINDOWS IS NONE")
        else:
            gameWindow[3] = int(button_gw[1])

        if gameWindow[0] != 0 and gameWindow[2] != 0:
            Player[0] = int(((gameWindow[2] - gameWindow[0]) / 2) + gameWindow[0])
        else:
            print("X GAME WINDOW ERROR")
            x, y = pyautogui.size()
            Player[0] = x / 2

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

    elif HOOK_OPTION == 1:
        from Engine.HookWindow import LocateImage

        left_gw[0], left_gw[1] = LocateImage("images/PlayerSettings/LeftOption1.png", Precision=0.75)
        if left_gw[0] == 0 and left_gw[1] == 0:
            left_gw[0], left_gw[1] = LocateImage("images/PlayerSettings/LeftOption2.png", Precision=0.75)

        if left_gw[0] == 0 and left_gw[1] == 0:
            left_gw[0], left_gw[1] = LocateImage("images/PlayerSettings/LeftOption3.png", Precision=0.75)

        try:
            gameWindow[0] = int(left_gw[0])
            gameWindow[1] = int(left_gw[1])
        except Exception as errno:
            print("?Error On ", errno)

        right_gw[0], right_gw[1] = LocateImage("images/PlayerSettings/RightOption1.png", Precision=0.75)
        if right_gw[0] == 0 and right_gw[1] == 0:
            right_gw[0], right_gw[1] = LocateImage("images/PlayerSettings/RightOption2.png", Precision=0.75)

        if right_gw[0] == 0 and right_gw[1] == 0:
            right_gw[0], right_gw[1] = LocateImage("images/PlayerSettings/RightOption3.png", Precision=0.75)

        if right_gw[0] == 0 and right_gw[1] == 0:
            right_gw[0], right_gw[1] = LocateImage("images/PlayerSettings/RightOption4.png", Precision=0.75)
        try:
            gameWindow[2] = int(right_gw[0])
        except Exception as errno:
            print("?Error On ", errno)

        button_gw[0], button_gw[1] = LocateImage("images/PlayerSettings/EndLocation.png", Precision=0.7)
        if button_gw[0] == 0 and button_gw[1] == 0:
            print("BUTTON GAME WINDOWS IS NONE")
        else:
            gameWindow[3] = int(button_gw[1])

        if gameWindow[0] != 0 and gameWindow[2] != 0:
            Player[0] = int(((gameWindow[2] - gameWindow[0]) / 2) + gameWindow[0])
        else:
            print("X GAME WINDOW ERROR")
            x, y = pyautogui.size()
            Player[0] = x / 2

        if gameWindow[1] != 0 and gameWindow[3] != 0:
            Player[1] = int(((gameWindow[3] - gameWindow[1]) / 2) + gameWindow[1])
        else:
            print("Y GAME WINDOW ERROR")
            x, y = pyautogui.size()
            print(x, y)
            Player[1] = y / 2

        if Player[1] != 0:
            return Player[0], Player[1], gameWindow[0], gameWindow[1], gameWindow[2], gameWindow[3]
        else:
            print("Error To Get Player Position !!!")
            return 0, 0, 0, 0, 0, 0
