from Engine.TakeLoot import GetLoot
from Engine.ScanTarget import ScanTarget
from Engine.NumberOfTargets import NumberOfTargets
from Engine.IsAttacking import IsAttacking

from Conf.Hotkeys import Hotkey

global monster
Target = [0, 0]


def AttackTarget(monster, BattlePosition, SQMs, TargetNumber, MOUSE_OPTION, HOOK_OPTION):

    SendToClient = Hotkey(MOUSE_OPTION)

    Target[0], Target[1] = ScanTarget(BattlePosition, monster, HOOK_OPTION)
    TargetNumber = NumberOfTargets(BattlePosition, monster, HOOK_OPTION)
    print("Number of " + monster + ": ", TargetNumber)

    if Target[0] != 0 and Target[1] != 0:
        attacking = IsAttacking(BattlePosition, HOOK_OPTION, monster)
        TargetNumber = int(NumberOfTargets(BattlePosition, monster, HOOK_OPTION))
        if not attacking:
            print("Attacking a Target")

            if MOUSE_OPTION == 1:
                past_mouse_position = SendToClient.Position()
            else:
                past_mouse_position = [0, 0]

            SendToClient.LeftClick(Target[0], Target[1])

            if MOUSE_OPTION == 1:
                SendToClient.MoveTo(past_mouse_position[0], past_mouse_position[1])

            if TargetNumber is not None:
                return TargetNumber
            else:
                return 0

        else:
            print("You are attacking")
            TargetNumber = NumberOfTargets(BattlePosition, monster, HOOK_OPTION)
            if TargetNumber != 0:
                return TargetNumber
            else:
                return 0
    else:
        return 0
