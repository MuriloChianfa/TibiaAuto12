import pyautogui
from PIL import Image, ImageTk
import tkinter as tk

from Engine.Defaults import *
from Engine.ScanStages import ScanStages
from Core.GetHealthPosition import GetHealthPosition


rgb = Defaults()
bool_life = False

HealthLocation = [0, 0]

lifeColorFull = [194, 74, 74]

lifeColor = [219, 79, 79]

hotkeys = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]

percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]


class AutoHeal:
    def __init__(self, root, HealthLocation):
        self.AutoHeal = tk.Toplevel(root)
        self.AutoHeal.focus_force()
        self.AutoHeal.grab_set()
        w = 348
        h = 546
        sw = self.AutoHeal.winfo_screenwidth()
        sh = self.AutoHeal.winfo_screenheight()
        x = (sw - w) / 1.325
        y = (sh - h) / 2.36
        self.AutoHeal.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.AutoHeal.resizable(width=False, height=False)
        self.AutoHeal.title('Module: Auto Life')
        self.AutoHeal.configure(background='#000', takefocus=True)
        image = Image.open('images/FundoHealingEdited.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.AutoHeal, image=photo, bg='#000')
        label.image = photo
        label.pack()

        def exit_button():
            self.AutoHeal.destroy()

        def func_auto_life():
            global bool_life
            if not bool_life:
                bool_life = True
                auto_life_button.configure(text='AutoHealing: ON')
                print("AutoHealing: ON")
                scanning_auto_life()
            else:
                bool_life = False
                print("AutoHealing: OFF")
                auto_life_button.configure(text='AutoHealing: OFF')

        def scanning_auto_life():
            life = ScanStages('Life').ScanStages(HealthLocation, lifeColor, lifeColorFull)

            if var_check_five.get():
                stage_three = var_dropdown_stage_five.get()
                if int(stage_three) > life or int(stage_three) == life:
                    pyautogui.press(var_dropdown_stage_six.get())
                    print("Pressed ", var_dropdown_stage_six.get())
            elif var_check_four.get() == "on":
                stage_two = var_dropdown_stage_three.get()
                if int(stage_two) > life or int(stage_two) == life:
                    pyautogui.press(var_dropdown_stage_four.get())
                    print("Pressed ", var_dropdown_stage_four.get())
            elif var_check_three.get() == "on":
                stage_one = var_dropdown_stage_one.get()
                if int(stage_one) > life or int(stage_one) == life:
                    pyautogui.press(var_dropdown_stage_two.get())
                    print("Pressed ", var_dropdown_stage_two.get())
            else:
                print("Modulo Not Configured")

            if bool_life:
                root.after(200, scanning_auto_life)

        var_check_one = tk.StringVar()
        var_check_two = tk.StringVar()
        var_check_three = tk.StringVar()
        var_check_four = tk.StringVar()
        var_check_five = tk.BooleanVar()
        var_check_six = tk.StringVar()
        var_check_seven = tk.StringVar()
        var_check_eight = tk.StringVar()
        var_check_nine = tk.StringVar()
        var_check_ten = tk.StringVar()
        var_check_eleven = tk.StringVar()
        var_check_twelve = tk.StringVar()
        var_dropdown_stage_one = tk.StringVar()
        var_dropdown_stage_one.set(90)
        var_dropdown_stage_two = tk.StringVar()
        var_dropdown_stage_two.set("f1")
        var_dropdown_stage_three = tk.StringVar()
        var_dropdown_stage_three.set(75)
        var_dropdown_stage_four = tk.StringVar()
        var_dropdown_stage_four.set("f2")
        var_dropdown_stage_five = tk.StringVar()
        var_dropdown_stage_five.set(35)
        var_dropdown_stage_six = tk.StringVar()
        var_dropdown_stage_six.set("f12")
        img_poison = ImageTk.PhotoImage(Image.open('images/Stats/poison.webp'))
        img_paralyze = ImageTk.PhotoImage(Image.open('images/Stats/paralyze.webp'))
        img_fire = ImageTk.PhotoImage(Image.open('images/Stats/fire.webp'))
        img_electrify = ImageTk.PhotoImage(Image.open('images/Stats/electrify.webp'))
        img_mort = ImageTk.PhotoImage(Image.open('images/Stats/mort.webp'))
        img_blood = ImageTk.PhotoImage(Image.open('images/Stats/blood.webp'))

        button_exit = tk.Button(self.AutoHeal, text='Ok', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=rgb.rgb((123, 13, 5)))
        button_exit.place(w=84, h=29, x=130, y=504)

        ''' button enable healing '''

        global bool_life
        if not bool_life:
            auto_life_button = tk.Button(self.AutoHeal, text='AutoHealing: OFF', font=('Microsoft Sans Serif', 10),
                                         bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_life,
                                         activebackground=rgb.rgb((123, 13, 5)))
            auto_life_button.place(w=328, h=29, x=12, y=469)
        else:
            auto_life_button = tk.Button(self.AutoHeal, text='AutoHealing: ON', font=('Microsoft Sans Serif', 10),
                                         bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_life,
                                         activebackground=rgb.rgb((123, 13, 5)))
            auto_life_button.place(w=328, h=29, x=12, y=469)

        name_label = tk.Label(self.AutoHeal, text='Healing', font=('Microsoft Sans Serif', 10),
                              bg=rgb.rgb((120, 98, 51)), fg='white')
        name_label.place(x=32, y=3)

        percentage_label = tk.Label(self.AutoHeal, text='% Percentage', font=('Microsoft Sans Serif', 10),
                                    bg=rgb.rgb((130, 16, 6)), fg='white')
        percentage_label.place(x=153, y=54)

        hotkey_label = tk.Label(self.AutoHeal, text='HotKey', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((130, 16, 6)), fg='white')
        hotkey_label.place(x=259, y=54)

        check_one = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((120, 98, 51)), height=2,
                                   text="Print on Tibia's screen",
                                   variable=var_check_one, onvalue="on",
                                   activebackground=rgb.rgb((120, 98, 51)))
        check_one.place(x=10, y=408)
        check_one.deselect()

        check_two = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((120, 98, 51)), text="Don't Buff",
                                   variable=var_check_two, onvalue="on", offvalue="off",
                                   activebackground=rgb.rgb((120, 98, 51)))
        check_two.place(x=10, y=440)
        check_two.deselect()

        check_three = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((130, 16, 6)), text="Enable Stage One",
                                     variable=var_check_three, onvalue="on", offvalue="off",
                                     activebackground=rgb.rgb((130, 16, 6)))
        check_three.place(x=32, y=94)
        check_three.deselect()

        check_four = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((130, 16, 6)), text="Enable Stage Two",
                                    variable=var_check_four, onvalue="on", offvalue="off",
                                    activebackground=rgb.rgb((130, 16, 6)))
        check_four.place(x=32, y=144)
        check_four.deselect()

        check_five = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((130, 16, 6)), text="Enable Stage Three",
                                    variable=var_check_five, onvalue=True, offvalue=False,
                                    activebackground=rgb.rgb((130, 16, 6)))
        check_five.place(x=32, y=194)
        check_four.deselect()

        check_six = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((130, 16, 6)), text="Enable Cure Statments",
                                   variable=var_check_six, onvalue="on", offvalue="off",
                                   activebackground=rgb.rgb((130, 16, 6)))
        check_six.place(x=105, y=334)
        check_six.deselect()

        check_seven = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((130, 16, 6)),
                                     variable=var_check_seven, onvalue="on", offvalue="off",
                                     activebackground=rgb.rgb((130, 16, 6)),
                                     image=img_paralyze)
        check_seven.place(x=52, y=364)
        check_seven.deselect()

        check_eight = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((130, 16, 6)),
                                     variable=var_check_eight, onvalue="on", offvalue="off",
                                     activebackground=rgb.rgb((130, 16, 6)),
                                     image=img_poison)
        check_eight.place(x=92, y=364)
        check_eight.deselect()

        check_nine = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((130, 16, 6)),
                                    variable=var_check_nine, onvalue="on", offvalue="off",
                                    activebackground=rgb.rgb((130, 16, 6)),
                                    image=img_fire)
        check_nine.place(x=132, y=364)
        check_nine.deselect()

        check_ten = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((130, 16, 6)),
                                   variable=var_check_ten, onvalue="on", offvalue="off",
                                   activebackground=rgb.rgb((130, 16, 6)),
                                   image=img_electrify)
        check_ten.place(x=172, y=364)
        check_ten.deselect()

        check_eleven = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((130, 16, 6)),
                                      variable=var_check_eleven, onvalue="on", offvalue="off",
                                      activebackground=rgb.rgb((130, 16, 6)),
                                      image=img_mort)
        check_eleven.place(x=212, y=364)
        check_eleven.deselect()

        check_twelve = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((130, 16, 6)),
                                      variable=var_check_twelve, onvalue="on", offvalue="off",
                                      activebackground=rgb.rgb((130, 16, 6)),
                                      image=img_blood)
        check_twelve.place(x=252, y=364)
        check_twelve.deselect()

        dropdown_stage_one = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_one, *percentage)
        dropdown_stage_one["fg"] = 'white'
        dropdown_stage_one["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_one["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_one["width"] = 4
        dropdown_stage_one.place(x=165, y=90)

        dropdown_stage_two = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_two, *hotkeys)
        dropdown_stage_two["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_two["fg"] = 'white'
        dropdown_stage_two["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_two["width"] = 4
        dropdown_stage_two.place(x=250, y=90)

        dropdown_stage_three = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_three, *percentage)
        dropdown_stage_three["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_three["fg"] = 'white'
        dropdown_stage_three["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_three["width"] = 4
        dropdown_stage_three.place(x=165, y=140)

        dropdown_stage_four = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_four, *hotkeys)
        dropdown_stage_four["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_four["fg"] = 'white'
        dropdown_stage_four["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_four["width"] = 4
        dropdown_stage_four.place(x=250, y=140)

        dropdown_stage_five = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_five, *percentage)
        dropdown_stage_five["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_five["fg"] = 'white'
        dropdown_stage_five["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_five["width"] = 4
        dropdown_stage_five.place(x=165, y=190)

        dropdown_stage_six = tk.OptionMenu(self.AutoHeal, var_dropdown_stage_six, *hotkeys)
        dropdown_stage_six["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_six["fg"] = 'white'
        dropdown_stage_six["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_six["width"] = 4
        dropdown_stage_six.place(x=250, y=190)

        self.AutoHeal.mainloop()
