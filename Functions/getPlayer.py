import pyautogui

class GetPlayerPosition:
    def get_player_pos():
        window_X, window_Y = pyautogui.size()
        print(window_X, window_Y)
        global player_X, player_Y
        player_X = int(window_X) / 2
        player_Y = (int(window_Y) / 2) - 100
        print("X Player Position Is: ", player_X)
        print("Y Player Position Is: ", player_Y)
        if player_X and player_Y is not None:
            return player_X, player_Y
        else:
            print("Error To Get Player Position !!!")
            return None

