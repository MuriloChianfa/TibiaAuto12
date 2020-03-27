import pyautogui


class GetMapPosition:
    def __init__(self):
        self.map_positions = [0, 0, 0, 0]

    def get_map_xy(self):
        top_right = pyautogui.locateOnScreen("images/MapSettings/MapSettings.png", confidence=0.8)
        map_size = 110  # 110px square
        self.map_positions[0], self.map_positions[1] = top_right[0] - map_size + 4, top_right[1] + 1
        self.map_positions[2], self.map_positions[3] = top_right[0] - 1, top_right[1] + map_size- 1
        if top_right[0] != -1:
            print("Your MiniMap Location Is: ")
            print(f"Start X: {self.map_positions[0]} Start Y: {self.map_positions[1]}")
            print(f"End X: {self.map_positions[2]} End Y: {self.map_positions[3]}")
            print(f"Size of X: {self.map_positions[2] - self.map_positions[0]}")
            print(f"Size of Y: {self.map_positions[3] - self.map_positions[1]}")
            return self.map_positions[0], self.map_positions[1], self.map_positions[2], self.map_positions[3]
        else:
            print("Error to get Map positions")
            return 0, 0, 0, 0

