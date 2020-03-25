import pyautogui


class GetTargetPosition:
    def find_battle():
        battle_initial_position = pyautogui.locateOnScreen('images/BattleList.png', grayscale=True, confidence=0.8)
        print("Your Battle location is:", battle_initial_position)
        battle_start_x, battle_start_y = pyautogui.center(battle_initial_position)
        battle_start_x = battle_start_x - 40
        battle_start_y = battle_start_y - 5
        battle_end_x = int(battle_start_x) + 155
        battle_end_y = int(battle_start_y) + 415
        return int(battle_start_x), int(battle_end_x), int(battle_start_y), int(battle_end_y)

    def scanning_for_target(battle_log, battle_start_x, battle_end_x, battle_start_y, battle_end_y, monster):
        has_target = pyautogui.locateOnScreen('images/Targets/' + monster + '.png', confidence=0.8, region=(
            battle_start_x, battle_start_y, battle_end_x, battle_end_y))
        none = 0
        if has_target:
            target_x, target_y = pyautogui.center(has_target)
            return target_x - 41, target_y
        else:
            return 0, 0

    def attaking(battle_log, battle_start_x, battle_end_x, battle_start_y, battle_end_y):
        attaking = pyautogui.locateOnScreen('images/attacking.png', confidence=0.8, region=(
            battle_start_x, battle_start_y, battle_end_x, battle_end_y))
        attaking2 = pyautogui.locateOnScreen('images/attacking2.png', confidence=0.8, region=(
            battle_start_x, battle_start_y, battle_end_x, battle_end_y))
        if attaking or attaking2:
            return True
        else:
            return False

# --------------------------- Arrumar Depois ------------------------------

    def scanning_follow_mode():
        follow = pyautogui.locateOnScreen('images/follow.png', confidence=0.8, region=(0, 0, 1826, 1024))
        if follow:
            follow_x, follow_y = pyautogui.center(follow)
            follow_x = int(follow_x)
            follow_y = int(follow_y)
            print("Clicking in Follow")
            return follow_x, follow_y
        else:
            return 0, 0

    '''
    
    def get_monster_list():
        targets = gui.config.get('MONSTERS', 'list').split(', ')
        targets = map(lambda target:target.replace(" ", "_"), targets)
        targets = map(lambda target: 'assets/monsters/'+target+'.png', targets)
        return list(targets)
        
        '''