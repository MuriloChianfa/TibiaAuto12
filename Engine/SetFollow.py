from Core.HookWindow import LocateImage, LocateBoolRGBImage


def SetFollow():
    X, Y = LocateImage('images/TibiaSettings/follow.png', Precision=0.8)
    if LocateBoolRGBImage('images/TibiaSettings/follow.png', Precision=0.8, Region=(X - 3, Y - 3, X + 16, Y + 16)):
        return False
    else:
        return True
