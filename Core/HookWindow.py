import json

with open('Scripts/Loads.json', 'r') as LoadsJson:
    data = json.load(LoadsJson)

if data['Platform'] == "Windows":
    from ctypes import windll
    import win32ui
    import win32gui
    from Core.GetHWND import GetHWND

elif data['Platform'] == "Linux":
    import os
    from Core.LinuxClient import Execute, FindAnotherWindow, FindWindow

    TEMPLATES_PATH = os.path.dirname(__file__) + "/../images/"

import numpy as np
import cv2
from PIL import Image, ImageOps

'''
    The OBS Window Name, To Search For The HWND

    If You Have The Other Language, Put The 'Windowed Projector' Name Here. 
'''

if data['Platform'] == "Windows":
    hwnd = GetHWND('Windowed Projector')

    if hwnd == 0:
        hwnd = GetHWND('Projetor em janela')

    if hwnd == 0:
        exit(1)

elif data['Platform'] == "Linux":
    AnotherWindow = FindAnotherWindow()
    Window = FindWindow()


'''
    I Did This Class So There Are No Errors Between The Threads.
    Because I Throw 'self' In All Components >.< Hahahahaha.
'''


class Hooker:
    if data['Platform'] == "Windows":
        def __init__(self):
            self.hwnd = hwnd
            self.win32gui = win32gui
            self.win32ui = win32ui
            self.dll = windll.user32
            self.hwndDC = self.win32gui.GetWindowDC(self.hwnd)
            self.mfcDC = self.win32ui.CreateDCFromHandle(self.hwndDC)
            self.saveDC = self.mfcDC.CreateCompatibleDC()
            self.saveBitMap = self.win32ui.CreateBitmap()
            self.left, self.top, self.right, self.bot = self.win32gui.GetClientRect(self.hwnd)
            self.left = self.left + 8
            self.top = self.top + 8
            self.right = self.right + 8
            self.bot = self.bot + 8
            self.w = self.right - self.left
            self.h = self.bot - self.top
            self.saveBitMap.CreateCompatibleBitmap(self.mfcDC, self.w, self.h)
            self.saveDC.SelectObject(self.saveBitMap)
            self.result = self.dll.PrintWindow(self.hwnd, self.saveDC.GetSafeHdc(), 1)

            self.bmpinfo = self.saveBitMap.GetInfo()
            self.bmpstr = self.saveBitMap.GetBitmapBits(True)

            self.TakedImage = Image.frombuffer(
                'RGB',
                (self.bmpinfo['bmWidth'], self.bmpinfo['bmHeight']),
                self.bmpstr, 'raw', 'BGRX', 0, 1)

            self.win32gui.DeleteObject(self.saveBitMap.GetHandle())
            self.saveDC.DeleteDC()
            self.mfcDC.DeleteDC()
            self.win32gui.ReleaseDC(self.hwnd, self.hwndDC)

    elif data['Platform'] == "Linux":
        def __init__(self, FileName="images/tmp_screen.png"):
            Execute(["scrot", "-u", FileName])
            self.TakedImage = cv2.imread(FileName)

            if self.TakedImage is not None:
                self.result = 1

    def HookWindow(self):
        if self.result == 1:
            return self.TakedImage
        else:
            return print('Debugged From HookWindow')


'''
    Here It Call The Hook Class, Passing The Region For Crop,
    Returning The Img Cropped.
'''


def TakeImage(Region=None):
    Except = True
    while Except:
        try:
            TakedImage = Hooker().HookWindow()
            if Region is not None:
                TakedImage = TakedImage.crop(
                    (Region[0], Region[1], Region[0] + (Region[2] - Region[0]), Region[1] + (Region[3] - Region[1])))
                return TakedImage
            else:
                return TakedImage
        except Exception as Ex:
            # print("Debugged From TakeImage: ", Ex)
            Except = True
            pass


