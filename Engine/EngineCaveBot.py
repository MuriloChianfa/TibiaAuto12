import json
import time

from Conf.Hotkeys import Hotkey

from Engine.SetFollow import SetFollow
from Engine.NumberOfTargets import NumberOfTargets
from Engine.AttackTarget import AttackTarget
from Engine.CheckWaypoint import CheckWaypoint
from Engine.TakeLoot import GetLoot

from Engine.HookWindow import LocateCenterImage

TargetNumber = 0


def EngineCaveBot(data, i, MapPosition, BattlePosition, monster, SQMs, MOUSE_OPTION, ScriptName):
    SendToClient = Hotkey(MOUSE_OPTION)

    MarkLocation = [0, 0]
    global TargetNumber

    time.sleep(3.5)

    while MarkLocation[0] == 0 and MarkLocation[1] == 0:
        MarkLocation[0], MarkLocation[1] = LocateCenterImage('images/MapSettings/' + data[i]["mark"] + '.png',
                                                             Region=(
                                                                 MapPosition[0], MapPosition[1], MapPosition[2],
                                                                 MapPosition[3]),
                                                             Precision=0.8)
        if MarkLocation[0] == 0 and MarkLocation[1] == 0:
            print("Mark: { ", data[i]["mark"], " } Not Located, Try Again")
            time.sleep(.3)
            SendToClient.Press('up_arrow')
            time.sleep(.1)
            SendToClient.Press('left_arrow')
            time.sleep(.7)
            SendToClient.Press('down_arrow')
            time.sleep(.1)
            SendToClient.Press('right_arrow')
            time.sleep(.1)
        else:
            print("successfully Located The Mark: { ", data[i]["mark"], " } Clicking On Your Position")
            MarkLocation[0] = MapPosition[0] + MarkLocation[0]
            MarkLocation[1] = MapPosition[1] + MarkLocation[1]

    if data[i]['status'] is True:

        if MOUSE_OPTION == 1:
            mp = SendToClient.Position()
        else:
            mp = [0, 0]
        SendToClient.LeftClick(MarkLocation[0], MarkLocation[1])
        if MOUSE_OPTION == 1:
            SendToClient.MoveTo(mp[0], mp[1])

        number = NumberOfTargets(BattlePosition, monster)

        while number > 0:
            TargetNumber = AttackTarget(monster, BattlePosition, SQMs, TargetNumber, MOUSE_OPTION)

            NeedFollow = SetFollow()

            if NeedFollow:
                print("Clicking in Follow")

                if MOUSE_OPTION == 1:
                    mp = SendToClient.Position()
                else:
                    mp = [0, 0]
                follow_x_pos, follow_y_pos = LocateCenterImage('images/TibiaSettings/follow.png', Precision=0.8)
                SendToClient.LeftClick(follow_x_pos, follow_y_pos)
                if MOUSE_OPTION == 1:
                    SendToClient.MoveTo(mp[0], mp[1])

            time.sleep(.2)

            TargetNumber2 = AttackTarget(monster, BattlePosition, SQMs, TargetNumber, MOUSE_OPTION)

            if TargetNumber2 < TargetNumber:
                GetLoot('right', MOUSE_OPTION).TakeLoot(SQMs)

            time.sleep(0.2)

            number = NumberOfTargets(BattlePosition, monster)

            if number == 0:
                break

        if CheckWaypoint(data[i]["mark"], MapPosition):
            data[i]['status'] = False
            if i + 1 == len(data):
                data[i - i]['status'] = True
                with open('Scripts/' + ScriptName + '.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)
            else:
                data[i + 1]['status'] = True
                with open('Scripts/' + ScriptName + '.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)
        else:
            EngineCaveBot(data, i, MapPosition, BattlePosition, monster, SQMs, MOUSE_OPTION, ScriptName)
    else:
        print("Error to locate: " + data[i]["mark"])
