def NumberOfTargets(BattlePosition, monster, HOOK_OPTION):
    if HOOK_OPTION == 0:
        import pyautogui

        target_number = list(pyautogui.locateAllOnScreen('images/Targets/' + monster + '.png', confidence=0.8, region=(
            BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3])))
        if target_number:
            return len(target_number)
        else:
            return 0

    elif HOOK_OPTION == 1:
        from HookWindow import LocateAllImages

        target_number = LocateAllImages('images/Targets/' + monster + '.png', Precision=0.8, Region=(
            BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))

        if target_number > 0:
            return target_number
        else:
            return 0
