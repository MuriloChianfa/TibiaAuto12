from Engine.GUI import *

EnabledPythonScripts = False


class PythonScripts:
    def __init__(self, root):
        self.PythonScripts = GUI('PythonScripts', 'Module: Python Scripts')
        self.PythonScripts.DefaultWindow('PythonScripts', [371, 374], [1.2, 2.29])

        self.PythonScripts.loop()

