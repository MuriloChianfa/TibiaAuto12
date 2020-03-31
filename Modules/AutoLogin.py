from Engine.GUI import *

EnabledAutoLogin = False


class AutoLogin:
    def __init__(self, root):
        self.AutoLogin = GUI('AutoLogin', 'Module: Auto Login')
        self.AutoLogin.DefaultWindow('DefaultWindow')

        def SetAutoLogin():
            global EnabledAutoLogin
            if not EnabledAutoLogin:
                EnabledAutoLogin = True
                ButtonEnabled.configure(text='AutoLogin: ON')
                ScanAutoLogin()
            else:
                EnabledAutoLogin = False
                ButtonEnabled.configure(text='AutoLogin: OFF')

        def ScanAutoLogin():
            if EnabledAutoLogin:
                print("Try Lock AutoLogin")
                print("Try This")

            root.after(300, ScanAutoLogin)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AutoLogin.addButton('Ok', self.AutoLogin.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledAutoLogin
        if not EnabledAutoLogin:
            ButtonEnabled = self.AutoLogin.addButton('AutoLogin: OFF', SetAutoLogin, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoLogin.addButton('AutoLogin: ON', SetAutoLogin, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoLogin.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.AutoLogin.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.AutoLogin.loop()

