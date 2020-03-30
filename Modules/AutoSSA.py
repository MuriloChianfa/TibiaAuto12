import tkinter as tk
from PIL import Image, ImageTk

from Engine.Defaults import *
from Engine.GUI import *


rgb = Defaults()
bool_auto_ssa = False


class AutoSSA:
    def __init__(self, root):
        self.AutoSSA = GUI('AutoSSA', 'Module: Auto SSA')
        self.AutoSSA.DefaultWindow('DefaultWindow')

        def func_auto_ssa():
            global bool_auto_ssa
            if not bool_auto_ssa:
                bool_auto_ssa = True
                ButtonEnabled.configure(text='AutoSSA: ON')
                scanning_auto_ssa()
            else:
                bool_auto_ssa = False
                ButtonEnabled.configure(text='AutoSSA: OFF')

        def scanning_auto_ssa():
            if bool_auto_ssa:
                print("Try Lock SSA")
                print("Try This")

            root.after(300, scanning_auto_ssa)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.AutoSSA.addButton('Ok', self.AutoSSA.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global bool_auto_ssa
        if not bool_auto_ssa:
            ButtonEnabled = self.AutoSSA.addButton('AutoSSA: OFF', func_auto_ssa, [328, 29, 12, 469],
                                                   [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.AutoSSA.addButton('AutoSSA: ON', func_auto_ssa, [328, 29, 12, 469],
                                                   [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.AutoSSA.addCheck("Print on Tibia's screen", CheckPrint, [10, 408], [120, 98, 51], 0)

        ButtonLowMana = self.AutoSSA.addCheck("Low Mana Warnings", LowMana, [10, 440], [120, 98, 51], 0)

        self.AutoSSA.loop()

