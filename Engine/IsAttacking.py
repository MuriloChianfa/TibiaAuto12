import pyautogui


def IsAttacking(BattlePosition):
    IsAttaking = pyautogui.locateOnScreen('images/TibiaSettings/attacking.png', confidence=0.6, region=(
        BattlePosition[0] - 10, BattlePosition[1], BattlePosition[2], BattlePosition[3]))
    IsAttaking2 = pyautogui.locateOnScreen('images/TibiaSettings/attacking2.png', confidence=0.6, region=(
        BattlePosition[0] - 10, BattlePosition[1], BattlePosition[2], BattlePosition[3]))
    if IsAttaking or IsAttaking2:
        return True
    else:
        return False

