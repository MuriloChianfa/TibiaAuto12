def ScanTarget(BattlePosition, monster, HOOK_OPTION):
    has_target = [0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        has_target = pyautogui.locateOnScreen('images/Targets/' + monster + '.png', confidence=0.9, region=(
            BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))
        if has_target:
            Target = pyautogui.center(has_target)
            if Target[0] < BattlePosition[0]:
                return Target[0] - 30, Target[1]
            else:
                return Target[0] - 40, Target[1]
        else:
            return 0, 0

    elif HOOK_OPTION == 1:
        from Engine.HookWindow import LocateCenterImage

        has_target[0], has_target[1] = LocateCenterImage('images/Targets/' + monster + '.png', Precision=0.9, Region=(
            BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))

        if has_target[0] != 0 and has_target[1] != 0:
            if has_target[0] < BattlePosition[0]:
                return (BattlePosition[0] - 30) + has_target[0], has_target[1] + BattlePosition[1]
            else:
                return (BattlePosition[0] - 40) + has_target[0], has_target[1] + BattlePosition[1]
        else:
            return 0, 0
