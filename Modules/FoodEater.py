from Engine.GUI import *

EnabledFoodEater = False


class FoodEater:
    def __init__(self, root):
        self.FoodEater = GUI('FoodEater', 'Module: Food Eater')
        self.FoodEater.DefaultWindow('DefaultWindow')

        def SetFoodEater():
            global EnabledFoodEater
            if not EnabledFoodEater:
                EnabledFoodEater = True
                ButtonEnabled.configure(text='FoodEater: ON')
                ScanFoodEater()
            else:
                EnabledFoodEater = False
                ButtonEnabled.configure(text='FoodEater: OFF')

        def ScanFoodEater():
            if EnabledFoodEater:
                print("Try Lock FoodEater")
                print("Try This")

            root.after(300, ScanFoodEater)

        CheckPrint = tk.BooleanVar()
        LowMana = tk.BooleanVar()

        self.FoodEater.addButton('Ok', self.FoodEater.destroyWindow, [84, 29, 130, 504], [127, 17, 8], [123, 13, 5])

        global EnabledFoodEater
        if not EnabledFoodEater:
            ButtonEnabled = self.FoodEater.addButton('FoodEater: OFF', SetFoodEater, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])
        else:
            ButtonEnabled = self.FoodEater.addButton('FoodEater: ON', SetFoodEater, [328, 29, 12, 469],
                                                       [127, 17, 8], [123, 13, 5])

        ButtonPrint = self.FoodEater.addCheck(CheckPrint, [10, 408], [120, 98, 51], 0, "Print on Tibia's screen")

        ButtonLowMana = self.FoodEater.addCheck(LowMana, [10, 440], [120, 98, 51], 0, "Low Mana Warnings")

        self.FoodEater.loop()

