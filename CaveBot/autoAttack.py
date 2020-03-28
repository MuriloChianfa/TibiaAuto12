import pyautogui
import time
from Functions.getTarget import *
from Main import get_SQMs_location, SQMs
from Functions.getLoot import *
from Functions.getSQM import *


class AutoAttack:
    def __init__(self):
        self.Target = [0, 0]
        self.target_number = 0

    def auto_attack(self, monster_name, battle_location):
        self.Target[0], self.Target[1] = GetTargetPosition().scanning_target(battle_location[0], battle_location[1],
                                                                   battle_location[2], battle_location[3], monster_name)
        target_number2 = GetTargetPosition().number_of_targets(battle_location[0], battle_location[1],
                                                               battle_location[2], battle_location[3], monster_name)
        print("Number of " + monster_name + ": ", target_number2)
        if target_number2 < self.target_number:
            if get_SQMs_location:
                GetLoot('right').take_loot(SQMs)
                target_number = 0
            else:
                SetSQMs().set_SQMs()

        if self.Target[0] != 0 and self.Target[1] != 0:
            self.target_number = GetTargetPosition().number_of_targets(battle_location[0], battle_location[1],
                                                                  battle_location[2], battle_location[3], monster_name)

            attacking = GetTargetPosition().attaking(battle_location[0], battle_location[1], battle_location[2],
                                                     battle_location[3])

            if not attacking:
                print("Attacking a Target")
                past_mouse_position = pyautogui.position()
                pyautogui.leftClick(self.Target[0], self.Target[1])
                pyautogui.moveTo(past_mouse_position)
                target_number2 = GetTargetPosition().number_of_targets(battle_location[0], battle_location[1],
                                                                       battle_location[2], battle_location[3], monster_name)
            else:
                print("You are attacking")
                target_number2 = GetTargetPosition().number_of_targets(battle_location[0], battle_location[1],
                                                                       battle_location[2], battle_location[3], monster_name)