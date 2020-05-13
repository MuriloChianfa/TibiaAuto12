import time
import collections
from ctypes import windll
import win32ui
import win32gui
import cv2
import numpy as np
import pygetwindow as gw
from PIL import Image, ImageOps

from GetHWND import GetHWND


Box = collections.namedtuple('Box', 'left top width height')
Point = collections.namedtuple('Point', 'x y')
LOAD_COLOR = cv2.IMREAD_COLOR
LOAD_GRAYSCALE = cv2.IMREAD_GRAYSCALE
USE_IMAGE_NOT_FOUND_EXCEPTION = True

unicode = str

hwnd = GetHWND('Projetor em janela')


class ImageNotFoundException(Exception):
    pass


class Hooker:
    def __init__(self, HWND):
        self.hwnd = HWND
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

    def HookWindow(self):
        if self.result == 1:
            return self.TakedImage
        else:
            return print('Error From HookWindow')


def TakeImage(Region=None):
    TakedImage = Hooker(hwnd).HookWindow()
    if Region is not None:
        TakedImage = TakedImage.crop((Region[0], Region[1], Region[0] + (Region[2] - Region[0]), Region[1] + (Region[3] - Region[1])))
        return TakedImage
    else:
        return TakedImage


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


def LocateCenterImage(image, Region=None, Precision=0.8):
    TakedImage = TakeImage(Region)

    img_rgb = np.array(TakedImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, LocatedPrecision, min_loc, Position = cv2.minMaxLoc(res)
    if LocatedPrecision > Precision:
        needleWidth, needleHeight = GetSize(image)
        if needleWidth:
            return Position[0] + int(needleWidth / 2), Position[1] + int(needleHeight / 2)
        else:
            print('Error From LocateCenterImage')
    return 0, 0


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


def PixelMatchesColor(X, Y, expectedRGBColor):
    TakedImage = TakeImage(Region=(X, Y, X + 1, Y + 1))
    rgb = TakedImage.getpixel((0, 0))
    if rgb == expectedRGBColor:
        return True
    else:
        return False


def SaveImage(Name, Region=None):
    TakedImage = TakeImage(Region)
    return TakedImage.save(Name)


def GetSize(needleImage):
    needleFileObj = open(needleImage, 'rb')
    needleImage = Image.open(needleFileObj)
    needleImage = ImageOps.grayscale(needleImage)
    needleWidth, needleHeight = needleImage.size
    return needleWidth, needleHeight
