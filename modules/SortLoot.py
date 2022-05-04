from engine.GUI import *

EnabledSortLoot = False


class SortLoot:
    def __init__(self, root):
        self.SortLoot = GUI('SortLoot', 'Module: Sort Loot')
        self.SortLoot.DefaultWindow('SortLoot', [414, 531], [1.2, 2.29])

        self.SortLoot.loop()

