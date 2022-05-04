import ctypes
from ctypes import wintypes
from collections import namedtuple
from Core.GetHWND import GetHWND


def check_zero(result, func, args):
    if not result:
        err = ctypes.get_last_error()

        if err:
            raise ctypes.WinError(err)

    return args


if not hasattr(wintypes, 'LPDWORD'): # PY2
    wintypes.LPDWORD = ctypes.POINTER(wintypes.DWORD)

WindowInfo = namedtuple('WindowInfo', 'hwnd title')

WNDENUMPROC = ctypes.WINFUNCTYPE(
    wintypes.BOOL,
    wintypes.HWND,    # _In_ hWnd
    wintypes.LPARAM,) # _In_ lParam

user32 = ctypes.WinDLL('user32', use_last_error=True)

user32.EnumWindows.errcheck = check_zero
user32.EnumWindows.argtypes = (
   WNDENUMPROC,      # _In_ lpEnumFunc
   wintypes.LPARAM,) # _In_ lParam

user32.IsWindowVisible.argtypes = (
    wintypes.HWND,) # _In_ hWnd

user32.GetWindowThreadProcessId.restype = wintypes.DWORD
user32.GetWindowThreadProcessId.argtypes = (
  wintypes.HWND,     # _In_      hWnd
  wintypes.LPDWORD,) # _Out_opt_ lpdwProcessId

user32.GetWindowTextLengthW.errcheck = check_zero
user32.GetWindowTextLengthW.argtypes = (
   wintypes.HWND,) # _In_ hWnd

user32.GetWindowTextW.errcheck = check_zero
user32.GetWindowTextW.argtypes = (
    wintypes.HWND,   # _In_  hWnd
    wintypes.LPWSTR, # _Out_ lpString
    ctypes.c_int,)   # _In_  nMaxCount


def get_titles():
    titles = {}

    @WNDENUMPROC
    def enum_proc(hWnd, lParam):
        if not user32.IsWindowVisible(hWnd):
            return True

        pid = wintypes.DWORD()
        user32.GetWindowThreadProcessId(
                    hWnd, ctypes.byref(pid))
        length = user32.GetWindowTextLengthW(hWnd) + 1
        title = ctypes.create_unicode_buffer(length)
        user32.GetWindowTextW(hWnd, title, length)

        titles[GetHWND(title.value)] = title.value

        return True

    user32.EnumWindows(enum_proc, 0)

    return titles
