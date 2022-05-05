from core.GUI import *


class AdjustConfig:
    def __init__(self, root):
        self.AdjustConfig = GUI('AdjustConfig', 'Module: Adjust Config')
        self.AdjustConfig.DefaultWindow('AdjustConfig', [830, 616], [2.25, 2.40])

        def ScanAdjustConfig():
            print("Try Lock AdjustConfig")
            print("Try This")

        self.AdjustConfig.addButton('Ok', self.AdjustConfig.destroyWindow, [810, 25], [10, 580])

        self.AdjustConfig.loop()

