from engine.GUI import *

EnabledSaveConfig = False


class SaveConfig:
    def __init__(self, root):
        self.SaveConfig = GUI('SaveConfig', 'Module: Save Config')
        self.SaveConfig.DefaultWindow('DefaultWindow')

        def SetSaveConfig():
            global EnabledSaveConfig
            if not EnabledSaveConfig:
                EnabledSaveConfig = True
                ButtonEnabled.configure(text='SaveConfig: ON')
                ScanSaveConfig()
            else:
                EnabledSaveConfig = False
                ButtonEnabled.configure(text='SaveConfig: OFF')

        def ScanSaveConfig():
            if EnabledSaveConfig:
                print("Try Lock SaveConfig")
                print("Try This")

            root.after(300, ScanSaveConfig)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.SaveConfig.addButton('Ok', self.SaveConfig.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledSaveConfig
        if not EnabledSaveConfig:
            ButtonEnabled = self.SaveConfig.addButton('SaveConfig: OFF', SetSaveConfig, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.SaveConfig.addButton('SaveConfig: ON', SetSaveConfig, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.SaveConfig.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.SaveConfig.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.SaveConfig.loop()

