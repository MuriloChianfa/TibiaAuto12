from Engine.GUI import *

EnabledAutoLooter = False


class AutoLooter:
    def __init__(self, root, Player, SQMs):
        self.AutoLooter = GUI('AutoLooter', 'Module: Auto Looter')
        self.AutoLooter.DefaultWindow('AutoLooter', [279, 447], [1.2, 2.29])

        self.AutoLooter.loop()

