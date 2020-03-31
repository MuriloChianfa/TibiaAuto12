from Engine.GUI import *

EnabledFPSChanger = False


class FPSChanger:
    def __init__(self, root):
        self.FPSChanger = GUI('FPSChanger', 'Module: FPS Changer')
        self.FPSChanger.DefaultWindow('DefaultWindow')

        def SetFPSChanger():
            global EnabledFPSChanger
            if not EnabledFPSChanger:
                EnabledFPSChanger = True
                ButtonEnabled.configure(text='FPSChanger: ON')
                ScanFPSChanger()
            else:
                EnabledFPSChanger = False
                ButtonEnabled.configure(text='FPSChanger: OFF')

        def ScanFPSChanger():
            if EnabledFPSChanger:
                print("Try Lock FPSChanger")
                print("Try This")

            root.after(300, ScanFPSChanger)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.FPSChanger.addButton('Ok', self.FPSChanger.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledFPSChanger
        if not EnabledFPSChanger:
            ButtonEnabled = self.FPSChanger.addButton('FPSChanger: OFF', SetFPSChanger, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.FPSChanger.addButton('FPSChanger: ON', SetFPSChanger, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.FPSChanger.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.FPSChanger.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.FPSChanger.loop()

