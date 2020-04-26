from Engine.GUI import *

EnabledAutoSeller = False


class AutoSeller:
    def __init__(self, root):
        self.AutoSeller = GUI('AutoSeller', 'Module: Auto Seller')
        self.AutoSeller.DefaultWindow('AutoSeller', [414, 783], [1.2, 2.29])

        self.AutoSeller.loop()

