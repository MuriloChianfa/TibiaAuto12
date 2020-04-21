import pyautogui


Hotkeys = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12",
           "Ctrl + F1", "Ctrl + F2", "Ctrl + F3", "Ctrl + F4", "Ctrl + F5", "Ctrl + F6",
           "Ctrl + F7", "Ctrl + F8", "Ctrl + F9", "Ctrl + F10", "Ctrl + F11", "Ctrl + F12",
           "Shift + F1", "Shift + F2", "Shift + F3", "Shift + F4", "Shift + F5", "Shift + F6",
           "Shift + F7", "Shift + F8", "Shift + F9", "Shift + F10", "Shift + F11", "Shift + F12"]


def PressHotkey(hotkey):
    ReturnedHotkey = Receiver.get(hotkey, "None Hotkey")
    return ReturnedHotkey()


def One():
    return pyautogui.press('f1')


def Two():
    return pyautogui.press('f2')


def Three():
    return pyautogui.press('f3')


def Four():
    return pyautogui.press('f4')


def Five():
    return pyautogui.press('f5')


def Six():
    return pyautogui.press('f6')


def Seven():
    return pyautogui.press('f7')


def Eight():
    return pyautogui.press('f8')


def Nine():
    return pyautogui.press('f9')


def Ten():
    return pyautogui.press('f10')


def Eleven():
    return pyautogui.press('f11')


def Twelve():
    return pyautogui.press('f12')


def COne():
    return pyautogui.hotkey('ctrl', 'f1')


def CTwo():
    return pyautogui.hotkey('ctrl', 'f2')


def CThree():
    return pyautogui.hotkey('ctrl', 'f3')


def CFour():
    return pyautogui.hotkey('ctrl', 'f4')


def CFive():
    return pyautogui.hotkey('ctrl', 'f5')


def CSix():
    return pyautogui.hotkey('ctrl', 'f6')


def CSeven():
    return pyautogui.hotkey('ctrl', 'f7')


def CEight():
    return pyautogui.hotkey('ctrl', 'f8')


def CNine():
    return pyautogui.hotkey('ctrl', 'f9')


def CTen():
    return pyautogui.hotkey('ctrl', 'f10')


def CEleven():
    return pyautogui.hotkey('ctrl', 'f11')


def CTwelve():
    return pyautogui.hotkey('ctrl', 'f12')


def SOne():
    return pyautogui.hotkey('shift', 'f1')


def STwo():
    return pyautogui.hotkey('shift', 'f2')


def SThree():
    return pyautogui.hotkey('shift', 'f3')


def SFour():
    return pyautogui.hotkey('shift', 'f4')


def SFive():
    return pyautogui.hotkey('shift', 'f5')


def SSix():
    return pyautogui.hotkey('shift', 'f6')


def SSeven():
    return pyautogui.hotkey('shift', 'f7')


def SEight():
    return pyautogui.hotkey('shift', 'f8')


def SNine():
    return pyautogui.hotkey('shift', 'f9')


def STen():
    return pyautogui.hotkey('shift', 'f10')


def SEleven():
    return pyautogui.hotkey('shift', 'f11')


def STwelve():
    return pyautogui.hotkey('shift', 'f12')


Receiver = {
        'F1': One,
        'F2': Two,
        'F3': Three,
        'F4': Four,
        'F5': Five,
        'F6': Six,
        'F7': Seven,
        'F8': Eight,
        'F9': Nine,
        'F10': CTen,
        'F11': CEleven,
        'F12': CTwelve,
        'Ctrl + F1': COne,
        'Ctrl + CF2': CTwo,
        'Ctrl + CF3': CThree,
        'Ctrl + CF4': CFour,
        'Ctrl + CF5': CFive,
        'Ctrl + CF6': CSix,
        'Ctrl + CF7': CSeven,
        'Ctrl + CF8': CEight,
        'Ctrl + CF9': CNine,
        'Ctrl + CF10': CTen,
        'Ctrl + CF11': CEleven,
        'Ctrl + CF12': CTwelve,
        'Shift + F1': SOne,
        'Shift + F2': STwo,
        'Shift + F3': SThree,
        'Shift + F4': SFour,
        'Shift + F5': SFive,
        'Shift + F6': SSix,
        'Shift + F7': SSeven,
        'Shift + F8': SEight,
        'Shift + F9': SNine,
        'Shift + F10': STen,
        'Shift + F11': SEleven,
        'Shift + F12': STwelve
    }
