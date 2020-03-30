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

    def cave_bot(self, data, i, mini_map, battle_location, monster_name, SQMs):
        locate_mark = pyautogui.locateOnScreen('images/MapSettings/' + data[i]["mark"] + '.png',
                                         region=(mini_map[0], mini_map[1], mini_map[2], mini_map[3]), confidence=0.9)
        locate_mark2 = pyautogui.center(locate_mark)
        target_number = GetTargetPosition().number_of_targets(battle_location[0], battle_location[1],
                                                              battle_location[2], battle_location[3],
                                                              monster_name)
        print("Localized: ", data[i]["mark"])
        if data[i]['status'] and locate_mark2 is not None:
            mp = pyautogui.position()
            pyautogui.click(locate_mark2[0], locate_mark2[1])
            pyautogui.moveTo(mp)
            while target_number > 0:
                follow_x_pos, follow_y_pos = GetFollow().scanning_follow_mode()

                if follow_x_pos != 0 and follow_y_pos != 0:
                    past_mouse_position = pyautogui.position()
                    pyautogui.leftClick(follow_x_pos, follow_y_pos)
                    pyautogui.moveTo(past_mouse_position)

                AutoAttack().auto_attack(monster_name, battle_location, SQMs, target_number)
                break

            print("wating 0.2 seconds")
            time.sleep(2)
            if CheckWaypoint().wpt_reached(data[i]["mark"], mini_map):
                data[i]['status'] = False
                if i+1 == len(data):
                    data[i-i]['status'] = True
                else:
                    data[i+1]['status'] = True
                with open('CaveBot/Scripts/ratThais.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)
            else:
                CaveBot().cave_bot(data, i, mini_map, battle_location, monster_name, SQMs)
        else:
            print("Error to locate: " + data[i]["mark"])
