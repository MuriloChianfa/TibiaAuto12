import pyautogui
from PIL import Image, ImageTk
import tkinter as tk
import time

from Engine.Defaults import *


rgb = Defaults()

username_value = ''
passwd_value = ''

bool_login = False


class AutoLogin:
    def __init__(self, root):
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
        self.AutoHeal.title('Module: Auto Login')
        self.AutoHeal.configure(background='#000', takefocus=True)
        image = Image.open('images/FundoHealingEdited.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.AutoHeal, image=photo, bg='#000')
        label.image = photo
        label.pack()

        def exit_button():
            self.AutoHeal.destroy()

        def func_auto_login():
            global bool_login
            if not bool_login:
                bool_login = True
                auto_login_button.configure(text='AutoLogin: ON')
                print("AutoLogin: ON")
                scanning_auto_login()
            else:
                bool_login = False
                print("AutoLogin: OFF")
                auto_login_button.configure(text='AutoLogin: OFF')

        def scanning_auto_login():
            global bool_login
            global username_value
            username_value = username.get()
            global passwd_value
            passwd_value = passwd.get()
            username_field_check = pyautogui.locateOnScreen('images/AccountName.png', grayscale=True, confidence=0.8)
            if username_field_check:
                print("You Are Offline... Trying To Login")
                time.sleep(1)
                if bool_login:
                    global pass_mouse_position
                    if username_field_X != 0 and username_field_Y != 0:
                        pass_mouse_position = pyautogui.position()
                        pyautogui.click(x=username_field_X, y=username_field_Y)
                        pyautogui.write(username_value, interval=0.15)
                        pyautogui.press('tab')
                        pyautogui.write(passwd_value, interval=0.15)
                        pyautogui.click(loginX, loginY)
                        time.sleep(2)
                        pyautogui.press('enter')
                        pyautogui.moveTo(pass_mouse_position)
                        username_field_check2 = pyautogui.locateOnScreen('images/AccountName/AccountName.png',
                                                                         grayscale=True,
                                                                         confidence=0.8)
                        if username_field_check2:
                            print("Error To Login !!!!")
                            username_field_check2 = None
                            username_field_check = None
                        else:
                            print("You Are Logged")
                            username_field_check = None
                            username_field_check2 = None

            if bool_login:
                root.after(3000, scanning_auto_login)

        # Buttons

        var_check_one = tk.StringVar()
        var_check_two = tk.StringVar()
        var_check_three = tk.StringVar()

        ''' ok button '''

        button_exit = tk.Button(self.AutoHeal, text='Ok', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=rgb.rgb((123, 13, 5)))
        button_exit.place(w=84, h=29, x=130, y=504)

        ''' button auto login '''

        global bool_login
        if not bool_login:
            auto_login_button = tk.Button(self.AutoHeal, text='AutoLogin: OFF', font=('Microsoft Sans Serif', 10),
                                          bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_login,
                                          activebackground=rgb.rgb((123, 13, 5)))
            auto_login_button.place(w=328, h=29, x=12, y=469)
        else:
            auto_login_button = tk.Button(self.AutoHeal, text='AutoLogin: ON', font=('Microsoft Sans Serif', 10),
                                          bg=rgb.rgb((127, 17, 8)), fg='white', command=func_auto_login,
                                          activebackground=rgb.rgb((123, 13, 5)))
            auto_login_button.place(w=328, h=29, x=12, y=469)

        check_one = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((120, 98, 51)), height=2,
                                   text="Print on Tibia's screen",
                                   variable=var_check_one, onvalue="on", offvalue="off")
        check_one.place(x=10, y=408)
        check_one.deselect()

        check_two = tk.Checkbutton(self.AutoHeal, bg=rgb.rgb((120, 98, 51)), text="Low Mana Warnings",
                                   variable=var_check_two, onvalue="on", offvalue="off")
        check_two.place(x=10, y=440)
        check_two.deselect()

        username_label = tk.Label(self.AutoHeal, text='Username', font=('Microsoft Sans Serif', 10),
                                  bg=rgb.rgb((130, 16, 6)), fg='white')
        username_label.place(x=69, y=84)

        username = tk.Entry(self.AutoHeal)
        username.place(x=149, y=86)
        global username_value
        username_value = username.get()

        passwd_label = tk.Label(self.AutoHeal, text='Password', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((130, 16, 6)), fg='white')
        passwd_label.place(x=69, y=124)

        passwd = tk.Entry(self.AutoHeal)
        passwd.place(x=149, y=126)
        global passwd_value
        passwd_value = passwd.get()

        self.AutoHeal.mainloop()