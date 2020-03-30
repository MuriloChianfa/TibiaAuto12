import pyautogui
import tkinter as tk
from PIL import Image, ImageTk

from Engine.Defaults import *


rgb = Defaults()
bool_color_change = False


class ColorChange:
    def __init__(self, root, Player):
        self.ColorChange = tk.Toplevel(root)
        self.ColorChange.focus_force()
        self.ColorChange.grab_set()
        w = 348
        h = 546
        sw = self.ColorChange.winfo_screenwidth()
        sh = self.ColorChange.winfo_screenheight()
        x = (sw - w) / 1.325
        y = (sh - h) / 2.36
        self.ColorChange.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.ColorChange.resizable(width=False, height=False)
        self.ColorChange.title('Module: Color Change')
        self.ColorChange.configure(background='#000', takefocus=True)
        image = Image.open('images/FundoHealingEdited.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.ColorChange, image=photo, bg='#000')
        label.image = photo
        label.pack()

        def exit_button():
            self.ColorChange.destroy()

        def func_color_change():
            global bool_color_change
            if not bool_color_change:
                bool_color_change = True
                print("Color Change: ON")
                color_change_button.configure(text='Color Change: ON')
                scanning_color_change()
            else:
                bool_color_change = False
                print("Color Change: OFF")
                color_change_button.configure(text='Color Change: OFF')

        def scanning_color_change():
            if bool_color_change:
                pyautogui.keyDown('ctrl')
                pyautogui.click(Player[0], Player[1], button='right')
                pyautogui.keyUp('ctrl')

            root.after(300, scanning_color_change)

        def dancing():
            pyautogui.hotkey("ctrl", "up")
            pyautogui.hotkey("ctrl", "left")
            pyautogui.hotkey("ctrl", "right")
            pyautogui.hotkey("ctrl", "down")

        # Buttons

        var_check_one = tk.StringVar()
        var_check_two = tk.StringVar()

        ''' ok button '''

        button_exit = tk.Button(self.ColorChange, text='Ok', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=rgb.rgb((123, 13, 5)))
        button_exit.place(w=84, h=29, x=130, y=504)

        ''' button auto login '''

        global bool_color_change
        if not bool_color_change:
            color_change_button = tk.Button(self.ColorChange, text='Color Change: OFF',
                                            font=('Microsoft Sans Serif', 10),
                                            bg=rgb.rgb((127, 17, 8)), fg='white', command=func_color_change,
                                            activebackground=rgb.rgb((123, 13, 5)))
            color_change_button.place(w=328, h=29, x=12, y=469)
        else:
            color_change_button = tk.Button(self.ColorChange, text='Color Change: ON',
                                            font=('Microsoft Sans Serif', 10),
                                            bg=rgb.rgb((127, 17, 8)), fg='white', command=func_color_change,
                                            activebackground=rgb.rgb((123, 13, 5)))
            color_change_button.place(w=328, h=29, x=12, y=469)

        self.ColorChange.mainloop()