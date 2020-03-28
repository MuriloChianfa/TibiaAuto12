import time
import json
import pyautogui
from CaveBot.checkWaypoint import *
from CaveBot.autoAttack import *
from Functions.getLoot import *
from Functions.getTarget import *


check_wpt = CheckWaypoint()


class CaveBot:
    def __init__(self):
        self.self = 0

    def cave_bot(self, data, i, mini_map):
        locate_mark = pyautogui.locateOnScreen('images/MapSettings/' + data[i]["mark"] + '.png',
                                         region=(mini_map[0], mini_map[1], mini_map[2], mini_map[3]), confidence=0.9)
        locate_mark2 = pyautogui.center(locate_mark)
        print(locate_mark)
        print(locate_mark2[0], locate_mark2[1])
        if data[i]['status'] and locate_mark2 is not None:
            mp = pyautogui.position()
            pyautogui.click(locate_mark2[0], locate_mark2[1])
            pyautogui.moveTo(mp)

            print("wating 5 seconds")
            time.sleep(5)
            if CheckWaypoint().wpt_reached(data[i]["mark"], mini_map):
                data[i]['status'] = False
                if i+1 == len(data):
                    data[i-i]['status'] = True
                else:
                    data[i+1]['status'] = True
                with open('CaveBot/Scripts/ratThais.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)
            else:
                CaveBot().cave_bot(data, i, mini_map)
        else:
            print("Error to locate: " + data[i]["mark"])
