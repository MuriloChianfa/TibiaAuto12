import pyautogui


class SetFollow:
    def __init__(self):
        self.follow = None
        self.follow_x = 0
        self.follow_y = 0

    def SetFollow(self):
        self.follow = pyautogui.locateOnScreen('images/TibiaSettings/follow.png', confidence=0.8)
        if self.follow:
            self.follow_x, self.follow_y = pyautogui.center(self.follow)
            self.follow_x = int(self.follow_x)
            self.follow_y = int(self.follow_y)
            print("Clicking in Follow")
            return self.follow_x, self.follow_y
        else:
            return 0, 0
