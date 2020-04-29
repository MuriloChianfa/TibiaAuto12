import collections
import win32ui
from ctypes import windll
import numpy as np
import cv2
from PIL import Image

from SendToClient import *


Box = collections.namedtuple('Box', 'left top width height')
LOAD_COLOR = cv2.IMREAD_COLOR
LOAD_GRAYSCALE = cv2.IMREAD_GRAYSCALE
USE_IMAGE_NOT_FOUND_EXCEPTION = True

unicode = str


class ImageNotFoundException(Exception):
    pass


with open('Loads.json', 'r') as LoadsJson:
    data = json.load(LoadsJson)

hwnd = data['hwnd']


def HookWindow():
    left, top, right, bot = win32gui.GetClientRect(hwnd)
    left = left + 8
    top = top + 31
    right = right + 8
    bot = bot + 8
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    TakedImage = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    if result == 1:
        return TakedImage
    else:
        return print('Error From HookWindow')


def TakeImage(Region=None):
    TakedImage = HookWindow()
    if Region is not None:
        TakedImage = TakedImage.crop((Region[0], Region[1], Region[0] + (Region[2] - Region[0]), Region[1] + (Region[3] - Region[1])))
        return TakedImage
    else:
        return TakedImage


def LocateImage(image, Region=None, ImageNumber=0, **kwargs):
    TakedImage = TakeImage(Region)
    retVal = tuple(SearchAll(image, TakedImage, **kwargs))
    if len(retVal) > 0:
        Value = retVal[ImageNumber]
        return Value[0] + Region[0], Value[1] + Region[1]
    else:
        return False, False


def LocateAllImages(image, Region=None, **kwargs):
    TakedImage = TakeImage(Region)
    retVal = SearchAll(image, TakedImage, **kwargs)
    return len(list(retVal))


def PixelMatchesColor(X, Y, expectedRGBColor, Precision=0):
    ReturnedPixel = TakeImage(Region=(X, Y, X + 1, Y + 1))
    pix = ReturnedPixel.load()
    R, G, B = pix[0, 0]
    ExpectedR, ExpectedG, ExpectedB = expectedRGBColor
    if (R - ExpectedR) <= Precision and (G - ExpectedG) <= Precision and (B - ExpectedB) <= Precision:
        return True
    else:
        return False


def SaveImage(Name, Region=None):
    img = TakeImage(Region)
    return img.save(Name)


def LoadCV2(img, grayscale=True):
    if isinstance(img, (str, unicode)):
        if grayscale:
            img_cv = cv2.imread(img, LOAD_GRAYSCALE)
        else:
            img_cv = cv2.imread(img, LOAD_COLOR)
        if img_cv is None:
            raise IOError("Failed to read %s because file is missing, "
                          "has improper permissions, or is an "
                          "unsupported or invalid format" % img)
    elif isinstance(img, np.ndarray):
        if grayscale and len(img.shape) == 3:
            img_cv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            img_cv = img
    elif hasattr(img, 'convert'):
        img_array = np.array(img.convert('RGB'))
        img_cv = img_array[:, :, ::-1].copy()
        if grayscale:
            img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    else:
        raise TypeError('expected an image filename, OpenCV numpy array, or PIL image')
    return img_cv


def SearchAll(needleImage, haystackImage, grayscale=True, limit=10000, Region=None, step=1, Precision=0.999):
    confidence = float(Precision)

    needleImage = LoadCV2(needleImage, grayscale)
    needleHeight, needleWidth = needleImage.shape[:2]
    haystackImage = LoadCV2(haystackImage, grayscale)

    if Region:
        haystackImage = haystackImage[Region[1]:Region[1]+Region[3],
                                      Region[0]:Region[0]+Region[2]]
    else:
        Region = (0, 0)

    if haystackImage.shape[0] < needleImage.shape[0] or haystackImage.shape[1] < needleImage.shape[1]:
        raise ValueError('needle dimension(s) exceed the haystack image or region dimensions')

    if step == 2:
        confidence *= 0.95
        needleImage = needleImage[::step, ::step]
        haystackImage = haystackImage[::step, ::step]
    else:
        step = 1

    result = cv2.matchTemplate(haystackImage, needleImage, cv2.TM_CCOEFF_NORMED)
    match_indices = np.arange(result.size)[(result > confidence).flatten()]
    matches = np.unravel_index(match_indices[:limit], result.shape)

    if len(matches[0]) == 0:
        print('Image Not Recognized')
        pass

    X = matches[1] * step + Region[0]
    Y = matches[0] * step + Region[1]
    for x, y in zip(X, Y):
        yield Box(x, y, needleWidth, needleHeight)