'''
    In LocateImage, It Compare With Another Image, If The Two Have Any
    Similarity To Each Other.
    
    If Have Similarity, He Return The X And Y Position.
    
    Examples:
    
    1°: LocateImage('images/TibiaSettings/BattleList.png')
    
    2°: LocateImage('images/TibiaSettings/BattleList.png', (1234, 435, 1280, 460)) == He Locate The Image On Passed Folder,
    In X: 1234 Up Until 1280 And Y: 435 Up Until 460.
'''


def LocateImage(image, Region=None, Precision=0.8):
    TakedImage = TakeImage(Region)

    img_rgb = np.array(TakedImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, LocatedPrecision, min_loc, Position = cv2.minMaxLoc(res)
    if LocatedPrecision > Precision:
        return Position[0], Position[1]
    return 0, 0


'''
    In LocateCenterImage, It Compare With Another Image, If The Two Have Any
    Similarity To Each Other.

    If Have Similarity, He Return The X And Y Position More Half Of Size The Image
    For Return The Position Of Center Of Image...
'''


def LocateCenterImage(image, Region=None, Precision=0.8):
    TakedImage = TakeImage(Region)

    img_rgb = np.array(TakedImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, LocatedPrecision, min_loc, Position = cv2.minMaxLoc(res)
    if LocatedPrecision > Precision:
        needleWidth, needleHeight = GetImageSize(image)
        if needleWidth:
            return Position[0] + int(needleWidth / 2), Position[1] + int(needleHeight / 2)
        else:
            print('Debugged From LocateCenterImage')
    return 0, 0


'''
    Here, It Search For All Images Passed From Argument
    And It Return The Number Of Images Found.
    
    Examples:
    
    LocateAllImages('images/Foods/Cheese.png'), He Search For All Cheeses On Your Screen,
    And Will Return This Number.
'''


def LocateAllImages(image, Region=None, Precision=0.8):
    TakedImage = TakeImage(Region)

    TakedImage = np.array(TakedImage)
    img_gray = cv2.cvtColor(TakedImage, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= Precision)

    Number = 0

    for pt in zip(*loc[::-1]):
        Number = Number + 1
    return Number


def LocateBoolRGBImage(image, Region=None, Precision=0.9):
    SaveImage('images/MonstersAttack/VerifyAttacking.png', Region)
    img_rgb = cv2.imread('images/MonstersAttack/VerifyAttacking.png', 0)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    min_val, LocatedPrecision, min_loc, Position = cv2.minMaxLoc(res)
    if LocatedPrecision > Precision:
        return True
    return False


'''
    In PixelMatchesColor, It Compare The RGB Color Of The Pixel Nedded,
    But This Dont Work 100% >.< Hahahaha.
    
    Example:
    
    PixelMatchesColor(657, 432, (255, 255, 255)), He Verify If Pixel X: 657 And Y: 432, Is Black.
'''


def PixelMatchesColor(X, Y, expectedRGBColor):
    TakedImage = TakeImage(Region=(X, Y, X + 1, Y + 1))
    rgb = TakedImage.getpixel((0, 0))
    if rgb == expectedRGBColor:
        return True
    else:
        return False


'''
    When Called, It Save The Image On Folder And Name Passed Per Argument, Examples:
    
    1°: SaveImage('TakedImage.png') == Save The Image In Current Directory,
    2°: SaveImage('images/Foods/Cheese.png', (1234, 435, 1280, 460)) == Save The Image On Passed Folder,
    And Crop Then In X: 1234 Up Until 1280 And Y: 435 Up Until 460.
'''


def SaveImage(Name, Region=None):
    TakedImage = TakeImage(Region)
    return TakedImage.save(Name)


def GetImageSize(needleImage):
    needleFileObj = open(needleImage, 'rb')
    needleImage = Image.open(needleFileObj)
    needleImage = ImageOps.grayscale(needleImage)
    needleWidth, needleHeight = needleImage.size
    return needleWidth, needleHeight


def IsFocused():
    return int(win32gui.GetForegroundWindow())
