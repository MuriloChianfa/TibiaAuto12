import pyautogui

MapPositions = [0, 0, 0, 0]


def GetMapPosition():
    top_right = pyautogui.locateOnScreen("images/MapSettings/MapSettings.png", confidence=0.8)
    map_size = 110  # 110px square
    MapPositions[0], MapPositions[1] = top_right[0] - map_size + 4, top_right[1] + 1
    MapPositions[2], MapPositions[3] = top_right[0] - 1, top_right[1] + map_size- 1
    if top_right[0] != -1:
        print("Your MiniMap Location Is: ")
        print(f"Start X: {MapPositions[0]} Start Y: {MapPositions[1]}")
        print(f"End X: {MapPositions[2]} End Y: {MapPositions[3]}")
        print(f"Size of X: {MapPositions[2] - MapPositions[0]}")
        print(f"Size of Y: {MapPositions[3] - MapPositions[1]}")
        return MapPositions[0], MapPositions[1], MapPositions[2], MapPositions[3]
    else:
        print("Error to get Map positions")
        return -1, -1, -1, -1

