import time
import tkinter as tk
import pygetwindow
from PIL import Image, ImageTk

from Engine.Defaults import *
from Conf.WindowTitles import *

rgb = Defaults()
bool_adjust_config = False
TibiaName = ''


class AdjustConfig:
    def __init__(self, root):
        self.AdjustConfig = tk.Toplevel(root)
        self.AdjustConfig.focus_force()
        self.AdjustConfig.grab_set()
        w = 348
        h = 546
        sw = self.AdjustConfig.winfo_screenwidth()
        sh = self.AdjustConfig.winfo_screenheight()
        x = (sw - w) / 1.325
        y = (sh - h) / 2.36
        self.AdjustConfig.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.AdjustConfig.resizable(width=False, height=False)
        self.AdjustConfig.title('Module: Adjust Config')
        self.AdjustConfig.configure(background='#000', takefocus=True)
        image = Image.open('images/FundoHealingEdited.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.AdjustConfig, image=photo, bg='#000')
        label.image = photo
        label.pack()

        def set_title():
            global TibiaName
            try:
                TibiaName = FindTibiaTitle()
            except IndexError as e:
                print("You need to login before starting bot.")
                root.destroy()
            if TibiaName is not None:
                TibiaWindow = pygetwindow.getWindowsWithTitle(TibiaName)[0]
                TibiaAuto = pygetwindow.getWindowsWithTitle("TibiaAuto V12")[0]
                Module = pygetwindow.getWindowsWithTitle("Module: Adjust Config")[0]
                TibiaAuto.minimize()
                Module.minimize()
                TibiaWindow.maximize()
                time.sleep(1)

                # configure()

                time.sleep(3)
                TibiaAuto.maximize()
                Module.maximize()
            else:
                print("Error to Log Tibia window")

        def exit_button():
            self.AdjustConfig.destroy()

        def func_adjust_config():
            global bool_adjust_config
            if not bool_adjust_config:
                bool_adjust_config = True
                adjust_config_button.configure(text='Adjust Config: ON')
                scanning_adjust_config()
            else:
                bool_adjust_config = False
                adjust_config_button.configure(text='Adjust Config: OFF')

        def scanning_adjust_config():
            if bool_adjust_config:
                print("Adjust Config.....")

            root.after(65, scanning_adjust_config)

        # Buttons

        ''' ok button '''

        button_exit = tk.Button(self.AdjustConfig, text='Ok', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=rgb.rgb((123, 13, 5)))
        button_exit.place(w=84, h=29, x=130, y=504)

        ''' button auto login '''

        global bool_adjust_config
        if not bool_adjust_config:
            adjust_config_button = tk.Button(self.AdjustConfig, text='Adjust Config: OFF',
                                             font=('Microsoft Sans Serif', 10),
                                             bg=rgb.rgb((127, 17, 8)), fg='white', command=func_adjust_config,
                                             activebackground=rgb.rgb((123, 13, 5)))
            adjust_config_button.place(w=328, h=29, x=12, y=469)
        else:
            adjust_config_button = tk.Button(self.AdjustConfig, text='Adjust Config: ON',
                                             font=('Microsoft Sans Serif', 10),
                                             bg=rgb.rgb((127, 17, 8)), fg='white', command=func_adjust_config,
                                             activebackground=rgb.rgb((123, 13, 5)))
            adjust_config_button.place(w=328, h=29, x=12, y=469)

        config_button = tk.Button(self.AdjustConfig, width=15, text="Configurar", command=set_title)
        config_button.pack()
        config_button.place(x=155, y=70)

        self.AdjustConfig.mainloop()

