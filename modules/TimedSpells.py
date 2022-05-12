"""
Food eater module
"""

from time import sleep

from conf.Hotkeys import Hotkey

from core.GUI import *
from core.GUIManager import *
from core.GUISetter import GUISetter, check_gui

from tkinter import CENTER, VERTICAL

from core.ThreadManager import ThreadManager

from engine.ScanFood import scan_food


class TimedSpells:
    started = False
    enabled = False

    gui_changes = []

    def __init__(self, root, MOUSE_OPTION):
        self.root = root
        self.window = GUI('TimedSpells', 'Module: Timed spells')
        self.window.DefaultWindow('TimedSpells', [306, 473], [1.2, 2.29])
        self.Setter = GUISetter("TimedSpellsLoader")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.ThreadManager = ThreadManager("ThreadTimedSpells")

        self.gui_vars()
        self.gui()

        self.check()
        self.check_state()

        self.window.Protocol(self.destroy)
        self.window.loop()

    def trigger(self):
        if TimedSpells.enabled:
            TimedSpells.enabled = False
            self.enabled_button.configure(text='TimedSpells: OFF', relief=RAISED, bg=rgb((127, 17, 8)))
            self.pause()
        else:
            TimedSpells.enabled = True
            self.enabled_button.configure(text='TimedSpells: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
            self.run()

        self.check()
        self.check_state()

    def trigger_table(self):
        self.check()
        self.check_state()

    def run(self):
        if not TimedSpells.started:
            self.ThreadManager.NewThread(self.execute)
            TimedSpells.started = False
        else:
            self.ThreadManager.UnPauseThread()
        print('TimedSpells: ON')

    def pause(self):
        self.ThreadManager.PauseThread()
        print('TimedSpells: OFF')

    def execute(self):
        hotkey = 0
        cast_time = 1
        current_time = 2

        spells = []

        for spell in self.table.get_children():
            spells.append(self.table.item(spell)["values"])

        for spell in spells:
            if self.check_instant.get():
                self.SendToClient.Press(spell[hotkey])

            spell.extend([0])

        while TimedSpells.enabled:
            for spell in spells:
                spell[current_time] += 1

                if spell[cast_time] == spell[current_time]:
                    spell[current_time] = 0
                    self.SendToClient.Press(spell[hotkey])

            sleep(1)

    def destroy(self):
        check_gui(TimedSpells.gui_changes, self.init_check_print, self.check_print.get(), 'CheckPrint')
        check_gui(TimedSpells.gui_changes, self.init_instant, self.check_instant.get(), 'InstantExecute')
        check_gui(TimedSpells.gui_changes, self.init_food_hotkey, self.food_hotkey.get(), 'Hotkey')

        spells = []

        for spell in self.table.get_children():
            spells.append(self.table.item(spell)["values"])

        check_gui(TimedSpells.gui_changes, self.init_spells, spells, 'Spells')

        if len(TimedSpells.gui_changes) != 0:
            for each_change in range(len(TimedSpells.gui_changes)):
                self.Setter.SetVariables.SetVar(
                    TimedSpells.gui_changes[each_change][0],
                    TimedSpells.gui_changes[each_change][1]
                )

        if not TimedSpells.enabled:
            print('Killing thread: ', self.ThreadManager)
            self.ThreadManager.KillThread()

        self.window.destroyWindow()

    def gui_vars(self):
        self.check_print, self.init_check_print = self.Setter.Variables.Bool('CheckPrint')
        self.check_instant, self.init_instant = self.Setter.Variables.Bool('InstantExecute')
        self.food_hotkey, self.init_food_hotkey = self.Setter.Variables.Str('Hotkey')
        self.cast_every, self.init_cast_every = self.Setter.Variables.Str('CastEvery')
        self.spells, self.init_spells = self.Setter.Variables.array('Spells')

    def validate_cast_every(self, *args):
        seconds = self.entry_cast_every.get()

        if len(seconds) < 2:
            return

        if not seconds[-1].isdigit():
            self.cast_every.set(seconds[:-1])
            return

        self.cast_every.set(seconds[:2])

    def remove_item(self):
        current_item = self.table.focus()

        if (type(self.table.item(current_item)['values']) is str):
            return

        # print(self.table.item(current_item))
        self.table.delete(current_item)

    def add_item(self):
        for child in self.table.get_children():
            if self.food_hotkey.get() in self.table.item(child)["values"]:
                return

        # print(self.table.item(child)["values"])

        self.table.insert('', tk.END, text='', values=(
            self.food_hotkey.get(),
            self.entry_cast_every.get()
        ))

    def gui(self):
        self.label = self.window.addLabel('Hotkey to press', [40, 45])
        self.hotkey_button = self.window.addOption(self.food_hotkey, self.SendToClient.Hotkeys, [145, 40], 10)

        self.label2 = self.window.addLabel('Cast every', [40, 75])
        self.label3 = self.window.addLabel('seconds', [230, 75])
        self.entry_cast_every = self.window.addEntry([145, 75], self.cast_every, 12)
        self.cast_every.trace("w", self.validate_cast_every)

        self.add_button = self.window.addButton('Add', self.add_item, [75, 23], [70, 110])
        self.remove_button = self.window.addButton('Remove', self.remove_item, [75, 23], [170, 110])

        self.table = self.window.addList(('hotkey', 'time'), 8, [230, 100], [40, 150])

        self.table.column('hotkey', width=115)
        self.table.column('time', anchor=CENTER, width=115)

        self.table.heading('hotkey', text="Hotkey", anchor=CENTER)
        self.table.heading('time', text="Time", anchor=CENTER)

        self.scroll = self.window.addScrollbar()

        self.table.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.table.yview)

        for spell in self.init_spells:
            self.table.insert('', tk.END, text='', values=(
                spell[0],
                spell[1]
            ))

        self.check_print_button = self.window.addCheck(self.check_print, [11, 365], self.init_check_print,
                                                       "Print on Tibia's screen")
        self.check_print_button.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                          selectcolor=rgb((114, 94, 48)))

        self.check_instant_button = self.window.addCheck(self.check_instant, [11, 385], self.init_instant,
                                                         "Execute instant")
        self.check_instant_button.configure(bg=rgb((114, 94, 48)), activebackground=rgb((114, 94, 48)),
                                            selectcolor=rgb((114, 94, 48)))

        if not TimedSpells.enabled:
            self.enabled_button = self.window.addButton('TimedSpells: OFF', self.trigger, [287, 23], [11, 411])
        else:
            self.enabled_button = self.window.addButton('TimedSpells: ON', self.trigger, [287, 23], [11, 411])
            self.enabled_button.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))

        self.ok_button = self.window.addButton('Ok', self.destroy, [73, 21], [115, 440])

    def check(self):
        if TimedSpells.enabled:
            self.hotkey_button.configure(state='disabled')
        else:
            self.hotkey_button.configure(state='normal')

    def check_state(self):
        if TimedSpells.enabled:
            Disable(self.label)
            Disable(self.hotkey_button)
            Disable(self.check_print_button)
            Disable(self.label2)
            Disable(self.label3)
            Disable(self.entry_cast_every)
            Disable(self.add_button)
            Disable(self.remove_button)
            Disable(self.check_instant_button)
        else:
            Enable(self.label)
            Enable(self.hotkey_button)
            Enable(self.check_print_button)
            Enable(self.label2)
            Enable(self.label3)
            Enable(self.entry_cast_every)
            Enable(self.add_button)
            Enable(self.remove_button)
            Enable(self.check_instant_button)

        ExecGUITrigger()
