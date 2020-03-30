import time
import tkinter as tk

import keyboard
import pyautogui
from PIL import Image, ImageTk
from PIL import ImageGrab
import json
import windowTitles
import pygetwindow

from Functions.getStages import *
from Functions.getTarget import *
from Functions.getLoot import *
from Functions.getMapPosition import *
from Functions.getPlayerPosition import *
from Functions.getPositions import *
from Functions.getSQM import *
from CaveBot.caveBot import *
from CaveBot.autoAttack import *

from Modules.AutoHeal import AutoHeal
from Modules.AutoMana import AutoMana
from Modules.AutoLogin import AutoLogin
from Modules.AutoHur import AutoHur
from Modules.AutoSSA import AutoSSA
from Modules.AutoRing import AutoRing
from Modules.ColorChange import ColorChange
from Modules.AdjustConfig import AdjustConfig
from Modules.AutoAttack import AutoAttack
from Modules.AutoLooter import AutoLooter

from Engine.Defaults import *

rgb = Defaults()

print('\033[33m' + "Start in 1 Seconds...")
time.sleep(1)

set_SQMs = SetSQMs()
get_target_position = GetTargetPosition()
get_number_targets = GetTargetPosition()
GetHealthPosition = GetHealthPosition()
get_battle_position = GetBattlePosition()
get_life_stage = GetStage("Life")
get_mana_position = GetManaPosition()
get_mana_stage = GetStage("Mana")
get_map_position = GetMapPosition()
get_player_position = GetPlayerPosition()
take_loot = GetLoot('right')

WAYPOINTS = [
    {
        "mark": "CheckMark.png",
        "status": "stand"
    },
    {
        "mark": "QuestionMark.png",
        "status": "stand"
    },
    {
        "mark": "ExclimationMark.png",
        "status": "stand"
    },
    {
        "mark": "Star.png",
        "status": "stand"
    },
    {
        "mark": "Cross.png",
        "status": "stand"
    }
]

gameWindow = [0, 0, 0, 0]

map_positions = [0, 0, 0, 0]

Player = [0, 0]

SQMs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Target = [0, 0]

HealthLocation = [0, 0]

ManaLocation = [0, 0]

battle_location = [0, 0, 0, 0]

mark = [0, 0]

TibiaName = ""

TibiaChar = ""

horizontal_SQM_size, vertical_SQM_size = 0, 0

get_health_location = False
get_mana_location = False
get_login_location = False
get_player_location = False
get_attack_location = False
get_SQMs_location = False
get_battle_location = False

bool_Cave_Bot = False


class Redirect:
    def __init__(self):
        self.WindowAutoHeal = False
        self.WindowAutoMana = False
        self.WindowAutoLogin = False
        self.WindowAutoHur = False
        self.WindowAutoSSA = False
        self.WindowAutoRing = False
        self.WindowColorChange = False
        self.WindowAdjustConfig = False
        self.WindowAutoAttack = False
        self.WindowAutoLooter = False

    def AutoHeal(self):
        self.WindowAutoHeal = True
        AutoHeal(root, HealthLocation)

    def AutoMana(self):
        self.WindowAutoMana = True
        AutoMana(root, ManaLocation)

    def AutoLogin(self):
        self.WindowAutoLogin = True
        AutoLogin(root)

    def AutoHur(self):
        self.WindowAutoHur = True
        AutoHur(root)

    def AutoSSA(self):
        self.WindowAutoSSA = True
        AutoSSA(root)

    def AutoRing(self):
        self.WindowAutoRing = True
        AutoRing(root)

    def ColorChange(self):
        self.WindowColorChange = True
        ColorChange(root, Player)

    def AdjustConfig(self):
        self.WindowAdjustConfig = True
        AdjustConfig(root)

    def AutoAttack(self):
        self.WindowAutoAttack = True
        AutoAttack(root, Target, SQMs)

    def AutoLooter(self):
        self.WindowAutoLooter = True
        AutoLooter(root, Player, SQMs)


