import pyautogui


def CheckWaypoint(image, map_positions):
    middle_start = (map_positions[0] + 50, map_positions[1] + 50)
    middle_end = (map_positions[2] - 50, map_positions[3] - 50)
    wpt = pyautogui.locateOnScreen('images/MapSettings/' + image + '.png',
                                   region=(middle_start[0], middle_start[1], middle_end[0], middle_end[1]),
                                   confidence=0.9, grayscale=True)
    if wpt:
        print("Chegou Na Marcação:", image)
        return True
    else:
        print("Não Chegou Na Marcação: ", image)
        return False
