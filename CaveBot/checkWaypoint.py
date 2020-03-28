import pyautogui


class CheckWaypoint:
    def wpt_reached(self, wpt_image, map_positions):
        middle = 50
        middle_start = (map_positions[0] + middle, map_positions[1] + middle)
        middle_end = (map_positions[2] - middle, map_positions[3] - middle)
        wpt = pyautogui.locateOnScreen(f'{wpt_image}', region=(middle_start[0], middle_start[1], middle_end[0], middle_end[1]), confidence=0.9)
        if wpt:
            return True
        print("Não chegou na marcação: ", self)
        return False

