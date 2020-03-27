import pyautogui


class GetPlayerPosition:
    def __init__(self):
        self.gameWindow = [0, 0, 0, 0]
        self.left_gw = None
        self.right_gw = None
        self.button_gw = None
        self.player_pos = [0, 0]

    ''' gw = Game Window'''

    def get_gw_xy(self):
        self.left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption1.png", confidence=0.8)
        if self.left_gw is None:
            self.left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption2.png", confidence=0.8)
        elif self.left_gw is None:
            self.left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption3.png", confidence=0.8)
        else:
            self.gameWindow[0] = int(self.left_gw[0])
            self.gameWindow[1] = int(self.left_gw[1])
            print(f"Left Game Window Localized In [ X: {self.gameWindow[0]}, Y: {self.gameWindow[1]} ]")

        self.right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption1.png", confidence=0.8)
        if self.right_gw is None:
            self.right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption2.png", confidence=0.8)
        elif self.right_gw is None:
            self.right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption3.png", confidence=0.8)
        elif self.right_gw is None:
            self.right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption4.png", confidence=0.8)
        else:
            self.gameWindow[2] = int(self.right_gw[0])
            print(f"Right Game Window Localized In [ X: {self.gameWindow[2]}, Y: {self.gameWindow[1]}]")

        self.button_gw = pyautogui.locateOnScreen("images/PlayerSettings/EndLocation.png", confidence=0.8)
        if self.button_gw is None:
            print("BUTTON GAME WINDOWS IS NONE")
        else:
            self.gameWindow[3] = int(self.button_gw[1])
            print(f"Left Button Game Window Localized In [ X: {self.gameWindow[0]}, Y: {self.gameWindow[3]}]")
            print(f"Right Button Game Window Localized In [ X: {self.gameWindow[2]}, Y: {self.gameWindow[3]}]")

        self.player_pos[0] = 0
        if self.gameWindow[0] != 0 and self.gameWindow[2] != 0:
            self.player_pos[0] = int(((self.gameWindow[2] - self.gameWindow[0]) / 2) + self.gameWindow[0])
        else:
            print("X GAME WINDOW ERROR")
            x, y = pyautogui.size()
            self.player_pos[0] = x / 2

        self.player_pos[1] = 0
        if self.gameWindow[1] != 0 and self.gameWindow[3] != 0:
            self.player_pos[1] = int(((self.gameWindow[3] - self.gameWindow[1]) / 2) + self.gameWindow[1])
        else:
            print("Y GAME WINDOW ERROR")
            x, y = pyautogui.size()
            self.player_pos[1] = y / 2

        print("X Player Position Is: ", self.player_pos[0])
        print("Y Player Position Is: ", self.player_pos[1])
        if self.player_pos is not None:
            return self.player_pos[0], self.player_pos[1], self.gameWindow[0], self.gameWindow[1], self.gameWindow[2], self.gameWindow[3]
        else:
            print("Error To Get Player Position !!!")
            return None
