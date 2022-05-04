import pygetwindow as gw


def GetHWND(Title):
    try:
        a = gw.getWindowsWithTitle(Title)
        a = str(a)
        b = a.split('=', 1)
        b = b[1].split(')', 1)
        hwnd = int(b[0])
        return hwnd
    except Exception as Ex:
        print("From GetHWND.py: ", Ex)
        print(f"Window Not Located: '{Title}', Trying Again")
        return 0
