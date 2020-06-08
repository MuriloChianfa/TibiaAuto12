from Core.HookWindow import LocateCenterImage


def ScanTarget(BattlePosition, monster):
    has_target = [0, 0]

    has_target[0], has_target[1] = LocateCenterImage('images/Targets/' + monster + '.png', Precision=0.86, Region=(
        BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))

    if has_target[0] != 0 and has_target[1] != 0:
        if has_target[0] < BattlePosition[0]:
            return (BattlePosition[0] - 30) + has_target[0] + 1, has_target[1] + BattlePosition[1] + 1
        else:
            return (BattlePosition[0] - 40) + has_target[0] + 1, has_target[1] + BattlePosition[1] + 1
    else:
        return 0, 0
