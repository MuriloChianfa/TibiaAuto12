import pyautogui
import time
from PIL import Image, ImageTk
import tkinter as tk

from Engine.Defaults import *

rgb = Defaults()
bool_auto_looter = False


class AutoLooter:
    def __init__(self, root, Player, SQMs):
        self.AutoLooter = tk.Toplevel(root)
        self.AutoLooter.focus_force()
        self.AutoLooter.grab_set()
        w = 348
        h = 546
        sw = self.AutoLooter.winfo_screenwidth()
        sh = self.AutoLooter.winfo_screenheight()
        x = (sw - w) / 1.325
        y = (sh - h) / 2.36
        self.AutoLooter.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.AutoLooter.resizable(width=False, height=False)
        self.AutoLooter.title('Module: Auto Looter')
        self.AutoLooter.configure(background='#000', takefocus=True)
        image = Image.open('images/FundoHealingEdited.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.AutoLooter, image=photo, bg='#000')
        label.image = photo
        label.pack()

        def exit_button():
            self.AutoLooter.destroy()

        def func_auto_looter():
            global bool_auto_looter
            if not bool_auto_looter:
                bool_auto_looter = True
                auto_looter_button.configure(text='Auto Looter: ON')
                print("Auto Looter: ON")
                global get_player_location
                if not get_player_location:
                    get_player_location = True
                    Player[0], Player[1] = get_player_position.get_gw_xy()
                    if Player[0] and Player[1] != 0:
                        if bool_auto_looter:
                            scanning_auto_looter()
                        else:
                            print("Master Key Non Activated!")
                    else:
                        print("ERROR!")
                else:
                    if bool_auto_looter:
                        scanning_auto_looter()
                    else:
                        print("Master Key Non Activated!")
            else:
                bool_auto_looter = False
                print("Auto Looter: OFF")
                auto_looter_button.configure(text='Auto Looter: OFF')

        def scanning_auto_looter():
            print("Scanning for loot")
            if bool_auto_looter:
                take_loot.take_loot(SQMs)
                time.sleep(4)
            else:
                print("Marster Key not enabled")

            if bool_auto_looter:
                root.after(400, scanning_auto_looter)

        # Buttons

        ''' ok button '''

        button_exit = tk.Button(self.AutoLooter, text='Ok', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=rgb.rgb((123, 13, 5)))
        button_exit.place(w=84, h=29, x=130, y=504)

        ''' button auto login '''

        global bool_auto_looter
        if not bool_auto_looter:
            auto_looter_button = tk.Button(self.AutoLooter, text='Auto Looter: OFF',
                                           font=('Microsoft Sans Serif', 10),
                                           bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_looter,
                                           activebackground=rgb.rgb((123, 13, 5)))
            auto_looter_button.place(w=328, h=29, x=12, y=469)
        else:
            auto_looter_button = tk.Button(self.AutoLooter, text='Auto Looter: ON',
                                           font=('Microsoft Sans Serif', 10),
                                           bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_looter,
                                           activebackground=rgb.rgb((123, 13, 5)))
            auto_looter_button.place(w=328, h=29, x=12, y=469)

        self.AutoLooter.mainloop()

