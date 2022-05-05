"""
starts the selection page to choose window of capture
"""

import time
import os
import threading

from core.GUI import *
from conf.conf_manager import ConfManager
from conf.WindowTitles import get_titles
from modules.ChooseConfig import ChooseConfig

from modules.Root import root

titles = get_titles()
conf = ConfManager.get('conf.json')
script = f'scripts/{conf["preferences_name"]}'


def choose_capture_window():
    window = tk.Tk()
    w = 260
    h = 90
    x = (window.winfo_screenwidth() - w) / 2.3
    y = (window.winfo_screenheight() - h) / 2.4
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.resizable(width=False, height=False)
    window.title('Choose window')
    window.configure(background=rgb((120, 98, 51)), takefocus=True)
    window.iconbitmap('images/icon.ico')

    def destroy():
        """
        destroy current window and exit with success status
        """

        print('Exiting...')

        window.destroy()
        exit(0)

    def reconfigure():
        """
        The Reconfigure Function, Verify If Already Exist One File
        With The Name Placed On Loads.Json.

        If Already Have One Archive, He Destroy The Archive And Restart The Program.
        """

        if os.path.isfile(script):
            os.remove(script)

        conf['configured'] = False
        ConfManager.set(conf, 'conf.json')

        window.destroy()

        from start import main
        main()

    def bootstrap():
        """
        load-up configurations and pass to conf page
        """

        if conf['preferences_name'] is None:
            conf['preferences_name'] = 'NewConfig.json'

        conf['hwnd'] = list(titles.keys())[list(titles.values()).index(selected_window.get())]
        ConfManager.set(conf, 'conf.json')

        window.destroy()

        if not conf['configured']:
            ChooseConfig(selected_window.get())
            return

        root(selected_window.get(), conf['preferences_name'])

    selected_window = tk.StringVar()
    selected_window.set(list(titles.values())[1])

    select_window_list = tk.OptionMenu(window, selected_window, *list(titles.values()))
    select_window_list.configure(anchor='w')
    select_window_list.pack()
    select_window_list.place(w=230, h=24, x=15, y=17)

    # region Buttons

    if conf['configured']:
        bootstrap_button = tk.Button(window, width=15, text="Load Up", command=bootstrap, bg=rgb((127, 17, 8)),
                                     fg='white',
                                     activebackground=rgb((123, 13, 5)))
        bootstrap_button.pack()
        bootstrap_button.place(w=85, h=25, x=140, y=53)

        exit_button = tk.Button(window, width=15, text="Reconfigure", command=reconfigure, bg=rgb((127, 17, 8)),
                                fg='white',
                                activebackground=rgb((123, 13, 5)))
    else:
        bootstrap_button = tk.Button(window, width=15, text="Configure", command=bootstrap,
                                     bg=rgb((127, 17, 8)),
                                     fg='white',
                                     activebackground=rgb((123, 13, 5)))
        bootstrap_button.pack()
        bootstrap_button.place(w=85, h=25, x=140, y=53)

        exit_button = tk.Button(window, width=15, text="Exit", command=destroy, bg=rgb((127, 17, 8)),
                                fg='white',
                                activebackground=rgb((123, 13, 5)))

    exit_button.pack()
    exit_button.place(w=85, h=25, x=28, y=53)

    # endregion

    window.mainloop()