def root():
    global root
    root = tk.Tk()
    w = 407
    h = 652
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    root.title('TibiaAuto V12')
    root.wm_iconbitmap('images/icone2.ico')
    root.configure(background='#000')
    image = Image.open('images/FundoTibiaAuto.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def exit_button():
        exit(0)

    global TibiaChar
    status_game_label = tk.Label(root, text=f'Logged as: {TibiaChar}', font=('Microsoft Sans Serif', 10),
                                 bg=rgb.rgb((127, 17, 8)), fg='white')
    status_game_label.place(x=20, y=15)

    open_spell_caster = tk.Button(root, text='Auto Hur', font=('Microsoft Sans Serif', 10),
                                  bg=rgb.rgb((127, 17, 8)), fg='white', command=Redirect().AutoHur,
                                  activebackground=rgb.rgb((123, 13, 5)))
    open_spell_caster.place(w=105, h=27, x=275, y=70)

    button_exit = tk.Button(root, text='Exit', font=('Microsoft Sans Serif', 10),
                            bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=rgb.rgb((123, 13, 5)))
    button_exit.place(w=108, h=29, x=11, y=615)

    open_auto_attack = tk.Button(root, text='Auto Attack', font=('Microsoft Sans Serif', 10),
                                 bg=rgb.rgb((127, 17, 8)), fg='white', command=Redirect().AutoAttack,
                                 activebackground=rgb.rgb((123, 13, 5)))
    open_auto_attack.place(w=105, h=27, x=275, y=359)

    open_auto_fish = tk.Button(root, text='Auto Fish', font=('Microsoft Sans Serif', 10),
                               bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                               activebackground=rgb.rgb((123, 13, 5)))
    open_auto_fish.place(w=105, h=27, x=275, y=102)

    open_auto_life = tk.Button(root, text='Auto Life', font=('Microsoft Sans Serif', 10),
                               bg=rgb.rgb((127, 17, 8)), fg='white', command=Redirect().AutoHeal,
                               activebackground=rgb.rgb((123, 13, 5)))
    open_auto_life.place(w=105, h=27, x=165, y=70)

    open_auto_mana = tk.Button(root, text='Auto Mana', font=('Microsoft Sans Serif', 10),
                               bg=rgb.rgb((127, 17, 8)), fg='white', command=Redirect().AutoMana,
                               activebackground=rgb.rgb((123, 13, 5)))
    open_auto_mana.place(w=105, h=27, x=165, y=102)

    open_cave_bot = tk.Button(root, text='Cave Bot', font=('Microsoft Sans Serif', 10),
                              bg=rgb.rgb((127, 17, 8)), fg='white', command=cave_bot,
                              activebackground=rgb.rgb((123, 13, 5)))
    open_cave_bot.place(w=105, h=27, x=165, y=359)

    open_timed_spells = tk.Button(root, text='Timed Spells', font=('Microsoft Sans Serif', 10),
                                  bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                  activebackground=rgb.rgb((123, 13, 5)))
    open_timed_spells.place(w=105, h=27, x=165, y=166)

    open_auto_login = tk.Button(root, text='Auto Login', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=Redirect().AutoLogin,
                                activebackground=rgb.rgb((123, 13, 5)))
    open_auto_login.place(w=105, h=27, x=275, y=166)

    open_color_change = tk.Button(root, text='Color Change', font=('Microsoft Sans Serif', 10),
                                  bg=rgb.rgb((127, 17, 8)), fg='white', command=Redirect().ColorChange,
                                  activebackground=rgb.rgb((123, 13, 5)))
    open_color_change.place(w=105, h=27, x=23, y=134)

    open_ammo_restack = tk.Button(root, text='Ammo Restack', font=('Microsoft Sans Serif', 10),
                                  bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                  activebackground=rgb.rgb((123, 13, 5)))
    open_ammo_restack.place(w=105, h=27, x=23, y=166)

    open_auto_looter = tk.Button(root, text='Auto Looter', font=('Microsoft Sans Serif', 10),
                                 bg=rgb.rgb((127, 17, 8)), fg='white', command=Redirect().AutoLooter,
                                 activebackground=rgb.rgb((123, 13, 5)))
    open_auto_looter.place(w=105, h=27, x=23, y=198)

    open_auto_uh = tk.Button(root, text='Healer Friend', font=('Microsoft Sans Serif', 10),
                             bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                             activebackground=rgb.rgb((123, 13, 5)))
    open_auto_uh.place(w=105, h=27, x=23, y=70)

    open_food_eater = tk.Button(root, text='Food Eater', font=('Microsoft Sans Serif', 10),
                                bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=rgb.rgb((123, 13, 5)))
    open_food_eater.place(w=105, h=27, x=23, y=260)

    open_auto_grouping = tk.Button(root, text='Auto Grouping', font=('Microsoft Sans Serif', 10),
                                   bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                   activebackground=rgb.rgb((123, 13, 5)))
    open_auto_grouping.place(w=105, h=27, x=23, y=292)

    open_sort_loot = tk.Button(root, text='Sort loot', font=('Microsoft Sans Serif', 10),
                               bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                               activebackground=rgb.rgb((123, 13, 5)))
    open_sort_loot.place(w=105, h=27, x=23, y=324)

    open_auto_banker = tk.Button(root, text='Auto Banker', font=('Microsoft Sans Serif', 10),
                                 bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                 activebackground=rgb.rgb((123, 13, 5)))
    open_auto_banker.place(w=105, h=27, x=23, y=356)

    open_auto_seller = tk.Button(root, text='Auto Seller', font=('Microsoft Sans Serif', 10),
                                 bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                 activebackground=rgb.rgb((123, 13, 5)))
    open_auto_seller.place(w=105, h=27, x=23, y=388)

    open_fps_changer = tk.Button(root, text='FPS changer', font=('Microsoft Sans Serif', 10),
                                 bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                 activebackground=rgb.rgb((123, 13, 5)))
    open_fps_changer.place(w=105, h=27, x=23, y=420)

    open_monsters = tk.Button(root, text='Monsters', font=('Microsoft Sans Serif', 10),
                              bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                              activebackground=rgb.rgb((123, 13, 5)))
    open_monsters.place(w=105, h=27, x=275, y=232)

    open_creature_info = tk.Button(root, text='Creature Info', font=('Microsoft Sans Serif', 10),
                                   bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                   activebackground=rgb.rgb((123, 13, 5)))
    open_creature_info.place(w=105, h=27, x=165, y=232)

    open_auto_ssa = tk.Button(root, text='Auto SSA', font=('Microsoft Sans Serif', 10),
                              bg=rgb.rgb((127, 17, 8)), fg='white', command=Redirect().AutoSSA,
                              activebackground=rgb.rgb((123, 13, 5)))
    open_auto_ssa.place(w=105, h=27, x=165, y=134)

    open_auto_ring = tk.Button(root, text='Auto Ring', font=('Microsoft Sans Serif', 10),
                               bg=rgb.rgb((127, 17, 8)), fg='white', command=Redirect().AutoRing,
                               activebackground=rgb.rgb((123, 13, 5)))
    open_auto_ring.place(w=105, h=27, x=275, y=134)

    open_load_config = tk.Button(root, text='Load Config', font=('Microsoft Sans Serif', 10),
                                 bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                 activebackground=rgb.rgb((123, 13, 5)))
    open_load_config.place(w=105, h=27, x=165, y=420)

    open_item_config = tk.Button(root, text='Adjust Config', font=('Microsoft Sans Serif', 10),
                                 bg=rgb.rgb((127, 17, 8)), fg='white', command=Redirect().AdjustConfig,
                                 activebackground=rgb.rgb((123, 13, 5)))
    open_item_config.place(w=105, h=27, x=165, y=452)

    open_save_config = tk.Button(root, text='Save Config', font=('Microsoft Sans Serif', 10),
                                 bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                 activebackground=rgb.rgb((123, 13, 5)))
    open_save_config.place(w=105, h=27, x=275, y=420)

    open_modules = tk.Button(root, text='Modules', font=('Microsoft Sans Serif', 10),
                             bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                             activebackground=rgb.rgb((123, 13, 5)))
    open_modules.place(w=105, h=27, x=275, y=452)

    open_python_scripts = tk.Button(root, text='Python Scripts', font=('Microsoft Sans Serif', 10),
                                    bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                    activebackground=rgb.rgb((123, 13, 5)))
    open_python_scripts.place(w=105, h=27, x=275, y=484)

    open_general_options = tk.Button(root, text='General Options And Statics',
                                     font=('Microsoft Sans Serif', 10),
                                     bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                                     activebackground=rgb.rgb((123, 13, 5)))
    open_general_options.place(w=245, h=29, x=153, y=526)

    root.mainloop()


def cave_bot():
    screen_cave_bot = tk.Toplevel(root)
    screen_cave_bot.focus_force()
    screen_cave_bot.grab_set()
    w = 348
    h = 546
    sw = screen_cave_bot.winfo_screenwidth()
    sh = screen_cave_bot.winfo_screenheight()
    x = (sw - w) / 1.325
    y = (sh - h) / 2.36
    screen_cave_bot.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen_cave_bot.resizable(width=False, height=False)
    screen_cave_bot.title('Module: Cave Bot')
    screen_cave_bot.configure(background='#000', takefocus=True)
    image = Image.open('images/FundoHealingEdited.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(screen_cave_bot, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def exit_button():
        screen_cave_bot.destroy()

    def func_cave_bot():
        global bool_Cave_Bot
        if not bool_Cave_Bot:
            bool_Cave_Bot = True
            cave_bot_button.configure(text='Cave Bot: ON')
            print("Cave Bot: ON")
            if bool_Cave_Bot:
                scanning_cave_bot()
            else:
                print("Master Key Non Activated!")
        else:
            bool_Cave_Bot = False
            print("Cave Bot: OFF")
            cave_bot_button.configure(text='Cave Bot: OFF')

    with open('CaveBot/Scripts/ratThais.json', 'r') as rJson:
        data = json.load(rJson)
        print(len(data))
    print(data)

    def scanning_cave_bot():
        if bool_Cave_Bot:
            print("CAVE BOT PRINT...")
            global monster
            for i in range(len(data)):
                CaveBot().cave_bot(data, i, map_positions, battle_location, monster, SQMs)
                time.sleep(1)
                
        if bool_Cave_Bot:
            root.after(1000, scanning_cave_bot)

    # Buttons

    ''' ok button '''

    button_exit = tk.Button(screen_cave_bot, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=rgb.rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=rgb.rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button auto login '''

    global bool_Cave_Bot
    if not bool_Cave_Bot:
        cave_bot_button = tk.Button(screen_cave_bot, text='Cave Bot: OFF',
                                    font=('Microsoft Sans Serif', 10),
                                    bg=rgb.rgb((127, 17, 8)), fg='white', command=func_cave_bot,
                                    activebackground=rgb.rgb((123, 13, 5)))
        cave_bot_button.place(w=328, h=29, x=12, y=469)
    else:
        cave_bot_button = tk.Button(screen_cave_bot, text='Cave Bot: ON',
                                    font=('Microsoft Sans Serif', 10),
                                    bg=rgb.rgb((127, 17, 8)), fg='white', command=func_cave_bot,
                                    activebackground=rgb.rgb((123, 13, 5)))
        cave_bot_button.place(w=328, h=29, x=12, y=469)

    screen_cave_bot.mainloop()


def main():
    config_master = tk.Tk()
    w = 260
    h = 90
    sw = config_master.winfo_screenwidth()
    sh = config_master.winfo_screenheight()
    x = (sw - w) / 2.3
    y = (sh - h) / 2.4
    config_master.geometry('%dx%d+%d+%d' % (w, h, x, y))
    config_master.resizable(width=False, height=False)
    config_master.title('Ready To Configure ?')
    config_master.configure(background=rgb.rgb((120, 98, 51)), takefocus=True)

    CHARACTERS = ["None"]

    try:
        global TibiaName
        TibiaName = windowTitles.find_tibia_title()
        TibiaCharacter = TibiaName.split(' - ')
        if TibiaCharacter:
            CHARACTERS[0] = '[4176] ' + TibiaCharacter[1]
            global TibiaChar
            TibiaChar = TibiaCharacter[1]
    except IndexError:
        print("You need to login before starting bot.")
        config_master.destroy()
        exit(1)

    char = tk.StringVar(config_master)
    char.set(CHARACTERS[0])

    def exiting():
        exit(1)

    def set_title():
        start_configuration = time.time()
        if TibiaName is not None:
            TibiaWindow = pygetwindow.getWindowsWithTitle(TibiaName)[0]
            TibiaAuto = pygetwindow.getWindowsWithTitle("Ready To Configure ?")[0]
            TibiaAuto.minimize()
            TibiaWindow.maximize()

            time.sleep(2)

            pyautogui.PAUSE = 0.005

            global get_attack_location
            battle_location[0], battle_location[2], battle_location[1], battle_location[
                3] = get_battle_position.get_battle_xy()
            print(f"Your Battle Box location X: {battle_location[0]} Y: {battle_location[1]}")
            get_attack_location = True

            Player[0], Player[1], gameWindow[0], gameWindow[1], gameWindow[2], gameWindow[
                3] = get_player_position.get_gw_xy()
            print(f"Left Game Window Localized In [ X: {gameWindow[0]}, Y: {gameWindow[1]} ]")
            print(f"Right Game Window Localized In [ X: {gameWindow[2]}, Y: {gameWindow[1]}]")
            print(f"Left Button Game Window Localized In [ X: {gameWindow[0]}, Y: {gameWindow[3]}]")
            print(f"Right Button Game Window Localized In [ X: {gameWindow[2]}, Y: {gameWindow[3]}]")
            print("X Player Position Is: ", Player[0])
            print("Y Player Position Is: ", Player[1])
            print("Game Window Start X:", gameWindow[0], " Start Y:", gameWindow[1])
            print("Game Window End X:", gameWindow[2], " End Y", gameWindow[3])

            global get_SQMs_location
            SQMs[0], SQMs[1], SQMs[2], SQMs[3], SQMs[4], SQMs[5], SQMs[6], SQMs[7], SQMs[8], SQMs[9], SQMs[10], SQMs[
                11], SQMs[12], SQMs[13], SQMs[14], SQMs[15], SQMs[16], SQMs[17] = set_SQMs.set_SQMs()
            time.sleep(0.1)
            print("1° SQM Is In: ", SQMs[0], SQMs[1])
            print("2° SQM Is In: ", SQMs[2], SQMs[3])
            print("3° SQM Is In: ", SQMs[4], SQMs[5])
            print("4° SQM Is In: ", SQMs[6], SQMs[7])
            print("5° SQM Is In: ", SQMs[8], SQMs[9])
            print("6° SQM Is In: ", SQMs[10], SQMs[11])
            print("7° SQM Is In: ", SQMs[12], SQMs[13])
            print("8° SQM Is In: ", SQMs[14], SQMs[15])
            print("9° SQM Is In: ", SQMs[16], SQMs[17])
            time.sleep(0.1)
            get_SQMs_location = True

            global get_health_location
            HealthLocation[0], HealthLocation[1] = GetHealthPosition.get_health_xy()
            HealthLocation[0], HealthLocation[1] = int(HealthLocation[0]), int(HealthLocation[1])
            print(f"Your Health Box location X: {HealthLocation[0]} Y: {HealthLocation[1]}")
            get_health_location = True

            global get_mana_location
            ManaLocation[0], ManaLocation[1] = get_mana_position.get_mana_xy()
            ManaLocation[0], ManaLocation[1] = int(ManaLocation[0]), int(ManaLocation[1])
            print(f"Your Mana Box location X: {ManaLocation[0]} Y: {ManaLocation[1]}")
            get_mana_location = True

            global map_positions
            map_positions[0], map_positions[1], map_positions[2], map_positions[3] = get_map_position.get_map_xy()

            end_configuration = time.time() - start_configuration
            print(f"Your Setup Time Is: {end_configuration:.2f} Seconds")

            print("Opening TibiaAuto...")

            time.sleep(0.3)
            config_master.destroy()
            time.sleep(1)
            root()
        else:
            print("Error to Log Tibia window")

    select_character = tk.OptionMenu(config_master, char, *CHARACTERS)
    select_character.configure(anchor='w')
    select_character.pack()
    select_character.place(w=230, h=24, x=15, y=17)

    config_button = tk.Button(config_master, width=15, text="Configurar", command=set_title, bg=rgb.rgb((127, 17, 8)),
                              fg='white',
                              activebackground=rgb.rgb((123, 13, 5)))
    config_button.pack()
    config_button.place(w=85, h=25, x=140, y=53)

    exit_button = tk.Button(config_master, width=15, text="Exit", command=exiting, bg=rgb.rgb((127, 17, 8)),
                            fg='white',
                            activebackground=rgb.rgb((123, 13, 5)))
    exit_button.pack()
    exit_button.place(w=85, h=25, x=28, y=53)

    config_master.mainloop()


if __name__ == '__main__':
    main()
