import pyautogui

BattlePositions = [0, 0, 0, 0]


def GetBattlePosition():
    battle_initial_position = pyautogui.locateOnScreen('images/TibiaSettings/BattleList.png', grayscale=True,
                                                       confidence=0.8)
    BattlePositions[0], BattlePositions[1] = pyautogui.center(battle_initial_position)
    BattlePositions[0] = BattlePositions[0] - 40
    BattlePositions[1] = BattlePositions[1] - 5
    BattlePositions[2] = int(BattlePositions[0]) + 155
    BattlePositions[3] = int(BattlePositions[1]) + 415
    return int(BattlePositions[0]), int(BattlePositions[1]), int(BattlePositions[2]), int(
        BattlePositions[3])

