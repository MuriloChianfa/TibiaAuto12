import time
import json
import os
import threading

from random import randint
from Conf.WindowTitles import *
from Engine.GUI import *
from GetHWND import GetHWND
from ChooseConfig import ChooseConfig

from root import root

Discovered = False
data = None


def WindowSelectCharacter():
    SelectCharacter = tk.Tk()
    w = 260
    h = 90
    sw = SelectCharacter.winfo_screenwidth()
    sh = SelectCharacter.winfo_screenheight()
    x = (sw - w) / 2.3
    y = (sh - h) / 2.4
    SelectCharacter.geometry('%dx%d+%d+%d' % (w, h, x, y))
    SelectCharacter.resizable(width=False, height=False)
    SelectCharacter.title('Choose Your Character')
    SelectCharacter.configure(background=rgb((120, 98, 51)), takefocus=True)

    CHARACTERS = [""]

    print('\033[33m' + "Start in 1 Seconds...")

    def Searcher():
        global Discovered, data
        while not Discovered:
            try:
                TibiaName = FindTibiaTitle()
                TibiaCharacter = TibiaName.split(' - ')
                if TibiaCharacter:
                    Discovered = True
                    NumberOfTheClient = str(randint(1000, 9999))
                    CHARACTERS[0] = '[' + NumberOfTheClient + '] ' + TibiaCharacter[1]
                    Char.set(CHARACTERS[0])
                    print(CHARACTERS[0])
                    try:
                        hwnd = GetHWND('Tibia - ')
                        with open('Loads.json', 'r') as LoadsJson:
                            data = json.load(LoadsJson)

                        print('You Current Tibia HWND: ', hwnd)

                        data['hwnd'] = hwnd
                        with open('Loads.json', 'w') as wJson:
                            json.dump(data, wJson, indent=4)
                    except Exception:
                        print('')
                        exit(1)
                    OptionSelectCharacter.configure(*CHARACTERS[0])
                    break
            except Exception:
                pass

    def exiting():
        exit(1)

    def ReadyToConfig():
        global data
        if CHARACTERS[0] != '':
            SelectCharacter.destroy()
            time.sleep(0.1)
            if data['Auto']:
                ScriptName = data['ScriptName']
                if os.path.isfile(ScriptName + '.json'):
                    root(CHARACTERS[0], ScriptName)
                else:
                    print("File Not Loaded")
                    exiting()
            else:
                ChooseConfig(CHARACTERS[0])
        else:
            print('Please, Login First')

    Char = tk.StringVar()
    Char.set(CHARACTERS[0])

    OptionSelectCharacter = tk.OptionMenu(SelectCharacter, Char, *CHARACTERS)
    OptionSelectCharacter.configure(anchor='w')
    OptionSelectCharacter.pack()
    OptionSelectCharacter.place(w=230, h=24, x=15, y=17)

    with open('Loads.json', 'r') as LoadsJson:
        data = json.load(LoadsJson)

    if data['Auto']:
        ConfigButton = tk.Button(SelectCharacter, width=15, text="Load Up", command=ReadyToConfig, bg=rgb((127, 17, 8)),
                                 fg='white',
                                 activebackground=rgb((123, 13, 5)))
        ConfigButton.pack()
        ConfigButton.place(w=85, h=25, x=140, y=53)
    else:
        ConfigButton = tk.Button(SelectCharacter, width=15, text="Configure", command=ReadyToConfig,
                                 bg=rgb((127, 17, 8)),
                                 fg='white',
                                 activebackground=rgb((123, 13, 5)))
        ConfigButton.pack()
        ConfigButton.place(w=85, h=25, x=140, y=53)

    ExitButton = tk.Button(SelectCharacter, width=15, text="Exit", command=exiting, bg=rgb((127, 17, 8)),
                           fg='white',
                           activebackground=rgb((123, 13, 5)))
    ExitButton.pack()
    ExitButton.place(w=85, h=25, x=28, y=53)

    ThreadSearcher = threading.Thread(target=Searcher)
    ThreadSearcher.start()

    SelectCharacter.mainloop()

