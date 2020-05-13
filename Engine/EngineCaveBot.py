import json
import time
import pyautogui

from Engine.CheckWaypoint import *
from Engine.SetFollow import SetFollow
from Engine.NumberOfTargets import NumberOfTargets
from Engine.AttackTarget import AttackTarget
from Engine.CheckWaypoint import CheckWaypoint
from Engine.TakeLoot import GetLoot

TargetNumber = 0


def EngineCaveBot(data, i, MapPosition, BattlePosition, monster, SQMs, HOOK_OPTION):
    MarkLocation = [0, 0]
    global TargetNumber
    if HOOK_OPTION == 0:

        MarkLocation = pyautogui.locateCenterOnScreen('images/MapSettings/' + data[i]["mark"] + '.png',
                                                      region=(
                                                      MapPosition[0], MapPosition[1], MapPosition[2], MapPosition[3]),
                                                      confidence=0.8)
        if data[i]['status'] is True and MarkLocation is not None:
            mp = pyautogui.position()
            pyautogui.click(MarkLocation[0], MarkLocation[1])
            pyautogui.moveTo(mp)
            number = NumberOfTargets(BattlePosition, monster, HOOK_OPTION)
            time.sleep(2.5)
            while number > 0:
                TargetNumber = AttackTarget(monster, BattlePosition, SQMs, TargetNumber, HOOK_OPTION)

                follow_x_pos, follow_y_pos = SetFollow()

                if follow_x_pos != 0 and follow_y_pos != 0:
                    past_mouse_position = pyautogui.position()
                    pyautogui.leftClick(follow_x_pos, follow_y_pos)
                    pyautogui.moveTo(past_mouse_position)

                time.sleep(0.3)

                TargetNumber2 = AttackTarget(monster, BattlePosition, SQMs, TargetNumber, HOOK_OPTION)

                if TargetNumber2 < TargetNumber:
                    GetLoot('Right').TakeLoot(SQMs)

                time.sleep(0.3)

                number = NumberOfTargets(BattlePosition, monster, HOOK_OPTION)
                if number == 0:
                    break

            if CheckWaypoint(data[i]["mark"], MapPosition, HOOK_OPTION):
                data[i]['status'] = False
                if i+1 == len(data):
                    data[i-i]['status'] = True
                else:
                    data[i+1]['status'] = True
                with open('Scripts/ratThais.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)
            else:
                EngineCaveBot(data, i, MapPosition, BattlePosition, monster, SQMs, HOOK_OPTION)
        else:
            print("Error to locate: " + data[i]["mark"])

    elif HOOK_OPTION == 1:
        from HookWindow import LocateCenterImage
        try:
            MarkLocation[0], MarkLocation[1] = LocateCenterImage('images/MapSettings/' + data[i]["mark"] + '.png',
                                                                 Region=(
                                                                     MapPosition[0], MapPosition[1], MapPosition[2],
                                                                     MapPosition[3]),
                                                                 Precision=0.83)
        except Exception:
            MarkLocation[0] = 0
            MarkLocation[1] = 0
            pass
        MarkLocation[0] = MapPosition[0] + MarkLocation[0]
        MarkLocation[1] = MapPosition[1] + MarkLocation[1] + 24
        if data[i]['status'] is True and MarkLocation[0] != 0 and MarkLocation[1] != 0:
            mp = pyautogui.position()
            pyautogui.click(MarkLocation[0], MarkLocation[1])
            pyautogui.moveTo(mp)
            try:
                number = NumberOfTargets(BattlePosition, monster, HOOK_OPTION)
            except Exception:
                number = 0
                pass
            time.sleep(2.5)
            while number > 0:
                try:
                    TargetNumber = AttackTarget(monster, BattlePosition, SQMs, TargetNumber, HOOK_OPTION)
                except Exception:
                    TargetNumber = 0
                    pass

                follow_x_pos, follow_y_pos = SetFollow()

                if follow_x_pos != 0 and follow_y_pos != 0:
                    past_mouse_position = pyautogui.position()
                    pyautogui.leftClick(follow_x_pos, follow_y_pos)
                    pyautogui.moveTo(past_mouse_position)

                time.sleep(0.3)

                try:
                    TargetNumber2 = AttackTarget(monster, BattlePosition, SQMs, TargetNumber, HOOK_OPTION)
                except Exception:
                    TargetNumber2 = 0
                    pass

                if TargetNumber2 < TargetNumber:
                    GetLoot('Right').TakeLoot(SQMs)

                time.sleep(0.3)

                try:
                    number = NumberOfTargets(BattlePosition, monster, HOOK_OPTION)
                except Exception:
                    number = 0
                    pass

                if number == 0:
                    break

            if CheckWaypoint(data[i]["mark"], MapPosition, HOOK_OPTION):
                data[i]['status'] = False
                if i + 1 == len(data):
                    data[i - i]['status'] = True
                else:
                    data[i + 1]['status'] = True
                with open('Scripts/ratThais.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)
            else:
                EngineCaveBot(data, i, MapPosition, BattlePosition, monster, SQMs, HOOK_OPTION)
        else:
            print("Error to locate: " + data[i]["mark"])
