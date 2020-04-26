from Engine.GUI import *

EnabledModules = False


class Modules:
    def __init__(self, root):
        self.Modules = GUI('Modules', 'Module: Modules')
        self.Modules.DefaultWindow('Modules', [351, 281], [1.2, 2.29])

        self.Modules.loop()

