def GetMapPosition(HOOK_OPTION):
    MapPositions = [0, 0, 0, 0]
    if HOOK_OPTION == 0:
        import pyautogui

        top_right = pyautogui.locateOnScreen("images/MapSettings/MapSettings.png", confidence=0.8)
        map_size = 110  # 110px square
        MapPositions[0], MapPositions[1] = top_right[0] - map_size + 4, top_right[1] + 1
        MapPositions[2], MapPositions[3] = top_right[0] - 1, top_right[1] + map_size- 1
        if top_right[0] != -1:
            print(f"MiniMap Start [X: {MapPositions[0]}, Y: {MapPositions[1]}]")
            print(f"MiniMap End [X: {MapPositions[2]}, Y: {MapPositions[3]}]")
            print("")
            print(f"Size of MiniMap [X: {MapPositions[2] - MapPositions[0]}, Y: {MapPositions[3] - MapPositions[1]}]")
            return MapPositions[0], MapPositions[1], MapPositions[2], MapPositions[3]
        else:
            print("Error To Get Map Positions")
            return -1, -1, -1, -1

    elif HOOK_OPTION == 1:
        from HookWindow import LocateImage

        top_right = LocateImage("images/MapSettings/MapSettings.png", Precision=0.8)
        map_size = 110  # 110px square
        MapPositions[0], MapPositions[1] = top_right[0] - map_size + 4, top_right[1] + 1
        MapPositions[2], MapPositions[3] = top_right[0] - 1, top_right[1] + map_size - 1
        if top_right[0] != -1:
            print(f"MiniMap Start [X: {MapPositions[0]}, Y: {MapPositions[1]}]")
            print(f"MiniMap End [X: {MapPositions[2]}, Y: {MapPositions[3]}]")
            print("")
            print(f"Size of MiniMap [X: {MapPositions[2] - MapPositions[0]}, Y: {MapPositions[3] - MapPositions[1]}]")
            return MapPositions[0], MapPositions[1], MapPositions[2], MapPositions[3]
        else:
            print("Error To Get Map Positions")
            return -1, -1, -1, -1
