class Hotkey:
    def __init__(self, MOUSE_OPTION):
        if MOUSE_OPTION == 0:
            from core.SendToClient import SendToClient
            self.SendToClient = SendToClient()
        else:
            from core.MoveMouse import MoveMouse
            self.SendToClient = MoveMouse()

    Hotkeys = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "Ctrl + F1", "Ctrl + F2", "Ctrl + F3", "Ctrl + F4", "Ctrl + F5", "Ctrl + F6",
               "Ctrl + F7", "Ctrl + F8", "Ctrl + F9", "Ctrl + F10", "Ctrl + F11", "Ctrl + F12",
               "Shift + F1", "Shift + F2", "Shift + F3", "Shift + F4", "Shift + F5", "Shift + F6",
               "Shift + F7", "Shift + F8", "Shift + F9", "Shift + F10", "Shift + F11", "Shift + F12"]

    def Press(self, Key):
        if Key == 'Ctrl + F1':
            self.SendToClient.PressHotkey('ctrl', 'F1')
        elif Key == 'Ctrl + F2':
            self.SendToClient.PressHotkey('ctrl', 'F2')
        elif Key == 'Ctrl + F3':
            self.SendToClient.PressHotkey('ctrl', 'F3')
        elif Key == 'Ctrl + F4':
            self.SendToClient.PressHotkey('ctrl', 'F4')
        elif Key == 'Ctrl + F5':
            self.SendToClient.PressHotkey('ctrl', 'F5')
        elif Key == 'Ctrl + F6':
            self.SendToClient.PressHotkey('ctrl', 'F6')
        elif Key == 'Ctrl + F7':
            self.SendToClient.PressHotkey('ctrl', 'F7')
        elif Key == 'Ctrl + F8':
            self.SendToClient.PressHotkey('ctrl', 'F8')
        elif Key == 'Ctrl + F9':
            self.SendToClient.PressHotkey('ctrl', 'F9')
        elif Key == 'Ctrl + F10':
            self.SendToClient.PressHotkey('ctrl', 'F10')
        elif Key == 'Ctrl + F11':
            self.SendToClient.PressHotkey('ctrl', 'F11')
        elif Key == 'Ctrl + F12':
            self.SendToClient.PressHotkey('ctrl', 'F12')
        elif Key == 'Shift + F1':
            self.SendToClient.PressHotkey('shift', 'F1')
        elif Key == 'Shift + F2':
            self.SendToClient.PressHotkey('shift', 'F2')
        elif Key == 'Shift + F3':
            self.SendToClient.PressHotkey('shift', 'F3')
        elif Key == 'Shift + F4':
            self.SendToClient.PressHotkey('shift', 'F4')
        elif Key == 'Shift + F5':
            self.SendToClient.PressHotkey('shift', 'F5')
        elif Key == 'Shift + F6':
            self.SendToClient.PressHotkey('shift', 'F6')
        elif Key == 'Shift + F7':
            self.SendToClient.PressHotkey('shift', 'F7')
        elif Key == 'Shift + F8':
            self.SendToClient.PressHotkey('shift', 'F8')
        elif Key == 'Shift + F9':
            self.SendToClient.PressHotkey('shift', 'F9')
        elif Key == 'Shift + F10':
            self.SendToClient.PressHotkey('shift', 'F10')
        elif Key == 'Shift + F11':
            self.SendToClient.PressHotkey('shift', 'F11')
        elif Key == 'Shift + F12':
            self.SendToClient.PressHotkey('shift', 'F12')
        else:
            self.SendToClient.Press(Key)

    def Position(self):
        return self.SendToClient.Position()

    def LeftClick(self, X, Y):
        Position = X, Y
        self.SendToClient.LeftClick(Position)

    def RightClick(self, X, Y):
        Position = X, Y
        self.SendToClient.RightClick(Position)
    
    def RawRightClick(self, X, Y):
        Position = X, Y
        self.SendToClient.RawRightClick(Position)

    def MoveTo(self, X, Y):
        self.SendToClient.MoveTo(X, Y)

    def MainWindowSize(self):
        return self.SendToClient.MainWindowSize()

    def DragTo(self, From, To):
        self.SendToClient.DragTo(From, To)
