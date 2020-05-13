def IsAttacking(BattlePosition, HOOK_OPTION):
    IsAttaking = [0, 0]
    IsAttaking2 = [0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        IsAttaking = pyautogui.locateOnScreen('images/TibiaSettings/attacking.png', confidence=0.6, region=(
            BattlePosition[0] - 10, BattlePosition[1], BattlePosition[2], BattlePosition[3]))
        IsAttaking2 = pyautogui.locateOnScreen('images/TibiaSettings/attacking2.png', confidence=0.6, region=(
            BattlePosition[0] - 10, BattlePosition[1], BattlePosition[2], BattlePosition[3]))
        if IsAttaking or IsAttaking2:
            return True
        else:
            return False

    elif HOOK_OPTION == 1:
        from HookWindow import LocateImage
        try:
            IsAttaking[0], IsAttaking[1] = LocateImage('images/TibiaSettings/attacking.png', Precision=0.8, Region=(
                BattlePosition[0] - 10, BattlePosition[1], BattlePosition[2], BattlePosition[3]))
            IsAttaking2[0], IsAttaking2[1] = LocateImage('images/TibiaSettings/attacking2.png', Precision=0.8, Region=(
                BattlePosition[0] - 10, BattlePosition[1], BattlePosition[2], BattlePosition[3]))
        except Exception:
            IsAttaking[0] = 0
            IsAttaking[1] = 0
            IsAttaking2[0] = 0
            IsAttaking2[1] = 0
            pass

        print("IsAttaking", IsAttaking[0], IsAttaking[1])
        print("IsAttaking2", IsAttaking2[0], IsAttaking2[1])
        print("BattlePosition", BattlePosition[0] - 10, BattlePosition[1], BattlePosition[2], BattlePosition[3])
        if IsAttaking[0] != 0 or IsAttaking[1] != 0:
            return True
        elif IsAttaking2[0] != 0 or IsAttaking2[1] != 0:
            return True
        else:
            return False
