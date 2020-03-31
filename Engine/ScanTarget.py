import pyautogui


def ScanTarget(BattlePosition, monster):
    has_target = pyautogui.locateOnScreen('images/Targets/' + monster + '.png', confidence=0.9, region=(
        BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))
    if has_target:
        Target = pyautogui.center(has_target)
        Target[0] = Target[0] - 40
        if Target[0] < BattlePosition[0]:
            return Target[0] + 10, Target[1]
        else:
            return Target[0], Target[1]
    else:
        return 0, 0

