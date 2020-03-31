import json
import time

from Engine.CheckWaypoint import *
from Engine.SetFollow import SetFollow
from Engine.NumberOfTargets import NumberOfTargets
from Engine.AttackTarget import AttackTarget
from Engine.CheckWaypoint import CheckWaypoint


def EngineCaveBot(data, i, mini_map, battle_location, monster_name, SQMs):
    locate_mark = pyautogui.locateOnScreen('images/MapSettings/' + data[i]["mark"] + '.png',
                                           region=(mini_map[0], mini_map[1], mini_map[2], mini_map[3]),
                                           confidence=0.9)
    locate_mark2 = pyautogui.center(locate_mark)
    target_number = NumberOfTargets(battle_location, monster_name)
    print("Localized: ", data[i]["mark"])
    if data[i]['status'] and locate_mark2 is not None:
        mp = pyautogui.position()
        pyautogui.click(locate_mark2[0], locate_mark2[1])
        pyautogui.moveTo(mp)
        while target_number > 0:
            follow_x_pos, follow_y_pos = SetFollow()

            if follow_x_pos != 0 and follow_y_pos != 0:
                past_mouse_position = pyautogui.position()
                pyautogui.leftClick(follow_x_pos, follow_y_pos)
                pyautogui.moveTo(past_mouse_position)

            AttackTarget(monster_name, battle_location, SQMs, target_number)
            break

        print("waiting 0.2 seconds")
        time.sleep(2)
        if CheckWaypoint(data[i]["mark"], mini_map):
            data[i]['status'] = False
            if i+1 == len(data):
                data[i-i]['status'] = True
            else:
                data[i+1]['status'] = True
            with open('Scripts/ratThais.json', 'w') as wJson:
                json.dump(data, wJson, indent=4)
        else:
            EngineCaveBot(data, i, mini_map, battle_location, monster_name, SQMs)
    else:
        print("Error to locate: " + data[i]["mark"])
