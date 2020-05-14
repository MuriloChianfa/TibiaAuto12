import time


def GetBattlePosition(HOOK_OPTION):
    BattlePositions = [0, 0, 0, 0]
    if HOOK_OPTION == 0:
        import pyautogui
        battle_initial_position = pyautogui.locateOnScreen('images/TibiaSettings/BattleList.png', grayscale=True,
                                                           confidence=0.8)
        BattlePositions[0], BattlePositions[1] = pyautogui.center(battle_initial_position)
        BattlePositions[0] = BattlePositions[0] - 40
        BattlePositions[1] = BattlePositions[1] - 5
        BattlePositions[2] = int(BattlePositions[0]) + 155
        BattlePositions[3] = int(BattlePositions[1]) + 415
        return int(BattlePositions[0]), int(BattlePositions[1]), int(BattlePositions[2]), int(
            BattlePositions[3])

    elif HOOK_OPTION == 1:
        from Engine.HookWindow import LocateCenterImage

        BattlePositions[0], BattlePositions[1] = LocateCenterImage('images/TibiaSettings/BattleList.png', Precision=0.75)
        BattlePositions[0] = int(BattlePositions[0]) - 40
        BattlePositions[1] = int(BattlePositions[1]) - 5
        BattlePositions[2] = int(BattlePositions[0]) + 155
        BattlePositions[3] = int(BattlePositions[1]) + 415

        if BattlePositions[0] != 0 and BattlePositions[1] != 0:
            return int(BattlePositions[0]), int(BattlePositions[1]), int(BattlePositions[2]), int(
                BattlePositions[3])
        else:
            return 0, 0, 0, 0
