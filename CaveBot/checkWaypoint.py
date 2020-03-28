import pyautogui


class CheckWaypoint:
    def wpt_reached(self, image, map_positions):
        middle_start = (map_positions[0] + 47, map_positions[1] + 48)
        middle_end = (map_positions[2] - 47, map_positions[3] - 48)
        wpt = pyautogui.locateOnScreen('images/MapSettings/' + image + '.png', region=(middle_start[0], middle_start[1], middle_end[0], middle_end[1]), confidence=0.9)
        if wpt:
            print("Chegou Na Marcação: ", image)
            print(wpt)
            print(len(wpt))
            return True
        print("Não Chegou Na Marcação: ", image)
        return False

