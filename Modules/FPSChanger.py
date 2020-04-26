from Engine.GUI import *

EnabledFPSChanger = False


class FPSChanger:
    def __init__(self, root):
        self.FPSChanger = GUI('FPSChanger', 'Module: FPS Changer')
        self.FPSChanger.DefaultWindow('FpsChanger', [224, 219], [1.2, 2.29])

        self.FPSChanger.loop()

