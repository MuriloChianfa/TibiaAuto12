import time
import cv2
import multiprocessing as mp
import numpy as np
from datetime import datetime
from tkinter import messagebox
from PIL import ImageOps

from core.GUI import *

from conf.conf_manager import ConfManager

platform = ConfManager.get('conf.json')['platform']

if platform == "windows":
    from ctypes import windll
    import win32ui
    import win32gui
elif platform == "linux":
    import os
    from core.LinuxClient import Execute, FindAnotherWindow, FindWindow

    TEMPLATES_PATH = os.path.dirname(__file__) + "/../images/"

    AnotherWindow = FindAnotherWindow()
    Window = FindWindow()


class Hooker:
    if platform == 'windows':
        def __init__(self):
            self.hwnd = ConfManager.get('conf.json')['hwnd']
            while win32gui.IsIconic(self.hwnd):
                time.sleep(1)
            self.dll = windll.user32
            try:
                self.hwndDC = win32gui.GetWindowDC(self.hwnd)
            except:
                messagebox.showerror(
                    'Tibia window not detected!', 'Please open a Tibia instance or focus the existing window again.')
                GUI.ExitGUI()
            self.mfcDC = win32ui.CreateDCFromHandle(self.hwndDC)
            self.saveDC = self.mfcDC.CreateCompatibleDC()
            self.saveBitMap = win32ui.CreateBitmap()
            self.left, self.top, self.right, self.bot = win32gui.GetClientRect(
                self.hwnd)
            self.left = self.left + 8
            self.top = self.top + 8
            self.right = self.right + 8
            self.bot = self.bot + 8
            self.w = self.right - self.left
            self.h = self.bot - self.top
            self.saveBitMap.CreateCompatibleBitmap(
                self.mfcDC, self.w, self.h)
            self.saveDC.SelectObject(self.saveBitMap)
            self.targetWindowIsFocused = self.dll.PrintWindow(
                self.hwnd, self.saveDC.GetSafeHdc(), 1)

            self.bmpinfo = self.saveBitMap.GetInfo()
            self.bmpstr = self.saveBitMap.GetBitmapBits(True)

            self.TakenImage = Image.frombuffer(
                'RGB',
                (self.bmpinfo['bmWidth'], self.bmpinfo['bmHeight']),
                self.bmpstr, 'raw', 'BGRX', 0, 1)

            win32gui.DeleteObject(self.saveBitMap.GetHandle())
            self.saveDC.DeleteDC()
            self.mfcDC.DeleteDC()
            win32gui.ReleaseDC(self.hwnd, self.hwndDC)

    elif platform == 'linux':
        def __init__(self, Filename="images/tmp_screen.png"):
            Execute(["scrot", "-u", Filename])
            self.TakenImage = cv2.imread(Filename)

            if self.TakenImage is not None:
                self.targetWindowIsFocused = 1

    def HookWindow(self):
        return self.TakenImage


'''
    Here It Call The Hook Class, Passing The Region For Crop,
    Returning The Img Cropped.
'''


def TakeImage(Region=None):
    Except = True
    while Except:
        try:
            TakenImage = Hooker().HookWindow()
            if Region is not None:
                TakenImage = TakenImage.crop(
                    (Region[0], Region[1], Region[0] + (Region[2] - Region[0]), Region[1] + (Region[3] - Region[1])))
                Except = False
                return TakenImage
            else:
                Except = False
                return TakenImage
        except Exception as Ex:
            print('Ex', Ex)
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
    TakenImage = TakeImage(Region)

    img_rgb = np.array(TakenImage)
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
    TakenImage = TakeImage(Region)

    img_rgb = np.array(TakenImage)
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
    TakenImage = TakeImage(Region)

    TakenImage = np.array(TakenImage)
    img_gray = cv2.cvtColor(TakenImage, cv2.COLOR_BGR2GRAY)
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
    TakenImage = TakeImage(Region=(X, Y, X + 1, Y + 1))
    rgb = TakenImage.getpixel((0, 0))
    if rgb == expectedRGBColor:
        return True
    else:
        return False


'''
    When Called, It Save The Image On Folder And Name Passed Per Argument, Examples:
    
    1°: SaveImage('TakenImage.png') == Save The Image In Current Directory,
    2°: SaveImage('images/Foods/Cheese.png', (1234, 435, 1280, 460)) == Save The Image On Passed Folder,
    And Crop Then In X: 1234 Up Until 1280 And Y: 435 Up Until 460.
'''


def SaveImage(Name, Region=None):
    TakenImage = TakeImage(Region)
    return TakenImage.save(Name)


def GetImageSize(needleImage):
    needleFileObj = open(needleImage, 'rb')
    needleImage = Image.open(needleFileObj)
    needleImage = ImageOps.grayscale(needleImage)
    needleWidth, needleHeight = needleImage.size
    return needleWidth, needleHeight


def IsFocused():
    return int(win32gui.GetForegroundWindow())
