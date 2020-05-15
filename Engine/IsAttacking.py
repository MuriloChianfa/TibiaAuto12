def IsAttacking(BattlePosition, HOOK_OPTION, MonsterName):
    IsAttaking = [0, 0]
    IsAttaking2 = [0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        IsAttaking = pyautogui.locateOnScreen('images/TibiaSettings/attacking.png', confidence=0.9, region=(
            BattlePosition[0] - 10, BattlePosition[1], BattlePosition[2], BattlePosition[3]))
        IsAttaking2 = pyautogui.locateOnScreen('images/TibiaSettings/attacking2.png', confidence=0.9, region=(
            BattlePosition[0] - 10, BattlePosition[1], BattlePosition[2], BattlePosition[3]))
        if IsAttaking or IsAttaking2:
            return True
        else:
            return False

    elif HOOK_OPTION == 1:
        # from Engine.HookWindow import LocateImage

        return False


'''IsAttaking[0], IsAttaking[1] = LocateImage('images/MonstersAttack/' + MonsterName + '1.png', Precision=0.8, Region=(
    BattlePosition[0] - 20, BattlePosition[1] - 1, BattlePosition[2], BattlePosition[3]))
if IsAttaking[0] != 0 and IsAttaking[1] != 0:
    return True
else:
    IsAttaking2[0], IsAttaking2[1] = LocateImage('images/MonstersAttack/' + MonsterName + '2.png', Precision=0.8, Region=(
        BattlePosition[0] - 20, BattlePosition[1] - 1, BattlePosition[2], BattlePosition[3]))
if IsAttaking2[0] != 0 and IsAttaking2[1] != 0:
    return True
else:
    return False'''
