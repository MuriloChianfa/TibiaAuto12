from Engine.GUI import *

EnabledAutoFish = False


class AutoFish:
    def __init__(self, root):
        self.AutoFish = GUI('AutoFish', 'Module: Auto Fish')
        self.AutoFish.DefaultWindow('AutoFish', [257, 258], [1.2, 2.29])

        self.AutoFish.loop()

