import json
import time

from Engine.CheckWaypoint import *
from Engine.SetFollow import SetFollow
from Engine.NumberOfTargets import NumberOfTargets
from Engine.AttackTarget import AttackTarget
from Engine.CheckWaypoint import CheckWaypoint
from Engine.TakeLoot import GetLoot

TargetNumber = 0


def EngineCaveBot(data, i, MapPosition, BattlePosition, monster, SQMs):
    locate_mark = pyautogui.locateOnScreen('images/MapSettings/' + data[i]["mark"] + '.png',
                                           region=(MapPosition[0], MapPosition[1], MapPosition[2], MapPosition[3]),
                                           confidence=0.9)
    if locate_mark:
        locate_mark2 = pyautogui.center(locate_mark)
    else:
        print("Error To Locate Mark")
        locate_mark2 = None
    print("Localized: ", data[i]["mark"])
    if data[i]['status'] and locate_mark2 is not None:
        mp = pyautogui.position()
        pyautogui.click(locate_mark2[0], locate_mark2[1])
        pyautogui.moveTo(mp)
        number = NumberOfTargets(BattlePosition, monster)
        while number > 0:
            global TargetNumber
            TargetNumber = AttackTarget(monster, BattlePosition, SQMs, TargetNumber)

            follow_x_pos, follow_y_pos = SetFollow()

            if follow_x_pos != 0 and follow_y_pos != 0:
                past_mouse_position = pyautogui.position()
                pyautogui.leftClick(follow_x_pos, follow_y_pos)
                pyautogui.moveTo(past_mouse_position)

            time.sleep(0.3)

            TargetNumber2 = AttackTarget(monster, BattlePosition, SQMs, TargetNumber)

            if TargetNumber2 < TargetNumber:
                GetLoot('Right').TakeLoot(SQMs)

            time.sleep(0.3)

            number = NumberOfTargets(BattlePosition, monster)
            if number == 0:
                break

        if CheckWaypoint(data[i]["mark"], MapPosition):
            data[i]['status'] = False
            if i+1 == len(data):
                data[i-i]['status'] = True
            else:
                data[i+1]['status'] = True
            with open('Scripts/ratThais.json', 'w') as wJson:
                json.dump(data, wJson, indent=4)
        else:
            EngineCaveBot(data, i, MapPosition, BattlePosition, monster, SQMs)
    else:
        print("Error to locate: " + data[i]["mark"])

