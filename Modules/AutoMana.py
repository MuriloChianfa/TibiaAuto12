import pyautogui
from PIL import Image, ImageTk
import tkinter as tk

from Engine.Defaults import *
from Engine.ScanStages import ScanStages
from Core.GetManaPosition import GetManaPosition


rgb = Defaults()
bool_mana = False

manaColorFull = [45, 45, 105]

manaColor = [83, 80, 218]

hotkeys = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]

percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]


class AutoMana:
    def __init__(self, root, ManaLocation):
        self.AutoMana = tk.Toplevel(root)
        self.AutoMana.focus_force()
        self.AutoMana.grab_set()
        w = 348
        h = 546
        sw = self.AutoMana.winfo_screenwidth()
        sh = self.AutoMana.winfo_screenheight()
        x = (sw - w) / 1.325
        y = (sh - h) / 2.36
        self.AutoMana.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.AutoMana.resizable(width=False, height=False)
        self.AutoMana.title('Module: Auto Mana')
        self.AutoMana.configure(background='#000', takefocus=True)
        image = Image.open('images/FundoHealingEdited.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.AutoMana, image=photo, bg='#000')
        label.image = photo
        label.pack()

        def exit_button():
            self.AutoMana.destroy()

        def func_auto_mana():
            global bool_mana
            if not bool_mana:
                bool_mana = True
                auto_mana_button.configure(text='AutoMana: ON')
                print("AutoMana: ON")
                if ManaLocation[0] and ManaLocation[1] != 0:
                    if bool_mana:
                        scanning_auto_mana()
                else:
                    print("Error on Mana Localization!")
            else:
                bool_mana = False
                print("AutoMana: OFF")
                auto_mana_button.configure(text='AutoMana: OFF')

        def scanning_auto_mana():
            mana = ScanStages('Mana').ScanStages(ManaLocation, manaColor, manaColorFull)

            if var_check_four.get() == "on":
                stage_two = var_dropdown_stage_three.get()
                if int(stage_two) >= mana:
                    mana_button2 = var_dropdown_stage_four.get()
                    pyautogui.press(mana_button2)
                    print("Pressed ", mana_button2)
            elif var_check_three.get() == "on":
                stage_one = var_dropdown_stage_one.get()
                if int(stage_one) >= mana:
                    mana_button1 = var_dropdown_stage_two.get()
                    pyautogui.press(mana_button1)
                    print("Pressed ", mana_button1)
            else:
                print("Modulo Not Configured")

            if bool_mana:
                root.after(300, scanning_auto_mana)

        # Buttons

        var_check_one = tk.StringVar()
        var_check_two = tk.StringVar()
        var_check_three = tk.StringVar()
        var_check_four = tk.StringVar()
        var_dropdown_stage_one = tk.StringVar()
        var_dropdown_stage_one.set(50)
        var_dropdown_stage_two = tk.StringVar()
        var_dropdown_stage_two.set("f3")
        var_dropdown_stage_three = tk.StringVar()
        var_dropdown_stage_three.set(25)
        var_dropdown_stage_four = tk.StringVar()
        var_dropdown_stage_four.set("f4")

        ''' ok button '''

        button_exit = tk.Button(self.AutoMana, text='Ok', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=rgb.rgb((123, 13, 5)))
        button_exit.place(w=84, h=29, x=130, y=504)

        ''' button auto hur '''

        global bool_mana
        if not bool_mana:
            auto_mana_button = tk.Button(self.AutoMana, text='AutoMana: OFF', font=('Microsoft Sans Serif', 10),
                                         bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_mana,
                                         activebackground=rgb.rgb((123, 13, 5)))
            auto_mana_button.place(w=328, h=29, x=12, y=469)
        else:
            auto_mana_button = tk.Button(self.AutoMana, text='AutoMana: ON', font=('Microsoft Sans Serif', 10),
                                         bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_mana,
                                         activebackground=rgb.rgb((123, 13, 5)))
            auto_mana_button.place(w=328, h=29, x=12, y=469)

        check_one = tk.Checkbutton(self.AutoMana, bg=rgb.rgb((120, 98, 51)), height=2,
                                   text="Print on Tibia's screen",
                                   variable=var_check_one, onvalue="on", offvalue="off")
        check_one.place(x=10, y=408)
        check_one.deselect()

        check_two = tk.Checkbutton(self.AutoMana, bg=rgb.rgb((120, 98, 51)), text="Low Mana Warnings",
                                   variable=var_check_two, onvalue="on", offvalue="off")
        check_two.place(x=10, y=440)
        check_two.deselect()

        check_three = tk.Checkbutton(self.AutoMana, bg=rgb.rgb((130, 16, 6)), text="Enable Stage One",
                                     variable=var_check_three, onvalue="on", offvalue="off",
                                     activebackground=rgb.rgb((130, 16, 6)))
        check_three.place(x=32, y=94)
        check_three.deselect()

        check_four = tk.Checkbutton(self.AutoMana, bg=rgb.rgb((130, 16, 6)), text="Enable Stage Two",
                                    variable=var_check_four, onvalue="on", offvalue="off",
                                    activebackground=rgb.rgb((130, 16, 6)))
        check_four.place(x=32, y=144)
        check_four.deselect()

        dropdown_stage_one = tk.OptionMenu(self.AutoMana, var_dropdown_stage_one, *percentage)
        dropdown_stage_one["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_one["fg"] = 'white'
        dropdown_stage_one["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_one["width"] = 4
        dropdown_stage_one.place(x=165, y=90)

        dropdown_stage_two = tk.OptionMenu(self.AutoMana, var_dropdown_stage_two, *hotkeys)
        dropdown_stage_two["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_two["fg"] = 'white'
        dropdown_stage_two["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_two["width"] = 4
        dropdown_stage_two.place(x=250, y=90)

        dropdown_stage_three = tk.OptionMenu(self.AutoMana, var_dropdown_stage_three, *percentage)
        dropdown_stage_three["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_three["fg"] = 'white'
        dropdown_stage_three["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_three["width"] = 4
        dropdown_stage_three.place(x=165, y=140)

        dropdown_stage_four = tk.OptionMenu(self.AutoMana, var_dropdown_stage_four, *hotkeys)
        dropdown_stage_four["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_four["fg"] = 'white'
        dropdown_stage_four["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_four["width"] = 4
        dropdown_stage_four.place(x=250, y=140)

        self.AutoMana.mainloop()

