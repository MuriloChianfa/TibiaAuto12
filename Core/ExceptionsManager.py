import tkinter as tk
from PIL import Image, ImageTk
from win32api import GetSystemMetrics, GetCursorPos

from Core.Defaults import rgb


class ExceptionsWindow:
    def __init__(self):
        self.windowID = 'TibiaAuto Error'
        self.name = 'TibiaAuto Error'

    def ErrorWindow(self, BackgroundImage):
        self.windowID = tk.Tk()
        self.windowID.focus_force()
        self.windowID.grab_set()
        X, Y = GetSys()
        CalculatedX = CalculatingX(X)
        CalculatedY = CalculatingY(Y)
        self.windowID.geometry('%dx%d+%d+%d' % (370, 233, CalculatedX, CalculatedY))
        self.windowID.title(self.name)
        self.windowID.resizable(width=False, height=False)
        self.windowID.configure(background='#001000', takefocus=True)
        if BackgroundImage is not None:
            # image = Image.open('images/Modules/' + BackgroundImage + '.png')
            image = Image.open(BackgroundImage + '.png')
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self.windowID, image=photo, bg='#001000')
            label.image = photo
            label.pack()
        self.windowID.overrideredirect(True)
        self.windowID.wm_attributes("-topmost", True)
        self.windowID.attributes("-transparentcolor", '#001000')

    def loop(self):
        self.windowID.mainloop()

    def Protocol(self, Function):
        return self.windowID.protocol("WM_DELETE_WINDOW", Function)

    def destroyWindow(self):
        self.windowID.destroy()

    def UpdateWindow(self, X, Y):
        self.windowID.geometry('370x233+%d+%d' % (X - 185, Y - 187))
        self.windowID.update()

    def addLabel(self, textOfLabel, position):
        labelID = tk.Label(self.windowID,
                           text=textOfLabel,
                           bg=rgb((114, 94, 48)),
                           fg='white')
        labelID.place(x=position[0], y=position[1])
        return labelID

    def addImage(self, image, position):
        imageID = tk.Label(self.windowID,
                           image=image,
                           bg=rgb((114, 94, 48)),
                           fg='white')
        imageID.place(x=position[0], y=position[1])
        return imageID

    def PositionOfWindow(self, value):
        if value == 'X':
            return self.windowID.winfo_x()
        elif value == 'Y':
            return self.windowID.winfo_y()


def GetSys():
    return GetSystemMetrics(0), GetSystemMetrics(1)


def CalculatingX(X):
    return (X / 2) - X * 0.18


def CalculatingY(Y):
    return (Y / 2) - Y * 0.15


def MousePosition():
    X, Y = GetCursorPos()
    return X, Y


def OpenImage(image, size):
    ImageID = Image.open(image)
    ImageID = ImageID.resize((size[0], size[1]), Image.ANTIALIAS)
    ImageID = ImageTk.PhotoImage(ImageID)
    return ImageID
