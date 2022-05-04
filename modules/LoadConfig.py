from engine.GUI import *

EnabledLoadConfig = False


class LoadConfig:
    def __init__(self, root):
        self.LoadConfig = GUI('LoadConfig', 'Module: Load Config')
        self.LoadConfig.DefaultWindow('DefaultWindow')

        def SetLoadConfig():
            global EnabledLoadConfig
            if not EnabledLoadConfig:
                EnabledLoadConfig = True
                ButtonEnabled.configure(text='LoadConfig: ON')
                ScanLoadConfig()
            else:
                EnabledLoadConfig = False
                ButtonEnabled.configure(text='LoadConfig: OFF')

        def ScanLoadConfig():
            if EnabledLoadConfig:
                print("Try Lock LoadConfig")
                print("Try This")

            root.after(300, ScanLoadConfig)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.LoadConfig.addButton('Ok', self.LoadConfig.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledLoadConfig
        if not EnabledLoadConfig:
            ButtonEnabled = self.LoadConfig.addButton('LoadConfig: OFF', SetLoadConfig, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.LoadConfig.addButton('LoadConfig: ON', SetLoadConfig, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.LoadConfig.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.LoadConfig.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.LoadConfig.loop()

