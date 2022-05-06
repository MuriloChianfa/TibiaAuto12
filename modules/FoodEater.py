"""
Food eater module
"""

from conf.Hotkeys import Hotkey

from core.GUI import *
from core.GUIManager import *
from core.GUISetter import GUISetter, check_gui
from core.ThreadManager import ThreadManager


class FoodEater:
    started = False
    enabled = False

    gui_changes = []

    def __init__(self, root, MOUSE_OPTION):
        self.root = root
        self.window = GUI('FoodEater', 'Module: Food Eater')
        self.window.DefaultWindow('FoodEater', [306, 191], [1.2, 2.29])
        self.Setter = GUISetter("FoodEaterLoader")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.ThreadManager = ThreadManager("ThreadFoodEater")

        self.gui_vars()
        self.gui()

        self.check()
        self.check_state()

        self.window.Protocol(self.destroy)
        self.window.loop()

    def trigger(self):
        if FoodEater.enabled:
            FoodEater.enabled = False
            self.enabled_button.configure(text='FoodEater: OFF', relief=RAISED, bg=rgb((127, 17, 8)))
            self.pause()
        else:
            FoodEater.enabled = True
            self.enabled_button.configure(text='FoodEater: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
            self.run()

        self.check()
        self.check_state()

    def run(self):
        if not FoodEater.started:
            self.ThreadManager.NewThread(self.execute)
            FoodEater.started = False
        else:
            self.ThreadManager.UnPauseThread()
        print('FoodEater: ON')

    def pause(self):
        self.ThreadManager.PauseThread()
        print('FoodEater: OFF')

    def execute(self):
        while FoodEater.enabled:
            print('Hotkey to eat food: ', self.food_hotkey.get())

    def destroy(self):
        check_gui(FoodEater.gui_changes, self.init_check_print, self.check_print.get(), 'CheckPrint')
        check_gui(FoodEater.gui_changes, self.init_food_hotkey, self.food_hotkey.get(), 'HotkeyFood')

        if len(FoodEater.gui_changes) != 0:
            for each_change in range(len(FoodEater.gui_changes)):
                self.Setter.SetVariables.SetVar(
                    FoodEater.gui_changes[each_change][0],
                    FoodEater.gui_changes[each_change][1]
                )

        if not FoodEater.enabled:
            print('Killing thread: ', self.ThreadManager)
            self.ThreadManager.KillThread()

        self.window.destroyWindow()

    def gui_vars(self):
        self.check_print, self.init_check_print = self.Setter.Variables.Bool('CheckPrint')
        self.food_hotkey, self.init_food_hotkey = self.Setter.Variables.Str('HotkeyFood')

    def gui(self):
        self.label = self.window.addLabel('Hotkey To Press', [110, 24])

        self.hotkey_button = self.window.addOption(self.food_hotkey, self.SendToClient.Hotkeys, [105, 50], 10)

        self.check_print_button = self.window.addCheck(self.check_print, [11, 100], self.init_check_print,
                                                       "Print on Tibia's screen")
        self.check_print_button.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                       selectcolor=rgb((114, 94, 48)))

        if not FoodEater.enabled:
            self.enabled_button = self.window.addButton('FoodEater: OFF', self.trigger, [287, 23], [11, 132])
        else:
            self.enabled_button = self.window.addButton('FoodEater: ON', self.trigger, [287, 23], [11, 132]) \
                .configure(relief=SUNKEN, bg=rgb((158, 46, 34)))

        self.ok_button = self.window.addButton('Ok', self.destroy, [73, 21], [115, 161])

    def check(self):
        if FoodEater.enabled:
            self.hotkey_button.configure(state='disabled')
        else:
            self.hotkey_button.configure(state='normal')

    def check_state(self):
        if FoodEater.enabled:
            Disable(self.label)
            Disable(self.hotkey_button)
            Disable(self.check_print_button)
        else:
            Enable(self.label)
            Enable(self.hotkey_button)
            Enable(self.check_print_button)

        ExecGUITrigger()
