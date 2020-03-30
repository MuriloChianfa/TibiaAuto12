import tkinter as tk
from PIL import Image, ImageTk

from Engine.Defaults import *


rgb = Defaults()
bool_auto_ring = False


class AutoRing:
    def __init__(self, root):
        self.AutoRing = tk.Toplevel(root)
        self.AutoRing.focus_force()
        self.AutoRing.grab_set()
        w = 348
        h = 546
        sw = self.AutoRing.winfo_screenwidth()
        sh = self.AutoRing.winfo_screenheight()
        x = (sw - w) / 1.325
        y = (sh - h) / 2.36
        self.AutoRing.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.AutoRing.resizable(width=False, height=False)
        self.AutoRing.title('Module: Auto Ring')
        self.AutoRing.configure(background='#000', takefocus=True)
        image = Image.open('images/FundoHealingEdited.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.AutoRing, image=photo, bg='#000')
        label.image = photo
        label.pack()

        def exit_button():
            self.AutoRing.destroy()

        def func_auto_ring():
            global bool_auto_ring
            if not bool_auto_ring:
                bool_auto_ring = True
                auto_ring_button.configure(text='Auto Ring: ON')
                scanning_auto_ring()
            else:
                bool_auto_ring = False
                auto_ring_button.configure(text='Auto Ring: OFF')

        def scanning_auto_ring():
            if bool_auto_ring:
                print("Try Lock Ring")

            root.after(150, scanning_auto_ring)

        # Buttons

        var_check_one = tk.StringVar()
        var_check_two = tk.StringVar()

        ''' ok button '''

        button_exit = tk.Button(self.AutoRing, text='Ok', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=rgb.rgb((123, 13, 5)))
        button_exit.place(w=84, h=29, x=130, y=504)

        ''' button auto login '''

        global bool_auto_ring
        if not bool_auto_ring:
            auto_ring_button = tk.Button(self.AutoRing, text='Auto Ring: OFF', font=('Microsoft Sans Serif', 10),
                                         bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_ring,
                                         activebackground=rgb.rgb((123, 13, 5)))
            auto_ring_button.place(w=328, h=29, x=12, y=469)
        else:
            auto_ring_button = tk.Button(self.AutoRing, text='Auto Ring: ON', font=('Microsoft Sans Serif', 10),
                                         bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_ring,
                                         activebackground=rgb.rgb((123, 13, 5)))
            auto_ring_button.place(w=328, h=29, x=12, y=469)

        check_one = tk.Checkbutton(self.AutoRing, bg=rgb.rgb((120, 98, 51)), height=2,
                                   text="Print on Tibia's screen",
                                   variable=var_check_one, onvalue="on", offvalue="off")
        check_one.place(x=10, y=408)
        check_one.deselect()

        check_two = tk.Checkbutton(self.AutoRing, bg=rgb.rgb((120, 98, 51)), text="Low Mana Warnings",
                                   variable=var_check_two, onvalue="on", offvalue="off")
        check_two.place(x=10, y=440)
        check_two.deselect()

        self.AutoRing.mainloop()

