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
        from Engine.HookWindow import LocateBoolRGBImage

        if LocateBoolRGBImage('images/MonstersAttack/' + MonsterName + '1.png', Region=(BattlePosition[0] - 1, BattlePosition[1] - 1, BattlePosition[2], BattlePosition[3]), Precision=0.8):
            return True
        elif LocateBoolRGBImage('images/MonstersAttack/' + MonsterName + '2.png', Region=(BattlePosition[0] - 1, BattlePosition[1] - 1, BattlePosition[2], BattlePosition[3]), Precision=0.8):
            return True
        else:
            return False
