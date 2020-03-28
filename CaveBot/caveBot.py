import time
import json
import pyautogui
from CaveBot.checkWaypoint import *
from CaveBot.autoAttack import *


check_wpt = CheckWaypoint()

class CaveBot:
    def check_cave_bot(self, data, map_positions, i, monster_name, battle_location):
        mark_box = pyautogui.locateOnScreen(f'{data[i]["mark"]}', region=(
            map_positions[0], map_positions[1], map_positions[2], map_positions[3]), confidence=0.9)
        print(data[i]["mark"], data[i]["status"])
        if data[i]['status']:
            mark_box = pyautogui.locateOnScreen(f'{data[i]["mark"]}', region=(
                map_positions[0], map_positions[1], map_positions[2], map_positions[3]), confidence=0.9)

            attack = AutoAttack().auto_attack(monster_name, battle_location)
            while attack:
                print("attacking...")

            pyautogui.click(mark_box[0], mark_box[1])

            time.sleep(4)
            if not check_wpt.wpt_reached(data[i]["mark"], map_positions):
                pyautogui.click(mark_box[0], mark_box[1])
                CaveBot().check_cave_bot(data, map_positions, i, monster_name, battle_location)
            else:
                time.sleep(3)
                if pyautogui.locateOnScreen(data[i]["mark"], region=(
                        map_positions[0], map_positions[1], map_positions[2], map_positions[3]), confidence=0.9):
                    data[i]['status'] = False
                    if i + 1 >= len(data):
                        data[i - i]['status'] = True
                    else:
                        data[i + 1]['status'] = True
                    with open('CaveBot/Scripts/ratThais.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
        else:
            print("Readjusting Json")
            data[i - i]['status'] = False
            data[0]['status'] = True
            with open('CaveBot/Scripts/ratThais.json', 'w') as wJson:
                json.dump(data, wJson, indent=4)