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
    return pyautogui.press('f1', presses=2)


def Two():
    return pyautogui.press('f2', presses=2)


def Three():
    return pyautogui.press('f3', presses=2)


def Four():
    return pyautogui.press('f4', presses=2)


def Five():
    return pyautogui.press('f5', presses=2)


def Six():
    return pyautogui.press('f6', presses=2)


def Seven():
    return pyautogui.press('f7', presses=2)


def Eight():
    return pyautogui.press('f8', presses=2)


def Nine():
    return pyautogui.press('f9', presses=2)


def Ten():
    return pyautogui.press('f10', presses=2)


def Eleven():
    return pyautogui.press('f11', presses=2)


def Twelve():
    return pyautogui.press('f12', presses=2)


def COne():
    return pyautogui.hotkey('ctrl', 'f1', presses=2)


def CTwo():
    return pyautogui.hotkey('ctrl', 'f2', presses=2)


def CThree():
    return pyautogui.hotkey('ctrl', 'f3', presses=2)


def CFour():
    return pyautogui.hotkey('ctrl', 'f4', presses=2)


def CFive():
    return pyautogui.hotkey('ctrl', 'f5', presses=2)


def CSix():
    return pyautogui.hotkey('ctrl', 'f6', presses=2)


def CSeven():
    return pyautogui.hotkey('ctrl', 'f7', presses=2)


def CEight():
    return pyautogui.hotkey('ctrl', 'f8', presses=2)


def CNine():
    return pyautogui.hotkey('ctrl', 'f9', presses=2)


def CTen():
    return pyautogui.hotkey('ctrl', 'f10', presses=2)


def CEleven():
    return pyautogui.hotkey('ctrl', 'f11', presses=2)


def CTwelve():
    return pyautogui.hotkey('ctrl', 'f12', presses=2)


def SOne():
    return pyautogui.hotkey('shift', 'f1', presses=2)


def STwo():
    return pyautogui.hotkey('shift', 'f2', presses=2)


def SThree():
    return pyautogui.hotkey('shift', 'f3', presses=2)


def SFour():
    return pyautogui.hotkey('shift', 'f4', presses=2)


def SFive():
    return pyautogui.hotkey('shift', 'f5', presses=2)


def SSix():
    return pyautogui.hotkey('shift', 'f6', presses=2)


def SSeven():
    return pyautogui.hotkey('shift', 'f7', presses=2)


def SEight():
    return pyautogui.hotkey('shift', 'f8', presses=2)


def SNine():
    return pyautogui.hotkey('shift', 'f9', presses=2)


def STen():
    return pyautogui.hotkey('shift', 'f10', presses=2)


def SEleven():
    return pyautogui.hotkey('shift', 'f11', presses=2)


def STwelve():
    return pyautogui.hotkey('shift', 'f12', presses=2)


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
        'F10': Ten,
        'F11': Eleven,
        'F12': Twelve,
        'Ctrl + F1': COne,
        'Ctrl + F2': CTwo,
        'Ctrl + F3': CThree,
        'Ctrl + F4': CFour,
        'Ctrl + F5': CFive,
        'Ctrl + F6': CSix,
        'Ctrl + F7': CSeven,
        'Ctrl + F8': CEight,
        'Ctrl + F9': CNine,
        'Ctrl + F10': CTen,
        'Ctrl + F11': CEleven,
        'Ctrl + F12': CTwelve,
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
