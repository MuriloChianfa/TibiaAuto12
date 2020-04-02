import threading
import pygetwindow

from Conf.WindowTitles import *
from Conf.SetSQMsPositions import SetSQMs

from Core.GetPlayerPosition import GetPlayerPosition
from Core.GetManaPosition import GetManaPosition
from Core.GetHealthPosition import GetHealthPosition
from Core.GetMapPosition import GetMapPosition
from Core.GetBattlePosition import GetBattlePosition
from Core.GetStatsPosition import GetStatsPosition

from Engine.Defaults import *
from Engine.GUI import *
from Engine.EngineCaveBot import *
from Engine.AttackTarget import *

from Modules.AdjustConfig import AdjustConfig
from Modules.AmmoRestack import AmmoRestack
from Modules.AutoAttack import AutoAttack
from Modules.AutoBanker import AutoBanker
from Modules.AutoFish import AutoFish
from Modules.AutoGrouping import AutoGrouping
from Modules.AutoHeal import AutoHeal
from Modules.AutoHur import AutoHur
from Modules.AutoLogin import AutoLogin
from Modules.AutoLooter import AutoLooter
from Modules.AutoMana import AutoMana
from Modules.AutoRing import AutoRing
from Modules.AutoSeller import AutoSeller
from Modules.AutoSSA import AutoSSA
from Modules.CaveBot import CaveBot
from Modules.ColorChange import ColorChange
from Modules.CreatureInfo import CreatureInfo
from Modules.FoodEater import FoodEater
from Modules.FPSChanger import FPSChanger
from Modules.GeneralOptions import GeneralOptions
from Modules.HealerFriend import HealerFriend
from Modules.LoadConfig import LoadConfig
from Modules.Modules import Modules
from Modules.Monsters import Monsters
from Modules.PythonScripts import PythonScripts
from Modules.SaveConfig import SaveConfig
from Modules.SortLoot import SortLoot
from Modules.TimedSpells import TimedSpells

print('\033[33m' + "Start in 1 Seconds...")
time.sleep(1)

mark = [0, 0]
Player = [0, 0]
Target = [0, 0]
gameWindow = [0, 0, 0, 0]
ManaLocation = [0, 0]
MapPositions = [0, 0, 0, 0]
StatsPositions = [0, 0, 0, 0]
HealthLocation = [0, 0]
BattlePositions = [0, 0, 0, 0]
SQMs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

TibiaName = ""
TibiaChar = ""

get_health_location = False
get_mana_location = False
get_player_location = False
get_attack_location = False
get_SQMs_location = False

bool_Cave_Bot = False


