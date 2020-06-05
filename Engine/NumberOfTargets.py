from Engine.HookWindow import LocateAllImages


def NumberOfTargets(BattlePosition, monster):
    target_number = LocateAllImages('images/Targets/' + monster + '.png', Precision=0.8, Region=(
        BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))

    if target_number > 0:
        return target_number
    else:
        return 0
