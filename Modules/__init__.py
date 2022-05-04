import time
import json
import os
import threading

from Core.GUI import *
from Conf.WindowTitles import get_titles
from Modules.ChooseConfig import ChooseConfig

from Modules.Root import root

titles = get_titles()

'''
    Starts The Interface For Your Visualization.
'''


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
    SelectCharacter.iconbitmap('images/icone2.ico')

    with open('Scripts/Loads.json', 'r') as LoadsJson:
        data = json.load(LoadsJson)

    print('\033[33m' + "Start in 1 Seconds...")

    def exiting():
        print("Exiting...")

        try:
            SelectCharacter.destroy()
            exit(0)
        except Exception as Ex:
            print(Ex)
            exit(0)

    '''
        The Reconfigure Function, Verify If Already Exist One File
        With The Name Placed On Loads.Json.
        
        If Already Have One Archive, He Destroy The Archive And Restart The Program.
    '''

    def Reconfigure():
        with open('Scripts/Loads.json', 'r') as LoadsJson:
            data = json.load(LoadsJson)

        if os.path.isfile('Scripts/' + data['ScriptName'] + '.json'):
            data['Auto'] = False
            with open('Scripts/Loads.json', 'w') as wJson:
                json.dump(data, wJson, indent=4)
            os.remove('Scripts/' + data['ScriptName'] + '.json')
            global Discovered
            Discovered = False
            time.sleep(.2)
            SelectCharacter.destroy()
            time.sleep(.4)
            from StartBot import main
            main()

    '''
        This Function Is Called When Player Click On 'Configure Button', or 'Load Up Button',
        If Dont Have One Character On Your ComboBox, He Just Ignore And Waits
        The Player Enter With One Character In The Tibia Client.
        
        Otherwise If The Player Have Already Logon, He Verify On Loads.Json,
        If The Status == True:
            He Verify The Name Of Script Placed On Loads.json
            If Exist, He Throw You For Root Window, In The 'Modules' Folder In The 'Root.py'
        If The Status == False:
            He Throw You For ChooseConfig Window In The 'Modules' Folder In The 'ChooseConfig.py'
    '''

    def ReadyToConfig():
        with open('Scripts/Loads.json', 'r') as LoadsJson:
            data = json.load(LoadsJson)

        selected_hwnd = list(titles.keys())[list(titles.values()).index(Char.get())]

        SelectCharacter.destroy()
        time.sleep(0.1)
        if not data['Auto']:
            ChooseConfig(Char.get())
            return

        if data['ScriptName'] is None:
            data['ScriptName'] = 'NewConfig'

        if not os.path.isfile('Scripts/' + data['ScriptName'] + '.json'):
            print("File Not Loaded")
            exiting()

        data['hwnd'] = selected_hwnd
        with open('Scripts/Loads.json', 'w') as wJson:
            json.dump(data, wJson, indent=4)

        root(Char.get(), data['ScriptName'])

    Char = tk.StringVar()
    Char.set(list(titles.values())[1])

    OptionSelectCharacter = tk.OptionMenu(SelectCharacter, Char, *list(titles.values()))
    OptionSelectCharacter.configure(anchor='w')
    OptionSelectCharacter.pack()
    OptionSelectCharacter.place(w=230, h=24, x=15, y=17)

    # region Buttons

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

    if data['Auto']:
        ExitButton = tk.Button(SelectCharacter, width=15, text="Reconfigure", command=Reconfigure, bg=rgb((127, 17, 8)),
                               fg='white',
                               activebackground=rgb((123, 13, 5)))
    else:
        ExitButton = tk.Button(SelectCharacter, width=15, text="Exit", command=exiting, bg=rgb((127, 17, 8)),
                               fg='white',
                               activebackground=rgb((123, 13, 5)))

    ExitButton.pack()
    ExitButton.place(w=85, h=25, x=28, y=53)

    # endregion

    SelectCharacter.mainloop()
