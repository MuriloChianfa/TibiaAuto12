"""

The SendToClient.py, Dont Work On Tibia Global
Because The Client Block The Requests =(

If You Choose The Option 'SendsToClient'
He Load The HWND from Loads.json

You Can Use This Class For Send Commands To Another Window Too,
You Just Need Change The HWND Number

"""

import win32gui
import win32api
import win32con

from conf.HexMapKeys import KeyToHex
from conf.conf_manager import ConfManager

data = ConfManager.get('conf.json')


class SendToClient:
    def __init__(self):
        self.hwnd = data['hwnd']

    '''
        This Function, Set Window To Focused
    '''

    def SetForeground(self):
        win32gui.SetForegroundWindow(self.hwnd)

    '''
        Here, He Get The Window Metrics
    '''

    def GetWindowSizes(self):
        win32gui.GetWindowRect(self.hwnd)

    '''
        Verify If The Window Is Focused In At Moment
        
        Examples:
        if SendToClient.IsFocused()
            print('Is Focused Now')
        else:
            print('The Window Is Not Focused')
    '''

    def IsFocused(self):
        if win32gui.IsIconic(self.hwnd):
            win32gui.ShowWindow(self.hwnd, win32con.SW_RESTORE)
            return False
        elif self.hwnd != win32gui.GetForegroundWindow():
            return False
        return True

    '''
        Send One Press Button For Client
        
        Examples:
        SendToClient.Press('F2')
        
        SendToClient.Press('m')
    '''

    def Press(self, Key):
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, KeyToHex.get(Key, ""), 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, KeyToHex.get(Key, ""), 0)

    '''
        Send One Press HotKey For Client

        Examples:
        SendToClient.Press('Ctrl', 'F1')

        SendToClient.Press('Shift', 'F7')
    '''

    def PressHotkey(self, Option,  Key):
        win32api.keybd_event(KeyToHex.get(Option, ""), 0, 0, 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, KeyToHex.get(Key, ""), 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, KeyToHex.get(Key, ""), 0)
        win32api.keybd_event(KeyToHex.get(Option, ""), 0, win32con.KEYEVENTF_KEYUP, 0)

    '''
        Here He Send One Mouse Click At One Position Received From Arg
        
        Examples:
        SendToClient.LeftClick((826, 435)) # Click With Left Button At This Position
        
        SendToClient.RightClick((826, 435)) #Click With Right Button At This Position
    '''

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

    '''
        Usage Just For Tibia...
        He Move The Object From Postion To Another Position
        
        Examples:
        SendToClient.DragTo((826, 435), (254, 324))
    '''

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

    @staticmethod
    def MainWindowSize():
        from win32api import GetSystemMetrics
        return GetSystemMetrics(0), GetSystemMetrics(1)
