import pyautogui

from Engine.TakeLoot import GetLoot
from Engine.ScanTarget import ScanTarget
from Engine.NumberOfTargets import NumberOfTargets
from Engine.IsAttacking import IsAttacking

global monster
Target = [0, 0]


def AttackTarget(monster, BattlePosition, SQMs, target_number):
    Target[0], Target[1] = ScanTarget(BattlePosition, monster)
    target_number2 = NumberOfTargets(BattlePosition, monster)
    print("Number of " + monster + ": ", target_number2)
    if target_number2 < target_number:
        GetLoot('Right').TakeLoot(SQMs)
    if Target[0] != 0 and Target[1] != 0:
        attacking = IsAttacking(BattlePosition)
        target_number = NumberOfTargets(BattlePosition, monster)
        if not attacking:
            print("Attacking a Target")
            past_mouse_position = pyautogui.position()
            pyautogui.leftClick(Target[0], Target[1])
            pyautogui.moveTo(past_mouse_position)
            target_number2 = NumberOfTargets(BattlePosition, monster)
        else:
            print("You are attacking")
            target_number2 = NumberOfTargets(BattlePosition, monster)

