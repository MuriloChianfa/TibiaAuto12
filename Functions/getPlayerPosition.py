import pyautogui


class GetPlayerPosition:
    def __init__(self):
        self.player_pos = None

    def getxy(self):
        try:
            left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption1.png", confidence=0.8)
            if left_gw is None:
                left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption2.png", confidence=0.8)
            elif left_gw is None:
                left_gw = pyautogui.locateOnScreen("images/PlayerSettings/LeftOption3.png", confidence=0.8)
            else:
                left_gw_x = left_gw[0]
                left_gw_y = left_gw[1]
                print("Left Game Window Localized [ X: {0}, Y: {1} ]", left_gw_x, left_gw_y)
        except:
            print("????????")
        try:
            right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption1.png", confidence=0.8)
            if right_gw is None:
                right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption2.png", confidence=0.8)
            elif right_gw is None:
                right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption3.png", confidence=0.8)
            elif right_gw is None:
                right_gw = pyautogui.locateOnScreen("images/PlayerSettings/RightOption4.png", confidence=0.8)
            else:
                right_gw_x = right_gw[0]
                right_gw_y = right_gw[1]
                print("Right Game Window Localized [ X: {0}, Y: {1} ]", right_gw_x, right_gw_y)
        except:
            print("????????")

        print("X Player Position Is: ", self.player_pos[0])
        print("Y Player Position Is: ", self.player_pos[1])
        if self.player_pos is not None:
            return self.player_pos
        else:
            print("Error To Get Player Position !!!")
            return None
