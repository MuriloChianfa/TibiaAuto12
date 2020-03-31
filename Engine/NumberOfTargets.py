import pyautogui


def NumberOfTargets(BattlePosition, monster):
    target_number = list(pyautogui.locateAllOnScreen('images/Targets/' + monster + '.png', confidence=0.8, region=(
        BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3])))
    return len(target_number)

