import win32gui
import win32api
import win32con
import json

from HexMapKeys import KeyToHex

with open('Loads.json', 'r') as LoadsJson:
    data = json.load(LoadsJson)


class SendToClient:
    def __init__(self):
        self.hwnd = data['hwnd']

    def SetForeground(self):
        win32gui.SetForegroundWindow(self.hwnd)

    def GetWindowSizes(self):
        win32gui.GetWindowRect(self.hwnd)

    def IsFocused(self):
        if win32gui.IsIconic(self.hwnd):
            win32gui.ShowWindow(self.hwnd, win32con.SW_RESTORE)
            return False
        elif self.hwnd != win32gui.GetForegroundWindow():
            return False
        else:
            return True

    def Press(self, Key):
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, KeyToHex.get(Key, ""), 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, KeyToHex.get(Key, ""), 0)

    def PressHotkey(self, Option,  Key):
        win32api.keybd_event(KeyToHex.get(Option, ""), 0, 0, 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, KeyToHex.get(Key, ""), 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, KeyToHex.get(Key, ""), 0)
        win32api.keybd_event(KeyToHex.get(Option, ""), 0, win32con.KEYEVENTF_KEYUP, 0)

    def LeftClick(self, Position):
        ClientPosition = win32gui.ScreenToClient(self.hwnd, Position)
        PositionToClick = win32api.MAKELONG(ClientPosition[0], ClientPosition[1])
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, 0, PositionToClick)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, PositionToClick)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, PositionToClick)

    def RightClick(self, Position):
        ClientPosition = win32gui.ScreenToClient(self.hwnd, Position)
        PositionToClick = win32api.MAKELONG(ClientPosition[0], ClientPosition[1] + 23)
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, 0, PositionToClick)
        win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, PositionToClick)
        win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, PositionToClick)

    def DragTo(self, From, To):
        ClientFrom = win32gui.ScreenToClient(self.hwnd, From)
        FromPosition = win32api.MAKELONG(ClientFrom[0], ClientFrom[1])
        ClientTo = win32gui.ScreenToClient(self.hwnd, To)
        ToPosition = win32api.MAKELONG(ClientTo[0], ClientTo[1])
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, FromPosition)
        win32api.SendMessage(self.hwnd, win32con.WM_MOUSEMOVE, 0, ToPosition)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, ToPosition)

    def UseOn(self, From, To):
        ClientFrom = win32gui.ScreenToClient(self.hwnd, From)
        FromPosition = win32api.MAKELONG(ClientFrom[0], ClientFrom[1])
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, 0, FromPosition)
        win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, FromPosition)
        win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, FromPosition)
        ClientTo = win32gui.ScreenToClient(self.hwnd, To)
        ToPosition = win32api.MAKELONG(ClientTo[0], ClientTo[1])
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, 0, ToPosition)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, ToPosition)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, ToPosition)
