import tkinter as tk
from PIL import Image, ImageTk

from Engine.Defaults import *


rgb = Defaults()
bool_hur = False


class AutoHur:
    def __init__(self, root):
        screen_auto_hur = tk.Toplevel(root)
        screen_auto_hur.focus_force()
        screen_auto_hur.grab_set()
        w = 348
        h = 546
        sw = screen_auto_hur.winfo_screenwidth()
        sh = screen_auto_hur.winfo_screenheight()
        x = (sw - w) / 1.325
        y = (sh - h) / 2.36
        screen_auto_hur.geometry('%dx%d+%d+%d' % (w, h, x, y))
        screen_auto_hur.resizable(width=False, height=False)
        screen_auto_hur.title('Module: Auto Hur')
        screen_auto_hur.configure(background='#000', takefocus=True)
        image = Image.open('images/FundoHealingEdited.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(screen_auto_hur, image=photo, bg='#000')
        label.image = photo
        label.pack()

        def exit_button():
            screen_auto_hur.destroy()

        def func_auto_hur():
            global bool_hur
            if not bool_hur:
                bool_hur = True
                auto_hur_button.configure(text='AutoHur: ON')
                scanning_auto_hur()
            else:
                bool_hur = False
                auto_hur_button.configure(text='AutoHur: OFF')

        def scanning_auto_hur():
            if bool_hur:
                print("Pressed Key f6")

            root.after(1500, scanning_auto_hur)

        # Buttons

        var_check_one = tk.StringVar()
        var_check_two = tk.StringVar()

        ''' ok button '''

        button_exit = tk.Button(screen_auto_hur, text='Ok', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=rgb.rgb((123, 13, 5)))
        button_exit.place(w=84, h=29, x=130, y=504)

        ''' button auto hur '''

        global bool_hur
        if not bool_hur:
            auto_hur_button = tk.Button(screen_auto_hur, text='AutoHur: OFF', font=('Microsoft Sans Serif', 10),
                                        bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_hur,
                                        activebackground=rgb.rgb((123, 13, 5)))
            auto_hur_button.place(w=328, h=29, x=12, y=469)
        else:
            auto_hur_button = tk.Button(screen_auto_hur, text='AutoHur: ON', font=('Microsoft Sans Serif', 10),
                                        bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_hur,
                                        activebackground=rgb.rgb((123, 13, 5)))
            auto_hur_button.place(w=328, h=29, x=12, y=469)

        check_one = tk.Checkbutton(screen_auto_hur, bg=rgb.rgb((120, 98, 51)), height=2,
                                   text="Print on Tibia's screen",
                                   variable=var_check_one, onvalue="on", offvalue="off")
        check_one.place(x=10, y=408)
        check_one.deselect()

        check_two = tk.Checkbutton(screen_auto_hur, bg=rgb.rgb((120, 98, 51)), text="Low Mana Warnings",
                                   variable=var_check_two, onvalue="on", offvalue="off")
        check_two.place(x=10, y=440)
        check_two.deselect()

        screen_auto_hur.mainloop()

