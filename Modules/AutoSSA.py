import tkinter as tk
from PIL import Image, ImageTk

from Engine.Defaults import *


rgb = Defaults()
bool_auto_ssa = False


class AutoSSA:
    def __init__(self, root):
        self.AutoSSA = tk.Toplevel(root)
        self.AutoSSA.focus_force()
        self.AutoSSA.grab_set()
        w = 348
        h = 546
        sw = self.AutoSSA.winfo_screenwidth()
        sh = self.AutoSSA.winfo_screenheight()
        x = (sw - w) / 1.325
        y = (sh - h) / 2.36
        self.AutoSSA.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.AutoSSA.resizable(width=False, height=False)
        self.AutoSSA.title('Module: Auto SSA')
        self.AutoSSA.configure(background='#000', takefocus=True)
        image = Image.open('images/FundoHealingEdited.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.AutoSSA, image=photo, bg='#000')
        label.image = photo
        label.pack()

        def exit_button():
            self.AutoSSA.destroy()

        def func_auto_ssa():
            global bool_auto_ssa
            if not bool_auto_ssa:
                bool_auto_ssa = True
                auto_ssa_button.configure(text='AutoSSA: ON')
                scanning_auto_ssa()
            else:
                bool_auto_ssa = False
                auto_ssa_button.configure(text='AutoSSA: OFF')

        def scanning_auto_ssa():
            if bool_auto_ssa:
                print("Try Lock SSA")

            root.after(300, scanning_auto_ssa)

        # Buttons

        var_check_one = tk.StringVar()
        var_check_two = tk.StringVar()

        ''' ok button '''

        button_exit = tk.Button(self.AutoSSA, text='Ok', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=rgb.rgb((123, 13, 5)))
        button_exit.place(w=84, h=29, x=130, y=504)

        ''' button auto login '''

        global bool_auto_ssa
        if not bool_auto_ssa:
            auto_ssa_button = tk.Button(self.AutoSSA, text='AutoSSA: OFF', font=('Microsoft Sans Serif', 10),
                                        bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_ssa,
                                        activebackground=rgb.rgb((123, 13, 5)))
            auto_ssa_button.place(w=328, h=29, x=12, y=469)
        else:
            auto_ssa_button = tk.Button(self.AutoSSA, text='AutoSSA: ON', font=('Microsoft Sans Serif', 10),
                                        bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_ssa,
                                        activebackground=rgb.rgb((123, 13, 5)))
            auto_ssa_button.place(w=328, h=29, x=12, y=469)

        check_one = tk.Checkbutton(self.AutoSSA, bg=rgb.rgb((120, 98, 51)), height=2,
                                   text="Print on Tibia's screen",
                                   variable=var_check_one, onvalue="on", offvalue="off")
        check_one.place(x=10, y=408)
        check_one.deselect()

        check_two = tk.Checkbutton(self.AutoSSA, bg=rgb.rgb((120, 98, 51)), text="Low Mana Warnings",
                                   variable=var_check_two, onvalue="on", offvalue="off")
        check_two.place(x=10, y=440)
        check_two.deselect()

        self.AutoSSA.mainloop()

