import pyautogui

from Engine.TakeLoot import GetLoot
from Engine.ScanTarget import ScanTarget
from Engine.NumberOfTargets import NumberOfTargets
from Engine.IsAttacking import IsAttacking

global monster
Target = [0, 0]


def AttackTarget(monster, BattlePosition, SQMs, TargetNumber):
    Target[0], Target[1] = ScanTarget(BattlePosition, monster)
    TargetNumber2 = NumberOfTargets(BattlePosition, monster)
    print("Number of " + monster + ": ", TargetNumber2)
    if TargetNumber2 < TargetNumber:
        GetLoot('Right').TakeLoot(SQMs)

    if Target[0] != 0 and Target[1] != 0:
        attacking = IsAttacking(BattlePosition)
        TargetNumber = NumberOfTargets(BattlePosition, monster)
        TargetNumber = int(TargetNumber)
        if not attacking:
            print("Attacking a Target")
            past_mouse_position = pyautogui.position()
            pyautogui.leftClick(Target[0], Target[1])
            pyautogui.moveTo(past_mouse_position)
            TargetNumber2 = NumberOfTargets(BattlePosition, monster)
            if TargetNumber is not None:
                return TargetNumber
            else:
                return 0
                
        else:
            print("You are attacking")
            TargetNumber2 = NumberOfTargets(BattlePosition, monster)
            if TargetNumber is not None:
                return TargetNumber
            else:
                return 0
    else:
        return 0

