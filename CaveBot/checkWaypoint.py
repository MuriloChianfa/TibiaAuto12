import pyautogui


class CheckWaypoint:
    def wpt_reached(self, minimap_pos):
        middle = 50
        middle_start = (minimap_pos[0] + middle, minimap_pos[1] + middle)
        middle_end = (minimap_pos[2] - middle, minimap_pos[3] - middle)
        wpt = pyautogui.locateOnScreen(self, region=(middle_start[0], middle_start[1], middle_end[0], middle_end[1]), confidence=0.9)
        if wpt[0] is not -1:
            return True
        print("Não chegou na marcação: ", self)
        return False

