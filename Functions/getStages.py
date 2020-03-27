import pyautogui


class GetStage:
    def __init__(self, name):
        self.stage = 0
        self.name = name

    def scanning_stage(self, Localization, color, colorFull):
        for i in range(100, 0, -5):
            if pyautogui.pixelMatchesColor(Localization[0] + i, Localization[1], (colorFull[0], colorFull[1], colorFull[2])):
                self.stage = i
                print(f"Get {self.name}: {self.stage}%")
                return self.stage
            elif pyautogui.pixelMatchesColor(Localization[0] + i, Localization[1], (color[0], color[1], color[2])):
                self.stage = i
                print(f"Get {self.name}: {self.stage}%")
                return self.stage

