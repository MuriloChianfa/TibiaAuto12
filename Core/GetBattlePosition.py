import pyautogui


class GetBattlePosition:
    def __init__(self):
        self.battle_location = [0, 0, 0, 0]

    def get_battle_xy(self):
        battle_initial_position = pyautogui.locateOnScreen('images/TibiaSettings/BattleList.png', grayscale=True,
                                                           confidence=0.8)
        print("Your Battle location is:", battle_initial_position)
        self.battle_location[0], self.battle_location[1] = pyautogui.center(battle_initial_position)
        self.battle_location[0] = self.battle_location[0] - 40
        self.battle_location[1] = self.battle_location[1] - 5
        self.battle_location[2] = int(self.battle_location[0]) + 155
        self.battle_location[3] = int(self.battle_location[1]) + 415
        return int(self.battle_location[0]), int(self.battle_location[1]), int(self.battle_location[2]), int(
            self.battle_location[3])

