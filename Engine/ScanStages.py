class ScanStages:
    def __init__(self, name, HOOK_OPTION):
        self.stage = 0
        self.name = name
        self.HOOK_OPTION = HOOK_OPTION

    def ScanStages(self, Localization, color, colorFull):
        if self.HOOK_OPTION == 0:
            import pyautogui

            if pyautogui.pixelMatchesColor(Localization[0] + 100, Localization[1],
                                           (colorFull[0], colorFull[1], colorFull[2])):
                self.stage = 100
                print(f"Get {self.name}: {self.stage}%")
                return self.stage
            else:
                for i in range(95, 5, -5):
                    if pyautogui.pixelMatchesColor(Localization[0] + i, Localization[1], (color[0], color[1], color[2])):
                        self.stage = i
                        print(f"Get {self.name}: {self.stage}%")
                        return self.stage

        elif self.HOOK_OPTION == 1:
            from Engine.HookWindow import PixelMatchesColor

            if PixelMatchesColor(Localization[0] + 100, Localization[1],
                                           (colorFull[0], colorFull[1], colorFull[2])):
                self.stage = 100
                print(f"Get {self.name}: {self.stage}%")
                return self.stage
            else:
                for i in range(95, 5, -5):
                    if PixelMatchesColor(Localization[0] + i, Localization[1], (color[0], color[1], color[2])):
                        self.stage = i
                        print(f"Get {self.name}: {self.stage}%")
                        return self.stage
