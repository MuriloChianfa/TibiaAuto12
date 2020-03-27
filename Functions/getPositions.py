import pyautogui


class GetHealthPosition:
    def __init__(self):
        self.health_location = [0, 0]

    def get_health_xy(self):
        health = pyautogui.locateOnScreen('images/PlayerSettings/health.png', grayscale=True, confidence=0.9)
        if health[0] != 0 and health[1] != 0:
            self.health_location[0], self.health_location[1] = pyautogui.center(health)
            return self.health_location[0], self.health_location[1]


class GetManaPosition:
    def __init__(self):
        self.mana_location = [0, 0]

    def get_mana_xy(self):
        manaLocation = pyautogui.locateOnScreen('images/PlayerSettings/mana.png', grayscale=True, confidence=0.9)
        if manaLocation[0] != 0 and manaLocation[1] != 0:
            self.mana_location[0], self.mana_location[1] = pyautogui.center(manaLocation)
            return self.mana_location[0], self.mana_location[1]


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
        return int(self.battle_location[0]), int(self.battle_location[1]), int(self.battle_location[2]), int(self.battle_location[3])