class Redirect:
    def __init__(self):
        self.Thread = threading

    def OpenAdjustConfig(self):
        AdjustConfig(root)

    def OpenAmmoRestack(self):
        AmmoRestack(root)

    def OpenAutoAttack(self):
        AutoAttack(root, SQMs, BattlePositions)

    def OpenAutoBanker(self):
        AutoBanker(root)

    def OpenAutoFish(self):
        AutoFish(root)

    def OpenAutoGrouping(self):
        AutoGrouping(root)

    def OpenAutoHeal(self):
        AutoHeal(root, HealthLocation)

    def OpenAutoHur(self):
        AutoHur(root, StatsPositions)

    def OpenAutoLogin(self):
        AutoLogin(root)

    def OpenAutoLooter(self):
        AutoLooter(root, Player, SQMs)

    def OpenAutoMana(self):
        AutoMana(root, ManaLocation)

    def OpenAutoRing(self):
        AutoRing(root)

    def OpenAutoSeller(self):
        AutoSeller(root)

    def OpenAutoSSA(self):
        AutoSSA(root)

    def OpenCaveBot(self):
        CaveBot(root, MapPositions, BattlePositions, SQMs)

    def OpenColorChange(self):
        ColorChange(root, Player)

    def OpenCreatureInfo(self):
        CreatureInfo(root)

    def OpenFoodEater(self):
        FoodEater(root)

    def OpenFPSChanger(self):
        FPSChanger(root)

    def OpenGeneralOptions(self):
        GeneralOptions(root)

    def OpenHealerFriend(self):
        HealerFriend(root)

    def OpenLoadConfig(self):
        LoadConfig(root)

    def OpenModules(self):
        Modules(root)

    def OpenMonsters(self):
        Monsters(root)

    def OpenPythonScripts(self):
        PythonScripts(root)

    def OpenSaveConfig(self):
        SaveConfig(root)

    def OpenSortLoot(self):
        SortLoot(root)

    def OpenTimedSpells(self):
        TimedSpells(root)


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
                                 bg=rgb((127, 17, 8)), fg='white')
    status_game_label.place(x=20, y=15)

    open_spell_caster = tk.Button(root, text='Auto Hur', font=('Microsoft Sans Serif', 10),
                                  bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoHur,
                                  activebackground=rgb((123, 13, 5)))
    open_spell_caster.place(w=105, h=27, x=275, y=70)

    button_exit = tk.Button(root, text='Exit', font=('Microsoft Sans Serif', 10),
                            bg=rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=rgb((123, 13, 5)))
    button_exit.place(w=108, h=29, x=11, y=615)

    open_auto_attack = tk.Button(root, text='Auto Attack', font=('Microsoft Sans Serif', 10),
                                 bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoAttack,
                                 activebackground=rgb((123, 13, 5)))
    open_auto_attack.place(w=105, h=27, x=275, y=359)

    open_auto_fish = tk.Button(root, text='Auto Fish', font=('Microsoft Sans Serif', 10),
                               bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoFish,
                               activebackground=rgb((123, 13, 5)))
    open_auto_fish.place(w=105, h=27, x=275, y=102)

    open_auto_life = tk.Button(root, text='Auto Life', font=('Microsoft Sans Serif', 10),
                               bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoHeal,
                               activebackground=rgb((123, 13, 5)))
    open_auto_life.place(w=105, h=27, x=165, y=70)

    open_auto_mana = tk.Button(root, text='Auto Mana', font=('Microsoft Sans Serif', 10),
                               bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoMana,
                               activebackground=rgb((123, 13, 5)))
    open_auto_mana.place(w=105, h=27, x=165, y=102)

    open_cave_bot = tk.Button(root, text='Cave Bot', font=('Microsoft Sans Serif', 10),
                              bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenCaveBot,
                              activebackground=rgb((123, 13, 5)))
    open_cave_bot.place(w=105, h=27, x=165, y=359)

    open_timed_spells = tk.Button(root, text='Timed Spells', font=('Microsoft Sans Serif', 10),
                                  bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenTimedSpells,
                                  activebackground=rgb((123, 13, 5)))
    open_timed_spells.place(w=105, h=27, x=165, y=166)

    open_auto_login = tk.Button(root, text='Auto Login', font=('Microsoft Sans Serif', 10),
                                bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoLogin,
                                activebackground=rgb((123, 13, 5)))
    open_auto_login.place(w=105, h=27, x=275, y=166)

    open_color_change = tk.Button(root, text='Color Change', font=('Microsoft Sans Serif', 10),
                                  bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenColorChange,
                                  activebackground=rgb((123, 13, 5)))
    open_color_change.place(w=105, h=27, x=23, y=134)

    open_ammo_restack = tk.Button(root, text='Ammo Restack', font=('Microsoft Sans Serif', 10),
                                  bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAmmoRestack,
                                  activebackground=rgb((123, 13, 5)))
    open_ammo_restack.place(w=105, h=27, x=23, y=166)

    open_auto_looter = tk.Button(root, text='Auto Looter', font=('Microsoft Sans Serif', 10),
                                 bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoLooter,
                                 activebackground=rgb((123, 13, 5)))
    open_auto_looter.place(w=105, h=27, x=23, y=198)

    open_auto_uh = tk.Button(root, text='Healer Friend', font=('Microsoft Sans Serif', 10),
                             bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenHealerFriend,
                             activebackground=rgb((123, 13, 5)))
    open_auto_uh.place(w=105, h=27, x=23, y=70)

    open_food_eater = tk.Button(root, text='Food Eater', font=('Microsoft Sans Serif', 10),
                                bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenFoodEater,
                                activebackground=rgb((123, 13, 5)))
    open_food_eater.place(w=105, h=27, x=23, y=260)

    open_auto_grouping = tk.Button(root, text='Auto Grouping', font=('Microsoft Sans Serif', 10),
                                   bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoGrouping,
                                   activebackground=rgb((123, 13, 5)))
    open_auto_grouping.place(w=105, h=27, x=23, y=292)

    open_sort_loot = tk.Button(root, text='Sort loot', font=('Microsoft Sans Serif', 10),
                               bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenSortLoot,
                               activebackground=rgb((123, 13, 5)))
    open_sort_loot.place(w=105, h=27, x=23, y=324)

    open_auto_banker = tk.Button(root, text='Auto Banker', font=('Microsoft Sans Serif', 10),
                                 bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoBanker,
                                 activebackground=rgb((123, 13, 5)))
    open_auto_banker.place(w=105, h=27, x=23, y=356)

    open_auto_seller = tk.Button(root, text='Auto Seller', font=('Microsoft Sans Serif', 10),
                                 bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoSeller,
                                 activebackground=rgb((123, 13, 5)))
    open_auto_seller.place(w=105, h=27, x=23, y=388)

    open_fps_changer = tk.Button(root, text='FPS changer', font=('Microsoft Sans Serif', 10),
                                 bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenFPSChanger,
                                 activebackground=rgb((123, 13, 5)))
    open_fps_changer.place(w=105, h=27, x=23, y=420)

    open_monsters = tk.Button(root, text='Monsters', font=('Microsoft Sans Serif', 10),
                              bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenMonsters,
                              activebackground=rgb((123, 13, 5)))
    open_monsters.place(w=105, h=27, x=275, y=232)

    open_creature_info = tk.Button(root, text='Creature Info', font=('Microsoft Sans Serif', 10),
                                   bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenCreatureInfo,
                                   activebackground=rgb((123, 13, 5)))
    open_creature_info.place(w=105, h=27, x=165, y=232)

    open_auto_ssa = tk.Button(root, text='Auto SSA', font=('Microsoft Sans Serif', 10),
                              bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoSSA,
                              activebackground=rgb((123, 13, 5)))
    open_auto_ssa.place(w=105, h=27, x=165, y=134)

    open_auto_ring = tk.Button(root, text='Auto Ring', font=('Microsoft Sans Serif', 10),
                               bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAutoRing,
                               activebackground=rgb((123, 13, 5)))
    open_auto_ring.place(w=105, h=27, x=275, y=134)

    open_load_config = tk.Button(root, text='Load Config', font=('Microsoft Sans Serif', 10),
                                 bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenLoadConfig,
                                 activebackground=rgb((123, 13, 5)))
    open_load_config.place(w=105, h=27, x=165, y=420)

    open_item_config = tk.Button(root, text='Adjust Config', font=('Microsoft Sans Serif', 10),
                                 bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenAdjustConfig,
                                 activebackground=rgb((123, 13, 5)))
    open_item_config.place(w=105, h=27, x=165, y=452)

    open_save_config = tk.Button(root, text='Save Config', font=('Microsoft Sans Serif', 10),
                                 bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenSaveConfig,
                                 activebackground=rgb((123, 13, 5)))
    open_save_config.place(w=105, h=27, x=275, y=420)

    open_modules = tk.Button(root, text='Modules', font=('Microsoft Sans Serif', 10),
                             bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenModules,
                             activebackground=rgb((123, 13, 5)))
    open_modules.place(w=105, h=27, x=275, y=452)

    open_python_scripts = tk.Button(root, text='Python Scripts', font=('Microsoft Sans Serif', 10),
                                    bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenPythonScripts,
                                    activebackground=rgb((123, 13, 5)))
    open_python_scripts.place(w=105, h=27, x=275, y=484)

    open_general_options = tk.Button(root, text='General Options And Statics',
                                     font=('Microsoft Sans Serif', 10),
                                     bg=rgb((127, 17, 8)), fg='white', command=Redirect().OpenGeneralOptions,
                                     activebackground=rgb((123, 13, 5)))
    open_general_options.place(w=245, h=29, x=153, y=526)

    root.mainloop()


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
    config_master.configure(background=rgb((120, 98, 51)), takefocus=True)

    CHARACTERS = ["None"]

    try:
        global TibiaName
        TibiaName = FindTibiaTitle()
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
            BattlePositions[0], BattlePositions[1], BattlePositions[2], BattlePositions[3] = GetBattlePosition()
            print(f"Your Battle Box location X: {BattlePositions[0]} Y: {BattlePositions[1]}")
            get_attack_location = True

            StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3] = GetStatsPosition()
            print("Your Status Bar Is In: ", StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3])

            Player[0], Player[1], gameWindow[0], gameWindow[1], gameWindow[2], gameWindow[
                3] = GetPlayerPosition()
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
                11], SQMs[12], SQMs[13], SQMs[14], SQMs[15], SQMs[16], SQMs[17] = SetSQMs()
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
            HealthLocation[0], HealthLocation[1] = GetHealthPosition()
            HealthLocation[0], HealthLocation[1] = int(HealthLocation[0]), int(HealthLocation[1])
            print(f"Your Health Box location X: {HealthLocation[0]} Y: {HealthLocation[1]}")
            get_health_location = True

            global get_mana_location
            ManaLocation[0], ManaLocation[1] = GetManaPosition()
            ManaLocation[0], ManaLocation[1] = int(ManaLocation[0]), int(ManaLocation[1])
            print(f"Your Mana Box location X: {ManaLocation[0]} Y: {ManaLocation[1]}")
            get_mana_location = True

            global MapPositions
            MapPositions[0], MapPositions[1], MapPositions[2], MapPositions[3] = GetMapPosition()

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

    config_button = tk.Button(config_master, width=15, text="Configurar", command=set_title, bg=rgb((127, 17, 8)),
                              fg='white',
                              activebackground=rgb((123, 13, 5)))
    config_button.pack()
    config_button.place(w=85, h=25, x=140, y=53)

    exit_button = tk.Button(config_master, width=15, text="Exit", command=exiting, bg=rgb((127, 17, 8)),
                            fg='white',
                            activebackground=rgb((123, 13, 5)))
    exit_button.pack()
    exit_button.place(w=85, h=25, x=28, y=53)

    config_master.mainloop()


if __name__ == '__main__':
    main()
