import pyautogui
import tkinter as tk
from tkinter import SUNKEN, RAISED, ttk
from PIL import Image, ImageTk

from core.Defaults import *


class GUI:
    def __init__(self, windowID, name):
        self.windowID = windowID
        self.name = name

    def MainWindow(self, BackgroundImage, sizes, positions):
        self.windowID = tk.Tk()
        w = sizes[0]
        h = sizes[1]
        sw = self.windowID.winfo_screenwidth()
        sh = self.windowID.winfo_screenheight()
        x = (sw - w) / positions[0]
        y = (sh - h) / positions[1]
        self.windowID.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.windowID.title(self.name)
        self.windowID.resizable(width=False, height=False)
        self.windowID.configure(background='#000', takefocus=True)
        self.windowID.iconbitmap('images/icon.ico')
        image = Image.open('images/Modules/' + BackgroundImage + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.windowID, image=photo, bg='#000')
        label.image = photo
        label.pack()

    def DefaultWindow(self, BackgroundImage, sizes, positions):
        self.windowID = tk.Toplevel()
        self.windowID.focus_force()
        self.windowID.grab_set()
        w = sizes[0]
        h = sizes[1]
        sw = self.windowID.winfo_screenwidth()
        sh = self.windowID.winfo_screenheight()
        x = (sw - w) / positions[0]
        y = (sh - h) / positions[1]
        self.windowID.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.windowID.title(self.name)
        self.windowID.resizable(width=False, height=False)
        self.windowID.configure(background='#000', takefocus=True)
        self.windowID.iconbitmap('images/icon.ico')
        image = Image.open('images/Modules/' + BackgroundImage + '.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.windowID, image=photo, bg='#000')
        label.image = photo
        label.pack()

    def InvisibleWindow(self, BackgroundImage):
        self.windowID = tk.Toplevel()
        self.windowID.focus_force()
        self.windowID.grab_set()
        self.windowID.resizable(width=False, height=False)
        self.windowID.geometry('130x130')
        self.windowID.image = tk.PhotoImage(file='images/BackgroundImages/' + BackgroundImage + '.png')
        label = tk.Label(self.windowID, image=self.windowID.image, bg='black')
        label.place(x=0, y=0)
        self.windowID.overrideredirect(True)
        self.windowID.wm_attributes("-topmost", True)
        self.windowID.attributes("-transparentcolor", "black")

    def loop(self):
        try:
            self.windowID.mainloop()
        except KeyboardInterrupt:
            print('Received SIGINT')
        except SystemExit:
            print('Received SIGTERM')
        finally:
            self.windowID.destroy()
            raise SystemExit

    def Protocol(self, Function):
        return self.windowID.protocol("WM_DELETE_WINDOW", Function)

    def UpdateWindow(self, X, Y):
        self.windowID.geometry('130x130+%d+%d' % (X - 65, Y - 65))
        self.windowID.update()

    def destroyWindow(self):
        self.windowID.destroy()

    def PositionOfWindow(self, value):
        if value == 'X':
            return self.windowID.winfo_x()
        elif value == 'Y':
            return self.windowID.winfo_y()

    def addButton(self, textOfButton, command, sizes, positions):
        buttonID = tk.Button(self.windowID,
                             text=textOfButton,
                             font=('Microsoft Sans Serif', 10),
                             bg=rgb((114, 0, 0)),
                             fg='white',
                             command=command,
                             cursor="hand2",
                             activebackground=rgb((103, 13, 5)))
        buttonID.place(w=sizes[0], h=sizes[1], x=positions[0], y=positions[1])
        return buttonID

    def addCheck(self, variable, position, selected, textOfButton="", image=None):
        buttonID = tk.Checkbutton(self.windowID,
                                  bg=rgb((114, 0, 3)),
                                  activebackground=rgb((114, 0, 3)),
                                  activeforeground='white',
                                  text=textOfButton,
                                  variable=variable,
                                  fg='white',
                                  selectcolor=rgb((114, 0, 3)),
                                  cursor="hand2",
                                  onvalue=True,
                                  offvalue=False,
                                  image=image)
        buttonID.place(x=position[0], y=position[1])
        if selected:
            buttonID.select()
        else:
            buttonID.deselect()
        return buttonID

    def addLabel(self, textOfLabel, position):
        labelID = tk.Label(self.windowID,
                           text=textOfLabel,
                           bg=rgb((114, 0, 0)),
                           fg='white')
        labelID.place(x=position[0], y=position[1])
        return labelID

    def addList(self, columns, height, sizes, position):
        style = ttk.Style()
        style.theme_use('winnative')
        style.configure('Treeview.Heading', background="gray")

        frame = tk.Frame(self.windowID, height=sizes[1], width=sizes[0])
        frame.place(x=position[0], y=position[1])

        table = ttk.Treeview(self.windowID, columns=columns, height=height, show='headings')
        table.place(x=position[0], y=position[1])

        return table

    def addScrollbar(self):
        from tkinter import VERTICAL, RIGHT, Y

        sb = tk.Scrollbar(self.windowID, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)

        return sb

    def addMinimalLabel(self, textOfLabel, position, h=16):
        labelID = tk.Label(self.windowID,
                           text=textOfLabel,
                           bg=rgb((114, 0, 0)),
                           fg='white')
        labelID.place(x=position[0], y=position[1], h=h)
        return labelID

    def addImage(self, image, position):
        imageID = tk.Label(self.windowID,
                           image=image,
                           bg=rgb((114, 0, 0)),
                           fg='white')
        imageID.place(x=position[0], y=position[1])
        return imageID

    def addEntry(self, position, var, width=12):
        entryID = tk.Entry(self.windowID,
                           width=width,
                           textvariable=var,
                           bg=rgb((114, 0, 0)),
                           borderwidth=2,
                           foreground=rgb((81, 216, 0))
                           )
        entryID.place(x=position[0], y=position[1])
        return entryID

    def addOption(self, variable, options, position, width=4):
        optionID = tk.OptionMenu(self.windowID, variable, *options)
        optionID['bg'] = rgb((114, 0, 0))
        optionID['fg'] = 'white'
        optionID['activebackground'] = rgb((103, 13, 5))
        optionID["highlightthickness"] = 0
        optionID['width'] = width
        optionID['cursor'] = "hand2"
        optionID.place(x=position[0], y=position[1])
        return optionID

    def addRadio(self, text, variable, value, position, command=None):
        RadioID = tk.Radiobutton(self.windowID,
                                 text=text,
                                 variable=variable,
                                 value=value,
                                 fg='white',
                                 selectcolor=rgb((114, 0, 3)),
                                 cursor="hand2",
                                 bg=rgb((114, 0, 3)),
                                 command=command)
        RadioID['activebackground'] = rgb((114, 0, 3)),
        RadioID['activeforeground'] = 'white',
        RadioID.place(x=position[0], y=position[1])
        return RadioID

    def addRadioImage(self, text, variable, value, position, command=None, image=None):
        RadioID = tk.Radiobutton(self.windowID,
                                 text=text,
                                 variable=variable,
                                 value=value,
                                 fg='white',
                                 selectcolor=rgb((114, 0, 3)),
                                 cursor="hand2",
                                 bg=rgb((114, 0, 3)),
                                 command=command,
                                 image=image)
        RadioID['activebackground'] = rgb((114, 0, 3)),
        RadioID['activeforeground'] = 'white',
        RadioID.place(x=position[0], y=position[1])
        return RadioID

    def After(self, Time, Function):
        return self.windowID.after(Time, Function)

    def deiconify(self):
        return self.windowID.deiconify()

    @staticmethod
    def openImage(image, size):
        ImageID = Image.open(image)
        ImageID = ImageID.resize((size[0], size[1]), Image.ANTIALIAS)
        ImageID = ImageTk.PhotoImage(ImageID)
        return ImageID
