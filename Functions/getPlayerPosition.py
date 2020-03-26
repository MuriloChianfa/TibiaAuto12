import pyautogui


class GetPlayerPosition:
    def __init__(self):
        self.start_gw_x = 0
        self.start_gw_y = 0
        self.end_gw_x = 0
        self.end_gw_y = 0
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
            self.start_gw_x = int(self.left_gw[0])
            self.start_gw_y = int(self.left_gw[1])
            print(f"Left Game Window Localized In [ X: {self.start_gw_x}, Y: {self.start_gw_y} ]")

        self.right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption1.png", confidence=0.8)
        if self.right_gw is None:
            self.right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption2.png", confidence=0.8)
        elif self.right_gw is None:
            self.right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption3.png", confidence=0.8)
        elif self.right_gw is None:
            self.right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption4.png", confidence=0.8)
        else:
            self.end_gw_x = int(self.right_gw[0])
            print(f"Right Game Window Localized In [ X: {self.end_gw_x}, Y: {self.start_gw_y}]")

        self.button_gw = pyautogui.locateOnScreen("images/PlayerSettings/EndLocation.png", confidence=0.8)
        if self.button_gw is None:
            print("BUTTON GAME WINDOWS IS NONE")
        else:
            self.end_gw_y = int(self.button_gw[1])
            print(f"Left Button Game Window Localized In [ X: {self.start_gw_x}, Y: {self.end_gw_y}]")
            print(f"Right Button Game Window Localized In [ X: {self.end_gw_x}, Y: {self.end_gw_y}]")

        self.player_pos[0] = 0
        if self.start_gw_x != 0 and self.end_gw_x != 0:
            self.player_pos[0] = int(((self.end_gw_x - self.start_gw_x) / 2) + self.start_gw_x)
        else:
            print("X GAME WINDOW ERROR")

        self.player_pos[1] = 0
        if self.start_gw_y != 0 and self.end_gw_y != 0:
            self.player_pos[1] = int(((self.end_gw_y - self.start_gw_y) / 2) + self.start_gw_y)
        else:
            print("Y GAME WINDOW ERROR")

        print("X Player Position Is: ", self.player_pos[0])
        print("Y Player Position Is: ", self.player_pos[1])
        if self.player_pos is not None:
            return self.player_pos[0], self.player_pos[1]
        else:
            print("Error To Get Player Position !!!")
            return None
