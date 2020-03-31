from Engine.GUI import *

EnabledAdjustConfig = False


class AdjustConfig:
    def __init__(self, root):
        self.AdjustConfig = GUI('AdjustConfig', 'Module: Adjust Config')
        self.AdjustConfig.DefaultWindow('DefaultWindow')

        def SetAdjustConfig():
            global EnabledAdjustConfig
            if not EnabledAdjustConfig:
                EnabledAdjustConfig = True
                ButtonEnabled.configure(text='AdjustConfig: ON')
                ScanAdjustConfig()
            else:
                EnabledAdjustConfig = False
                ButtonEnabled.configure(text='AdjustConfig: OFF')

        def ScanAdjustConfig():
            if EnabledAdjustConfig:
                print("Try Lock AdjustConfig")
                print("Try This")

            root.after(300, ScanAdjustConfig)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AdjustConfig.addButton('Ok', self.AdjustConfig.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAdjustConfig
        if not EnabledAdjustConfig:
            ButtonEnabled = self.AdjustConfig.addButton('AdjustConfig: OFF', SetAdjustConfig, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AdjustConfig.addButton('AdjustConfig: ON', SetAdjustConfig, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AdjustConfig.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AdjustConfig.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AdjustConfig.loop()

