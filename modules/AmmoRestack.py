from engine.GUI import *

EnabledAmmoRestack = False


class AmmoRestack:
    def __init__(self, root):
        self.AmmoRestack = GUI('AmmoRestack', 'Module: Ammo Restack')
        self.AmmoRestack.DefaultWindow('AmmoRestack', [269, 544], [1.2, 2.29])

        self.AmmoRestack.loop()

