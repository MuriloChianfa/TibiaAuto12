from tkinter import RAISED, SUNKEN

from core.Defaults import rgb


def ToggleState(state, button, checking_buttons, start_thread_fn, stop_thread_fn):
    if not state:
        state = True
        button.configure(
            text='AutoHealing: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
        print("AutoHealing: ON")
        checking_buttons()
        start_thread_fn()
    else:
        state = False
        print("AutoHealing: OFF")
        checking_buttons()
        button.configure(
            text='AutoHealing: OFF', relief=RAISED, bg=rgb((114, 0, 0)))
        stop_thread_fn()
