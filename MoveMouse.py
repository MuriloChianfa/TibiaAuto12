import ctypes
import ctypes.wintypes

from HexMapKeys import KeyToHex


class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]


class MoveMouse:
    def __init__(self):
        self.DLL = ctypes.windll.user32

        self.KEYEVENTF_KEYDOWN = 0x0000
        self.KEYEVENTF_KEYUP = 0x0002

        self.MOUSEEVENTF_MOVE = 0x0001
        self.MOUSEEVENTF_LEFTDOWN = 0x0002
        self.MOUSEEVENTF_LEFTUP = 0x0004
        self.MOUSEEVENTF_RIGHTDOWN = 0x0008
        self.MOUSEEVENTF_RIGHTUP = 0x0010
        self.MOUSEEVENTF_LEFTCLICK = self.MOUSEEVENTF_LEFTDOWN + self.MOUSEEVENTF_LEFTUP
        self.MOUSEEVENTF_RIGHTCLICK = self.MOUSEEVENTF_RIGHTDOWN + self.MOUSEEVENTF_RIGHTUP

    def MainWindowSize(self):
        return self.DLL.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)

    def Position(self):
        Cursor = POINT()
        self.DLL.GetCursorPos(ctypes.byref(Cursor))
        return Cursor.x, Cursor.y

    def Press(self, Key):
        self.DLL.keybd_event(KeyToHex.get(Key, ""), 0, self.KEYEVENTF_KEYDOWN, 0)
        self.DLL.keybd_event(KeyToHex.get(Key, ""), 0, self.KEYEVENTF_KEYUP, 0)

    def PressHotkey(self, Option, Key):
        if Option == 'Ctrl':
            self.DLL.keybd_event(0x11, 0, self.KEYEVENTF_KEYDOWN, 0)
            self.DLL.keybd_event(KeyToHex.get(Key, ""), 0, self.KEYEVENTF_KEYDOWN, 0)
            self.DLL.keybd_event(0x11, 0, self.KEYEVENTF_KEYUP, 0)
            self.DLL.keybd_event(KeyToHex.get(Key, ""), 0, self.KEYEVENTF_KEYUP, 0)
        elif Option == 'Shift':
            self.DLL.keybd_event(0x10, 0, self.KEYEVENTF_KEYDOWN, 0)
            self.DLL.keybd_event(KeyToHex.get(Key, ""), 0, self.KEYEVENTF_KEYDOWN, 0)
            self.DLL.keybd_event(0x10, 0, self.KEYEVENTF_KEYUP, 0)
            self.DLL.keybd_event(KeyToHex.get(Key, ""), 0, self.KEYEVENTF_KEYUP, 0)

    def LeftClick(self, Position):
        self.DLL.mouse_event(self.MOUSEEVENTF_LEFTCLICK, ctypes.c_long(Position[0]), ctypes.c_long(Position[1]), 0, 0)

    def RightClick(self, Position):
        self.DLL.mouse_event(self.MOUSEEVENTF_RIGHTCLICK, ctypes.c_long(Position[0]), ctypes.c_long(Position[1]), 0, 0)

    def MoveTo(self, X, Y):
        self.DLL.SetCursorPos(X, Y)

    def DragTo(self, From, To):
        self.DLL.SetCursorPos(From[0], From[1])
        self.DLL.mouse_event(self.MOUSEEVENTF_LEFTDOWN, ctypes.c_long(From[0]), ctypes.c_long(From[1]), 0, 0)
        self.DLL.SetCursorPos(To[0], To[1])
        self.DLL.mouse_event(self.MOUSEEVENTF_LEFTUP, ctypes.c_long(To[0]), ctypes.c_long(To[1]), 0, 0)

    def UseOn(self, From, To):
        self.DLL.SetCursorPos(From[0], From[1])
        self.DLL.mouse_event(self.MOUSEEVENTF_RIGHTDOWN, ctypes.c_long(From[0]), ctypes.c_long(From[1]), 0, 0)
        self.DLL.mouse_event(self.MOUSEEVENTF_RIGHTUP, ctypes.c_long(From[0]), ctypes.c_long(From[1]), 0, 0)
        self.DLL.SetCursorPos(To[0], To[1])
        self.DLL.mouse_event(self.MOUSEEVENTF_LEFTDOWN, ctypes.c_long(To[0]), ctypes.c_long(To[1]), 0, 0)
        self.DLL.mouse_event(self.MOUSEEVENTF_LEFTUP, ctypes.c_long(To[0]), ctypes.c_long(To[1]), 0, 0)
