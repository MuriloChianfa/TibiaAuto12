from Engine.GUI import *

EnabledTimedSpells = False


class TimedSpells:
    def __init__(self, root):
        self.TimedSpells = GUI('TimedSpells', 'Module: Timed Spells')
        self.TimedSpells.DefaultWindow('TimedSpells', [306, 473], [1.2, 2.29])

        self.TimedSpells.loop()
