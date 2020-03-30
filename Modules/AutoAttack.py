import pyautogui
import tkinter as tk
from PIL import Image, ImageTk


from Engine.Defaults import *

rgb = Defaults()
bool_auto_attack = False
monster = 'Rat'
target_number = 0
target_number2 = 0

monsters = [
    "Rat",
    "CaveRat",
    "Orc",
    "OrcWarrior",
    "OrcSpearman",
    "Cyclops",
    "Rotworm",
    "AnyCorym",
    "CorymCharlatan",
    "CorymSkirmisher",
    "CorymVanguard",
    "Stonerefiner"
]

priority = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class AutoAttack:
    def __init__(self, root, Target, SQMs):
        self.AutoAttack = tk.Toplevel(root)
        self.AutoAttack.focus_force()
        self.AutoAttack.grab_set()
        w = 348
        h = 546
        sw = self.AutoAttack.winfo_screenwidth()
        sh = self.AutoAttack.winfo_screenheight()
        x = (sw - w) / 1.325
        y = (sh - h) / 2.36
        self.AutoAttack.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.AutoAttack.resizable(width=False, height=False)
        self.AutoAttack.title('Module: Auto Attack')
        self.AutoAttack.configure(background='#000', takefocus=True)
        image = Image.open('images/FundoHealingEdited.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.AutoAttack, image=photo, bg='#000')
        label.image = photo
        label.pack()

        def exit_button():
            self.AutoAttack.destroy()

        def func_auto_attack():
            global bool_auto_attack
            if not bool_auto_attack:
                bool_auto_attack = True
                auto_attack_button.configure(text='AutoAttack: ON')
                print("AutoAttack: ON")
                Defaults.combine_funcs(scanning_auto_attack(), scanning_follow_modee())
            else:
                bool_auto_attack = False
                print("AutoAttack: OFF")
                auto_attack_button.configure(text='AutoAttack: OFF')

        def scanning_auto_attack():
            if bool_auto_attack:
                global target_number, target_number2, battle_location
                monster = var_dropdown_stage_one.get()
                Target[0], Target[1] = get_target_position.scanning_target(battle_location[0], battle_location[1],
                                                                           battle_location[2], battle_location[3],
                                                                           monster)
                target_number2 = get_target_position.number_of_targets(battle_location[0], battle_location[1],
                                                                       battle_location[2], battle_location[3], monster)
                print("Number of " + monster + ": ", target_number2)
                if target_number2 < target_number:
                        take_loot.take_loot(SQMs)
                        target_number = 0

                if Target[0] != 0 and Target[1] != 0:
                    target_number = get_target_position.number_of_targets(battle_location[0], battle_location[1],
                                                                          battle_location[2], battle_location[3],
                                                                          monster)

                    attacking = get_target_position.attaking(battle_location[0], battle_location[1], battle_location[2],
                                                             battle_location[3])

                    if not attacking:
                        print("Attacking a Target")
                        past_mouse_position = pyautogui.position()
                        pyautogui.leftClick(Target[0], Target[1])
                        pyautogui.moveTo(past_mouse_position)
                        target_number2 = get_target_position.number_of_targets(battle_location[0], battle_location[1],
                                                                               battle_location[2], battle_location[3],
                                                                               monster)
                    else:
                        print("You are attacking")
                        target_number2 = get_target_position.number_of_targets(battle_location[0], battle_location[1],
                                                                               battle_location[2], battle_location[3],
                                                                               monster)

            if bool_auto_attack:
                root.after(250, scanning_auto_attack)

        def scanning_follow_modee():
            if bool_auto_attack:
                battle_log = 0
                follow_x_pos, follow_y_pos = GetFollow().scanning_follow_mode()

                if follow_x_pos != 0 and follow_y_pos != 0:
                    past_mouse_position = pyautogui.position()
                    pyautogui.leftClick(follow_x_pos, follow_y_pos)
                    pyautogui.moveTo(past_mouse_position)

            if bool_auto_attack:
                root.after(300, scanning_follow_modee)

        # Buttons

        var_check_one = tk.StringVar()
        var_check_two = tk.StringVar()
        var_check_three = tk.StringVar()
        global monster
        var_dropdown_stage_one = tk.StringVar()
        var_dropdown_stage_one.set(monster)
        var_dropdown_stage_two = tk.StringVar()
        var_dropdown_stage_two.set(1)

        ''' ok button '''

        button_exit = tk.Button(self.AutoAttack, text='Ok', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=rgb.rgb((123, 13, 5)))
        button_exit.place(w=84, h=29, x=130, y=504)

        ''' button auto login '''

        global bool_auto_attack
        if not bool_auto_attack:
            auto_attack_button = tk.Button(self.AutoAttack, text='AutoAttack: OFF',
                                           font=('Microsoft Sans Serif', 10),
                                           bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_attack,
                                           activebackground=rgb.rgb((123, 13, 5)))
            auto_attack_button.place(w=328, h=29, x=12, y=469)
        else:
            auto_attack_button = tk.Button(self.AutoAttack, text='AutoAttack: ON', font=('Microsoft Sans Serif', 10),
                                           bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_attack,
                                           activebackground=rgb.rgb((123, 13, 5)))
            auto_attack_button.place(w=328, h=29, x=12, y=469)

        check_one = tk.Checkbutton(self.AutoAttack, bg=rgb.rgb((120, 98, 51)), height=2,
                                   text="Print on Tibia's screen",
                                   variable=var_check_one, onvalue="on", offvalue="off")
        check_one.place(x=10, y=408)
        check_one.deselect()

        check_two = tk.Checkbutton(self.AutoAttack, bg=rgb.rgb((120, 98, 51)), text="Low Mana Warnings",
                                   variable=var_check_two, onvalue="on", offvalue="off")
        check_two.place(x=10, y=440)
        check_two.deselect()

        check_three = tk.Checkbutton(self.AutoAttack, bg=rgb.rgb((130, 16, 6)), text="Attack Monster",
                                     variable=var_check_three, onvalue="on", offvalue="off",
                                     activebackground=rgb.rgb((130, 16, 6)))
        check_three.place(x=32, y=74)
        check_three.select()

        dropdown_stage_one = tk.OptionMenu(self.AutoAttack, var_dropdown_stage_one, *monsters)
        dropdown_stage_one["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_one["fg"] = 'white'
        dropdown_stage_one["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_one["width"] = 4
        dropdown_stage_one.place(x=155, y=70)

        dropdown_stage_two = tk.OptionMenu(self.AutoAttack, var_dropdown_stage_two, *priority)
        dropdown_stage_two["bg"] = rgb.rgb((127, 17, 8))
        dropdown_stage_two["fg"] = 'white'
        dropdown_stage_two["activebackground"] = rgb.rgb((103, 13, 5))
        dropdown_stage_two["width"] = 4
        dropdown_stage_two.place(x=240, y=70)

        self.AutoAttack.mainloop()

