from Engine.GUI import *

EnabledGeneralOptions = False


class GeneralOptions:
    def __init__(self, root):
        self.GeneralOptions = GUI('GeneralOptions', 'Module: General Options')
        self.GeneralOptions.DefaultWindow('DefaultWindow')

        def SetGeneralOptions():
            global EnabledGeneralOptions
            if not EnabledGeneralOptions:
                EnabledGeneralOptions = True
                ButtonEnabled.configure(text='GeneralOptions: ON')
                ScanGeneralOptions()
            else:
                EnabledGeneralOptions = False
                ButtonEnabled.configure(text='GeneralOptions: OFF')

        def ScanGeneralOptions():
            if EnabledGeneralOptions:
                print("Try Lock GeneralOptions")
                print("Try This")

            root.after(300, ScanGeneralOptions)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.GeneralOptions.addButton('Ok', self.GeneralOptions.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledGeneralOptions
        if not EnabledGeneralOptions:
            ButtonEnabled = self.GeneralOptions.addButton('GeneralOptions: OFF', SetGeneralOptions, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.GeneralOptions.addButton('GeneralOptions: ON', SetGeneralOptions, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.GeneralOptions.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.GeneralOptions.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.GeneralOptions.loop()

