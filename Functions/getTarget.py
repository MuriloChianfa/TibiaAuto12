import pyautogui


class GetTargetPosition:
    def find_battle():
        battle_initial_position = pyautogui.locateOnScreen('images/TibiaSettings/BattleList.png', grayscale=True, confidence=0.8)
        print("Your Battle location is:", battle_initial_position)
        battle_start_x, battle_start_y = pyautogui.center(battle_initial_position)
        battle_start_x = battle_start_x - 40
        battle_start_y = battle_start_y - 5
        battle_end_x = int(battle_start_x) + 155
        battle_end_y = 415
        return int(battle_start_x), int(battle_end_x), int(battle_start_y), int(battle_end_y)

    def scanning_target(battle_log, battle_start_x, battle_end_x, battle_start_y, battle_end_y, monster):
        has_target = pyautogui.locateOnScreen('images/Targets/' + monster + '.png', confidence=0.9, region=(
            battle_start_x, battle_start_y, battle_end_x, battle_end_y))
        none = 0
        if has_target:
            target_x, target_y = pyautogui.center(has_target)
            target_x = target_x - 40
            if target_x < battle_start_x:
                return target_x + 10, target_y
            else:
                return target_x, target_y
        else:
            return 0, 0

    def number_of_targets(battle_log, battle_start_x, battle_end_x, battle_start_y, battle_end_y, monster):
        target_number = list(pyautogui.locateAllOnScreen('images/Targets/' + monster + '.png', confidence=0.8, region=(
            battle_start_x, battle_start_y, battle_end_x, battle_end_y)))
        return len(target_number)

    def attaking(battle_log, battle_start_x, battle_end_x, battle_start_y, battle_end_y):
        attaking = pyautogui.locateOnScreen('images/TibiaSettings/attacking.png', confidence=0.6, region=(
            battle_start_x - 10, battle_start_y, battle_end_x, battle_end_y))
        attaking2 = pyautogui.locateOnScreen('images/TibiaSettings/attacking2.png', confidence=0.6, region=(
            battle_start_x - 10, battle_start_y, battle_end_x, battle_end_y))
        if attaking or attaking2:
            return True
        else:
            return False


class GetFollow:
    def __init__(self):
        self.follow = None
        self.follow_x = 0
        self.follow_y = 0

    def scanning_follow_mode(self):
        self.follow = pyautogui.locateOnScreen('images/TibiaSettings/follow.png', confidence=0.8)
        if self.follow:
            self.follow_x, self.follow_y = pyautogui.center(self.follow)
            self.follow_x = int(self.follow_x)
            self.follow_y = int(self.follow_y)
            print("Clicking in Follow")
            return self.follow_x, self.follow_y
        else:
            return 0, 0
