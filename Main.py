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


#region Arrays

lifeColorFull = [194, 74, 74]

lifeColor = [219, 79, 79]

manaColorFull = [45, 45, 105]

manaColor = [83, 80, 218]

gameWindow = [0, 0, 0, 0]

map_positions = [0, 0, 0, 0]

Player = [0, 0]

SQMs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Target = [0, 0]

HealthLocation = [0, 0]

ManaLocation = [0, 0]

battle_location = [0, 0, 0, 0]

hotkeys = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]

percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]

mark = [0, 0]

monsters = [
    "Rat",
    "CaveRat",
    "Orc",
    "OrcWarrior",
    "OrcSpearman",
    "Cyclops",
    "Rotworm",
    "AnyCorym",
    "CorymCharlatan",
    "CorymSkirmisher",
    "CorymVanguard",
    "Stonerefiner"
]

priority = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#endregion


# region GlobalVariables

TibiaName = ""

target_number = 0
target_number2 = 0

username_field_X = 0
username_field_Y = 0

horizontal_SQM_size, vertical_SQM_size = 0, 0

get_health_location = False
get_mana_location = False
get_login_location = False
get_player_location = False
get_attack_location = False
get_SQMs_location = False
get_battle_location = False

bool_auto_looter = False
bool_adjust_config = False
bool_life = False
bool_hur = False
bool_mana = False
bool_login = False
bool_auto_attack = False
bool_auto_ssa = False
bool_auto_ring = False
bool_color_change = False
bool_Cave_Bot = False

monster = "Rat"

master_key_start = False

master_start = False

# endregion


def _from_rgb(rgb):  # Function to translate color to RGB
    return "#%02x%02x%02x" % rgb


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func


def capture_screen():
    global screen
    screen = ImageGrab.grab()
    return screen


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

    def func_config_masterkey():
        global master_start
        if not master_start:
            master_start = True
            enable_master_key.configure(text='Disable Master Key "J"')
        else:
            master_start = False
            enable_master_key.configure(text='Enable Master Key "J"')

    def init_key_check():
        if keyboard.is_pressed('j'):
            global master_key_start
            if master_key_start == False and master_start == True:
                master_key_start = True
                status_game_label.configure(text='Status Game: ON')
            elif master_key_start == True and master_start == False:
                master_key_start = True
                status_game_label.configure(text='Status Game: ON')
            else:
                master_key_start = False
                status_game_label.configure(text='Status Game: OFF')

        root.after(75, init_key_check)

    enable_master_key = tk.Button(root, text='Enable Master Key "J"',
                                  font=('Microsoft Sans Serif', 10),
                                  bg=_from_rgb((127, 17, 8)), fg='white',
                                  command=combine_funcs(init_key_check, func_config_masterkey),
                                  activebackground=_from_rgb((123, 13, 5)))
    enable_master_key.place(w=150, h=24, x=190, y=13)

    status_game_label = tk.Label(root, text='Status Game: OFF', font=('Microsoft Sans Serif', 10),
                                 bg=_from_rgb((127, 17, 8)), fg='white')
    status_game_label.place(x=20, y=15)

    open_spell_caster = tk.Button(root, text='Auto Hur', font=('Microsoft Sans Serif', 10),
                                  bg=_from_rgb((127, 17, 8)), fg='white', command=auto_hur,
                                  activebackground=_from_rgb((123, 13, 5)))
    open_spell_caster.place(w=105, h=27, x=275, y=70)

    button_exit = tk.Button(root, text='Exit', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=108, h=29, x=11, y=615)

    open_auto_attack = tk.Button(root, text='Auto Attack', font=('Microsoft Sans Serif', 10),
                                 bg=_from_rgb((127, 17, 8)), fg='white', command=auto_attack,
                                 activebackground=_from_rgb((123, 13, 5)))
    open_auto_attack.place(w=105, h=27, x=275, y=359)

    open_auto_fish = tk.Button(root, text='Auto Fish', font=('Microsoft Sans Serif', 10),
                               bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                               activebackground=_from_rgb((123, 13, 5)))
    open_auto_fish.place(w=105, h=27, x=275, y=102)

    open_auto_life = tk.Button(root, text='Auto Life', font=('Microsoft Sans Serif', 10),
                               bg=_from_rgb((127, 17, 8)), fg='white', command=auto_life,
                               activebackground=_from_rgb((123, 13, 5)))
    open_auto_life.place(w=105, h=27, x=165, y=70)

    open_auto_mana = tk.Button(root, text='Auto Mana', font=('Microsoft Sans Serif', 10),
                               bg=_from_rgb((127, 17, 8)), fg='white', command=auto_mana,
                               activebackground=_from_rgb((123, 13, 5)))
    open_auto_mana.place(w=105, h=27, x=165, y=102)

    open_cave_bot = tk.Button(root, text='Cave Bot', font=('Microsoft Sans Serif', 10),
                              bg=_from_rgb((127, 17, 8)), fg='white', command=cave_bot,
                              activebackground=_from_rgb((123, 13, 5)))
    open_cave_bot.place(w=105, h=27, x=165, y=359)

    open_timed_spells = tk.Button(root, text='Timed Spells', font=('Microsoft Sans Serif', 10),
                                  bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                  activebackground=_from_rgb((123, 13, 5)))
    open_timed_spells.place(w=105, h=27, x=165, y=166)

    open_auto_login = tk.Button(root, text='Auto Login', font=('Microsoft Sans Serif', 10),
                                bg=_from_rgb((127, 17, 8)), fg='white', command=auto_login,
                                activebackground=_from_rgb((123, 13, 5)))
    open_auto_login.place(w=105, h=27, x=275, y=166)

    open_color_change = tk.Button(root, text='Color Change', font=('Microsoft Sans Serif', 10),
                                  bg=_from_rgb((127, 17, 8)), fg='white', command=color_change,
                                  activebackground=_from_rgb((123, 13, 5)))
    open_color_change.place(w=105, h=27, x=23, y=134)

    open_ammo_restack = tk.Button(root, text='Ammo Restack', font=('Microsoft Sans Serif', 10),
                                  bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                  activebackground=_from_rgb((123, 13, 5)))
    open_ammo_restack.place(w=105, h=27, x=23, y=166)

    open_auto_looter = tk.Button(root, text='Auto Looter', font=('Microsoft Sans Serif', 10),
                                 bg=_from_rgb((127, 17, 8)), fg='white', command=auto_looter,
                                 activebackground=_from_rgb((123, 13, 5)))
    open_auto_looter.place(w=105, h=27, x=23, y=198)

    open_auto_uh = tk.Button(root, text='Healer Friend', font=('Microsoft Sans Serif', 10),
                             bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                             activebackground=_from_rgb((123, 13, 5)))
    open_auto_uh.place(w=105, h=27, x=23, y=70)

    open_food_eater = tk.Button(root, text='Food Eater', font=('Microsoft Sans Serif', 10),
                                bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                activebackground=_from_rgb((123, 13, 5)))
    open_food_eater.place(w=105, h=27, x=23, y=260)

    open_auto_grouping = tk.Button(root, text='Auto Grouping', font=('Microsoft Sans Serif', 10),
                                   bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                   activebackground=_from_rgb((123, 13, 5)))
    open_auto_grouping.place(w=105, h=27, x=23, y=292)

    open_sort_loot = tk.Button(root, text='Sort loot', font=('Microsoft Sans Serif', 10),
                               bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                               activebackground=_from_rgb((123, 13, 5)))
    open_sort_loot.place(w=105, h=27, x=23, y=324)

    open_auto_banker = tk.Button(root, text='Auto Banker', font=('Microsoft Sans Serif', 10),
                                 bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                 activebackground=_from_rgb((123, 13, 5)))
    open_auto_banker.place(w=105, h=27, x=23, y=356)

    open_auto_seller = tk.Button(root, text='Auto Seller', font=('Microsoft Sans Serif', 10),
                                 bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                 activebackground=_from_rgb((123, 13, 5)))
    open_auto_seller.place(w=105, h=27, x=23, y=388)

    open_fps_changer = tk.Button(root, text='FPS changer', font=('Microsoft Sans Serif', 10),
                                 bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                 activebackground=_from_rgb((123, 13, 5)))
    open_fps_changer.place(w=105, h=27, x=23, y=420)

    open_monsters = tk.Button(root, text='Monsters', font=('Microsoft Sans Serif', 10),
                              bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                              activebackground=_from_rgb((123, 13, 5)))
    open_monsters.place(w=105, h=27, x=275, y=232)

    open_creature_info = tk.Button(root, text='Creature Info', font=('Microsoft Sans Serif', 10),
                                   bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                   activebackground=_from_rgb((123, 13, 5)))
    open_creature_info.place(w=105, h=27, x=165, y=232)

    open_auto_ssa = tk.Button(root, text='Auto SSA', font=('Microsoft Sans Serif', 10),
                              bg=_from_rgb((127, 17, 8)), fg='white', command=auto_ssa,
                              activebackground=_from_rgb((123, 13, 5)))
    open_auto_ssa.place(w=105, h=27, x=165, y=134)

    open_auto_ring = tk.Button(root, text='Auto Ring', font=('Microsoft Sans Serif', 10),
                               bg=_from_rgb((127, 17, 8)), fg='white', command=auto_ring,
                               activebackground=_from_rgb((123, 13, 5)))
    open_auto_ring.place(w=105, h=27, x=275, y=134)

    open_load_config = tk.Button(root, text='Load Config', font=('Microsoft Sans Serif', 10),
                                 bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                 activebackground=_from_rgb((123, 13, 5)))
    open_load_config.place(w=105, h=27, x=165, y=420)

    open_item_config = tk.Button(root, text='Adjust Config', font=('Microsoft Sans Serif', 10),
                                 bg=_from_rgb((127, 17, 8)), fg='white', command=adjust_config,
                                 activebackground=_from_rgb((123, 13, 5)))
    open_item_config.place(w=105, h=27, x=165, y=452)

    open_save_config = tk.Button(root, text='Save Config', font=('Microsoft Sans Serif', 10),
                                 bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                 activebackground=_from_rgb((123, 13, 5)))
    open_save_config.place(w=105, h=27, x=275, y=420)

    open_modules = tk.Button(root, text='Modules', font=('Microsoft Sans Serif', 10),
                             bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                             activebackground=_from_rgb((123, 13, 5)))
    open_modules.place(w=105, h=27, x=275, y=452)

    open_python_scripts = tk.Button(root, text='Python Scripts', font=('Microsoft Sans Serif', 10),
                                    bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                    activebackground=_from_rgb((123, 13, 5)))
    open_python_scripts.place(w=105, h=27, x=275, y=484)

    open_general_options = tk.Button(root, text='General Options And Statics',
                                     font=('Microsoft Sans Serif', 10),
                                     bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                                     activebackground=_from_rgb((123, 13, 5)))
    open_general_options.place(w=245, h=29, x=153, y=526)

    root.mainloop()


def auto_life():
    screen_auto_life = tk.Toplevel(root)
    screen_auto_life.focus_force()
    screen_auto_life.grab_set()
    w = 348
    h = 546
    sw = screen_auto_life.winfo_screenwidth()
    sh = screen_auto_life.winfo_screenheight()
    x = (sw - w) / 1.325
    y = (sh - h) / 2.36
    screen_auto_life.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen_auto_life.resizable(width=False, height=False)
    screen_auto_life.title('Module: Auto Life')
    screen_auto_life.configure(background='#000', takefocus=True)
    image = Image.open('images/FundoHealingEdited.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(screen_auto_life, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def exit_button():
        screen_auto_life.destroy()

    def func_auto_life():
        global bool_life
        if not bool_life:
            bool_life = True
            auto_life_button.configure(text='AutoHealing: ON')
            print("AutoHealing: ON")
            global get_health_location
            if not get_health_location:
                HealthLocation[0], HealthLocation[1] = GetHealthPosition.get_health_xy()
                get_health_location = True
                if HealthLocation[0] and HealthLocation[1] != 0:
                    if bool_life and master_key_start:
                        scanning_auto_life()
                    else:
                        print("Master Key Non Activated!")
                else:
                    print("Error on Health Localization!")
            else:
                if bool_life and master_key_start:
                    scanning_auto_life()
                else:
                    print("Master Key Non Activated!")
        else:
            bool_life = False
            print("AutoHealing: OFF")
            auto_life_button.configure(text='AutoHealing: OFF')

    def scanning_auto_life():
        life = get_life_stage.scanning_stage(HealthLocation, lifeColor, lifeColorFull)

        if var_check_five.get() == "on":
            stage_three = var_dropdown_stage_five.get()
            if int(stage_three) > life or int(stage_three) == life:
                pyautogui.press(var_dropdown_stage_six.get())
                print("Pressed ", var_dropdown_stage_six.get())
        elif var_check_four.get() == "on":
            stage_two = var_dropdown_stage_three.get()
            if int(stage_two) > life or int(stage_two) == life:
                pyautogui.press(var_dropdown_stage_four.get())
                print("Pressed ", var_dropdown_stage_four.get())
        elif var_check_three.get() == "on":
            stage_one = var_dropdown_stage_one.get()
            if int(stage_one) > life or int(stage_one) == life:
                pyautogui.press(var_dropdown_stage_two.get())
                print("Pressed ", var_dropdown_stage_two.get())
        else:
            print("Modulo Not Configured")

        if bool_life and master_key_start:
            root.after(200, scanning_auto_life)

    var_check_one = tk.StringVar()
    var_check_two = tk.StringVar()
    var_check_three = tk.StringVar()
    var_check_four = tk.StringVar()
    var_check_five = tk.StringVar()
    var_check_six = tk.StringVar()
    var_check_seven = tk.StringVar()
    var_check_eight = tk.StringVar()
    var_check_nine = tk.StringVar()
    var_check_ten = tk.StringVar()
    var_check_eleven = tk.StringVar()
    var_check_twelve = tk.StringVar()
    var_dropdown_stage_one = tk.StringVar()
    var_dropdown_stage_one.set(90)
    var_dropdown_stage_two = tk.StringVar()
    var_dropdown_stage_two.set("f1")
    var_dropdown_stage_three = tk.StringVar()
    var_dropdown_stage_three.set(75)
    var_dropdown_stage_four = tk.StringVar()
    var_dropdown_stage_four.set("f2")
    var_dropdown_stage_five = tk.StringVar()
    var_dropdown_stage_five.set(35)
    var_dropdown_stage_six = tk.StringVar()
    var_dropdown_stage_six.set("f12")
    img_poison = ImageTk.PhotoImage(Image.open('images/Stats/poison.webp'))
    img_paralyze = ImageTk.PhotoImage(Image.open('images/Stats/paralyze.webp'))
    img_fire = ImageTk.PhotoImage(Image.open('images/Stats/fire.webp'))
    img_electrify = ImageTk.PhotoImage(Image.open('images/Stats/electrify.webp'))
    img_mort = ImageTk.PhotoImage(Image.open('images/Stats/mort.webp'))
    img_blood = ImageTk.PhotoImage(Image.open('images/Stats/blood.webp'))

    button_exit = tk.Button(screen_auto_life, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button enable healing '''

    global bool_life
    if not bool_life:
        auto_life_button = tk.Button(screen_auto_life, text='AutoHealing: OFF', font=('Microsoft Sans Serif', 10),
                                     bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_life,
                                     activebackground=_from_rgb((123, 13, 5)))
        auto_life_button.place(w=328, h=29, x=12, y=469)
    else:
        auto_life_button = tk.Button(screen_auto_life, text='AutoHealing: ON', font=('Microsoft Sans Serif', 10),
                                     bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_life,
                                     activebackground=_from_rgb((123, 13, 5)))
        auto_life_button.place(w=328, h=29, x=12, y=469)

    name_label = tk.Label(screen_auto_life, text='Healing', font=('Microsoft Sans Serif', 10),
                          bg=_from_rgb((120, 98, 51)), fg='white')
    name_label.place(x=32, y=3)

    percentage_label = tk.Label(screen_auto_life, text='% Percentage', font=('Microsoft Sans Serif', 10),
                                bg=_from_rgb((130, 16, 6)), fg='white')
    percentage_label.place(x=153, y=54)

    hotkey_label = tk.Label(screen_auto_life, text='HotKey', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((130, 16, 6)), fg='white')
    hotkey_label.place(x=259, y=54)

    check_one = tk.Checkbutton(screen_auto_life, bg=_from_rgb((120, 98, 51)), height=2, text="Print on Tibia's screen",
                               variable=var_check_one, onvalue="on",
                               activebackground=_from_rgb((120, 98, 51)))
    check_one.place(x=10, y=408)
    check_one.deselect()

    check_two = tk.Checkbutton(screen_auto_life, bg=_from_rgb((120, 98, 51)), text="Don't Buff",
                               variable=var_check_two, onvalue="on", offvalue="off",
                               activebackground=_from_rgb((120, 98, 51)))
    check_two.place(x=10, y=440)
    check_two.deselect()

    check_three = tk.Checkbutton(screen_auto_life, bg=_from_rgb((130, 16, 6)), text="Enable Stage One",
                                 variable=var_check_three, onvalue="on", offvalue="off",
                                 activebackground=_from_rgb((130, 16, 6)))
    check_three.place(x=32, y=94)
    check_three.deselect()

    check_four = tk.Checkbutton(screen_auto_life, bg=_from_rgb((130, 16, 6)), text="Enable Stage Two",
                                variable=var_check_four, onvalue="on", offvalue="off",
                                activebackground=_from_rgb((130, 16, 6)))
    check_four.place(x=32, y=144)
    check_four.deselect()

    check_five = tk.Checkbutton(screen_auto_life, bg=_from_rgb((130, 16, 6)), text="Enable Stage Three",
                                variable=var_check_five, onvalue="on", offvalue="off",
                                activebackground=_from_rgb((130, 16, 6)))
    check_five.place(x=32, y=194)
    check_five.deselect()

    check_six = tk.Checkbutton(screen_auto_life, bg=_from_rgb((130, 16, 6)), text="Enable Cure Statments",
                               variable=var_check_six, onvalue="on", offvalue="off",
                               activebackground=_from_rgb((130, 16, 6)))
    check_six.place(x=105, y=334)
    check_six.deselect()

    check_seven = tk.Checkbutton(screen_auto_life, bg=_from_rgb((130, 16, 6)),
                                 variable=var_check_seven, onvalue="on", offvalue="off",
                                 activebackground=_from_rgb((130, 16, 6)),
                                 image=img_paralyze)
    check_seven.place(x=52, y=364)
    check_seven.deselect()

    check_eight = tk.Checkbutton(screen_auto_life, bg=_from_rgb((130, 16, 6)),
                                 variable=var_check_eight, onvalue="on", offvalue="off",
                                 activebackground=_from_rgb((130, 16, 6)),
                                 image=img_poison)
    check_eight.place(x=92, y=364)
    check_eight.deselect()

    check_nine = tk.Checkbutton(screen_auto_life, bg=_from_rgb((130, 16, 6)),
                                variable=var_check_nine, onvalue="on", offvalue="off",
                                activebackground=_from_rgb((130, 16, 6)),
                                image=img_fire)
    check_nine.place(x=132, y=364)
    check_nine.deselect()

    check_ten = tk.Checkbutton(screen_auto_life, bg=_from_rgb((130, 16, 6)),
                               variable=var_check_ten, onvalue="on", offvalue="off",
                               activebackground=_from_rgb((130, 16, 6)),
                               image=img_electrify)
    check_ten.place(x=172, y=364)
    check_ten.deselect()

    check_eleven = tk.Checkbutton(screen_auto_life, bg=_from_rgb((130, 16, 6)),
                                  variable=var_check_eleven, onvalue="on", offvalue="off",
                                  activebackground=_from_rgb((130, 16, 6)),
                                  image=img_mort)
    check_eleven.place(x=212, y=364)
    check_eleven.deselect()

    check_twelve = tk.Checkbutton(screen_auto_life, bg=_from_rgb((130, 16, 6)),
                                  variable=var_check_twelve, onvalue="on", offvalue="off",
                                  activebackground=_from_rgb((130, 16, 6)),
                                  image=img_blood)
    check_twelve.place(x=252, y=364)
    check_twelve.deselect()

    dropdown_stage_one = tk.OptionMenu(screen_auto_life, var_dropdown_stage_one, *percentage)
    dropdown_stage_one["fg"] = 'white'
    dropdown_stage_one["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_one["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_one["width"] = 4
    dropdown_stage_one.place(x=165, y=90)

    dropdown_stage_two = tk.OptionMenu(screen_auto_life, var_dropdown_stage_two, *hotkeys)
    dropdown_stage_two["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_two["fg"] = 'white'
    dropdown_stage_two["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_two["width"] = 4
    dropdown_stage_two.place(x=250, y=90)

    dropdown_stage_three = tk.OptionMenu(screen_auto_life, var_dropdown_stage_three, *percentage)
    dropdown_stage_three["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_three["fg"] = 'white'
    dropdown_stage_three["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_three["width"] = 4
    dropdown_stage_three.place(x=165, y=140)

    dropdown_stage_four = tk.OptionMenu(screen_auto_life, var_dropdown_stage_four, *hotkeys)
    dropdown_stage_four["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_four["fg"] = 'white'
    dropdown_stage_four["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_four["width"] = 4
    dropdown_stage_four.place(x=250, y=140)

    dropdown_stage_five = tk.OptionMenu(screen_auto_life, var_dropdown_stage_five, *percentage)
    dropdown_stage_five["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_five["fg"] = 'white'
    dropdown_stage_five["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_five["width"] = 4
    dropdown_stage_five.place(x=165, y=190)

    dropdown_stage_six = tk.OptionMenu(screen_auto_life, var_dropdown_stage_six, *hotkeys)
    dropdown_stage_six["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_six["fg"] = 'white'
    dropdown_stage_six["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_six["width"] = 4
    dropdown_stage_six.place(x=250, y=190)

    screen_auto_life.mainloop()


def auto_hur():
    screen_auto_hur = tk.Toplevel(root)
    screen_auto_hur.focus_force()
    screen_auto_hur.grab_set()
    w = 348
    h = 546
    sw = screen_auto_hur.winfo_screenwidth()
    sh = screen_auto_hur.winfo_screenheight()
    x = (sw - w) / 1.325
    y = (sh - h) / 2.36
    screen_auto_hur.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen_auto_hur.resizable(width=False, height=False)
    screen_auto_hur.title('Module: Auto Hur')
    screen_auto_hur.configure(background='#000', takefocus=True)
    image = Image.open('images/FundoHealingEdited.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(screen_auto_hur, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def exit_button():
        screen_auto_hur.destroy()

    def func_auto_hur():
        global bool_hur
        if not bool_hur:
            bool_hur = True
            auto_hur_button.configure(text='AutoHur: ON')
            scanning_auto_hur()
        else:
            bool_hur = False
            auto_hur_button.configure(text='AutoHur: OFF')

    def scanning_auto_hur():
        if bool_hur and master_key_start:
            screencp = capture_screen()
            hur = screencp.getpixel((1662, 336))
            hur2 = screencp.getpixel((1675, 335))
            print("Check Hur", hur, hur2)
            if hur != (197, 170, 126):
                if hur == (254, 110, 0):
                    if hur2 != (161, 127, 73):
                        pyautogui.press('f6')
                        print("Pressed Key f6")
                elif hur != (197, 170, 126):
                    pyautogui.press('f6')
                    print("Pressed Key f6")

        root.after(1500, scanning_auto_hur)

    # Buttons

    var_check_one = tk.StringVar()
    var_check_two = tk.StringVar()

    ''' ok button '''

    button_exit = tk.Button(screen_auto_hur, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button auto hur '''

    global bool_hur
    if not bool_hur:
        auto_hur_button = tk.Button(screen_auto_hur, text='AutoHur: OFF', font=('Microsoft Sans Serif', 10),
                                    bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_hur,
                                    activebackground=_from_rgb((123, 13, 5)))
        auto_hur_button.place(w=328, h=29, x=12, y=469)
    else:
        auto_hur_button = tk.Button(screen_auto_hur, text='AutoHur: ON', font=('Microsoft Sans Serif', 10),
                                    bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_hur,
                                    activebackground=_from_rgb((123, 13, 5)))
        auto_hur_button.place(w=328, h=29, x=12, y=469)

    check_one = tk.Checkbutton(screen_auto_hur, bg=_from_rgb((120, 98, 51)), height=2, text="Print on Tibia's screen",
                               variable=var_check_one, onvalue="on", offvalue="off")
    check_one.place(x=10, y=408)
    check_one.deselect()

    check_two = tk.Checkbutton(screen_auto_hur, bg=_from_rgb((120, 98, 51)), text="Low Mana Warnings",
                               variable=var_check_two, onvalue="on", offvalue="off")
    check_two.place(x=10, y=440)
    check_two.deselect()

    screen_auto_hur.mainloop()


def auto_mana():
    screen_auto_mana = tk.Toplevel(root)
    screen_auto_mana.focus_force()
    screen_auto_mana.grab_set()
    w = 348
    h = 546
    sw = screen_auto_mana.winfo_screenwidth()
    sh = screen_auto_mana.winfo_screenheight()
    x = (sw - w) / 1.325
    y = (sh - h) / 2.36
    screen_auto_mana.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen_auto_mana.resizable(width=False, height=False)
    screen_auto_mana.title('Module: Auto Mana')
    screen_auto_mana.configure(background='#000', takefocus=True)
    image = Image.open('images/FundoHealingEdited.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(screen_auto_mana, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def exit_button():
        screen_auto_mana.destroy()

    def func_auto_mana():
        global bool_mana
        if not bool_mana:
            bool_mana = True
            auto_mana_button.configure(text='AutoMana: ON')
            print("AutoMana: ON")
            global get_mana_location
            if not get_mana_location:
                ManaLocation[0], ManaLocation[1] = get_mana_position.get_mana_xy()
                get_mana_location = True
                if ManaLocation[0] and ManaLocation[1] != 0:
                    if bool_mana and master_key_start:
                        scanning_auto_mana()
                    else:
                        print("Master Key Non Activated!")
                else:
                    print("Error on Mana Localization!")
            else:
                if bool_mana and master_key_start:
                    scanning_auto_mana()
                else:
                    print("Master Key Non Activated!")
        else:
            bool_mana = False
            print("AutoMana: OFF")
            auto_mana_button.configure(text='AutoMana: OFF')

    def scanning_auto_mana():
        mana = get_mana_stage.scanning_stage(ManaLocation, manaColor, manaColorFull)

        if var_check_four.get() == "on":
            stage_two = var_dropdown_stage_three.get()
            if int(stage_two) >= mana:
                mana_button2 = var_dropdown_stage_four.get()
                pyautogui.press(mana_button2)
                print("Pressed ", mana_button2)
        elif var_check_three.get() == "on":
            stage_one = var_dropdown_stage_one.get()
            if int(stage_one) >= mana:
                mana_button1 = var_dropdown_stage_two.get()
                pyautogui.press(mana_button1)
                print("Pressed ", mana_button1)
        else:
            print("Modulo Not Configured")

        if bool_mana and master_key_start:
            root.after(300, scanning_auto_mana)

    # Buttons

    var_check_one = tk.StringVar()
    var_check_two = tk.StringVar()
    var_check_three = tk.StringVar()
    var_check_four = tk.StringVar()
    var_dropdown_stage_one = tk.StringVar()
    var_dropdown_stage_one.set(50)
    var_dropdown_stage_two = tk.StringVar()
    var_dropdown_stage_two.set("f3")
    var_dropdown_stage_three = tk.StringVar()
    var_dropdown_stage_three.set(25)
    var_dropdown_stage_four = tk.StringVar()
    var_dropdown_stage_four.set("f4")

    ''' ok button '''

    button_exit = tk.Button(screen_auto_mana, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button auto hur '''

    global bool_mana
    if not bool_mana:
        auto_mana_button = tk.Button(screen_auto_mana, text='AutoMana: OFF', font=('Microsoft Sans Serif', 10),
                                     bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_mana,
                                     activebackground=_from_rgb((123, 13, 5)))
        auto_mana_button.place(w=328, h=29, x=12, y=469)
    else:
        auto_mana_button = tk.Button(screen_auto_mana, text='AutoMana: ON', font=('Microsoft Sans Serif', 10),
                                     bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_mana,
                                     activebackground=_from_rgb((123, 13, 5)))
        auto_mana_button.place(w=328, h=29, x=12, y=469)

    check_one = tk.Checkbutton(screen_auto_mana, bg=_from_rgb((120, 98, 51)), height=2, text="Print on Tibia's screen",
                               variable=var_check_one, onvalue="on", offvalue="off")
    check_one.place(x=10, y=408)
    check_one.deselect()

    check_two = tk.Checkbutton(screen_auto_mana, bg=_from_rgb((120, 98, 51)), text="Low Mana Warnings",
                               variable=var_check_two, onvalue="on", offvalue="off")
    check_two.place(x=10, y=440)
    check_two.deselect()

    check_three = tk.Checkbutton(screen_auto_mana, bg=_from_rgb((130, 16, 6)), text="Enable Stage One",
                                 variable=var_check_three, onvalue="on", offvalue="off",
                                 activebackground=_from_rgb((130, 16, 6)))
    check_three.place(x=32, y=94)
    check_three.deselect()

    check_four = tk.Checkbutton(screen_auto_mana, bg=_from_rgb((130, 16, 6)), text="Enable Stage Two",
                                variable=var_check_four, onvalue="on", offvalue="off",
                                activebackground=_from_rgb((130, 16, 6)))
    check_four.place(x=32, y=144)
    check_four.deselect()

    dropdown_stage_one = tk.OptionMenu(screen_auto_mana, var_dropdown_stage_one, *percentage)
    dropdown_stage_one["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_one["fg"] = 'white'
    dropdown_stage_one["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_one["width"] = 4
    dropdown_stage_one.place(x=165, y=90)

    dropdown_stage_two = tk.OptionMenu(screen_auto_mana, var_dropdown_stage_two, *hotkeys)
    dropdown_stage_two["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_two["fg"] = 'white'
    dropdown_stage_two["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_two["width"] = 4
    dropdown_stage_two.place(x=250, y=90)

    dropdown_stage_three = tk.OptionMenu(screen_auto_mana, var_dropdown_stage_three, *percentage)
    dropdown_stage_three["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_three["fg"] = 'white'
    dropdown_stage_three["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_three["width"] = 4
    dropdown_stage_three.place(x=165, y=140)

    dropdown_stage_four = tk.OptionMenu(screen_auto_mana, var_dropdown_stage_four, *hotkeys)
    dropdown_stage_four["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_four["fg"] = 'white'
    dropdown_stage_four["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_four["width"] = 4
    dropdown_stage_four.place(x=250, y=140)

    screen_auto_mana.mainloop()


def auto_login():
    screen_auto_login = tk.Toplevel(root)
    screen_auto_login.focus_force()
    screen_auto_login.grab_set()
    w = 348
    h = 546
    sw = screen_auto_login.winfo_screenwidth()
    sh = screen_auto_login.winfo_screenheight()
    x = (sw - w) / 1.325
    y = (sh - h) / 2.36
    screen_auto_login.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen_auto_login.resizable(width=False, height=False)
    screen_auto_login.title('Module: Auto Login')
    screen_auto_login.configure(background='#000', takefocus=True)
    image = Image.open('images/FundoHealingEdited.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(screen_auto_login, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def exit_button():
        screen_auto_login.destroy()

    def func_auto_login():
        global bool_login
        if not bool_login:
            bool_login = True
            auto_login_button.configure(text='AutoLogin: ON')
            print("AutoLogin: ON")
            global get_login_location
            if not get_login_location:
                get_login_location = True
                username_field = pyautogui.locateOnScreen('images/TibiaSettings/AccountName.png', grayscale=True, confidence=0.8)
                print("Your Login location is:", username_field)
                username_field_Xc, username_field_Yc = pyautogui.center(username_field)
                global username_field_X
                global username_field_Y
                username_field_X = int(username_field_Xc)
                username_field_Y = int(username_field_Yc)
                login = pyautogui.locateOnScreen('images/TibiaSettings/Login.png', grayscale=True, confidence=0.8)
                print("Your Login Button location is:", login)
                loginXc, loginYc = pyautogui.center(login)
                global loginX
                global loginY
                loginX = int(loginXc)
                loginY = int(loginYc)
                if login:
                    if bool_login and master_key_start:
                        scanning_auto_login()
                    else:
                        print("Master Key Non Activated!")
                else:
                    print("ERROR!")
            else:
                if bool_login and master_key_start:
                    scanning_auto_login()
                else:
                    print("Master Key Non Activated!")
        else:
            bool_login = False
            print("AutoLogin: OFF")
            auto_login_button.configure(text='AutoLogin: OFF')

    def scanning_auto_login():
        global bool_login
        global username_value
        username_value = username.get()
        global passwd_value
        passwd_value = passwd.get()
        username_field_check = pyautogui.locateOnScreen('images/AccountName.png', grayscale=True, confidence=0.8)
        if username_field_check:
            print("You Are Offline... Trying To Login")
            time.sleep(1)
            if bool_login and master_key_start:
                global pass_mouse_position
                if username_field_X != 0 and username_field_Y != 0:
                    pass_mouse_position = pyautogui.position()
                    pyautogui.click(x=username_field_X, y=username_field_Y)
                    pyautogui.write(username_value, interval=0.15)
                    pyautogui.press('tab')
                    pyautogui.write(passwd_value, interval=0.15)
                    pyautogui.click(loginX, loginY)
                    time.sleep(2)
                    pyautogui.press('enter')
                    pyautogui.moveTo(pass_mouse_position)
                    username_field_check2 = pyautogui.locateOnScreen('images/AccountName/AccountName.png', grayscale=True,
                                                                     confidence=0.8)
                    if username_field_check2:
                        print("Error To Login !!!!")
                        username_field_check2 = None
                        username_field_check = None
                    else:
                        print("You Are Logged")
                        username_field_check = None
                        username_field_check2 = None

        if bool_login and master_key_start:
            root.after(3000, scanning_auto_login)

    # Buttons

    var_check_one = tk.StringVar()
    var_check_two = tk.StringVar()
    var_check_three = tk.StringVar()

    ''' ok button '''

    button_exit = tk.Button(screen_auto_login, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button auto login '''

    global bool_login
    if not bool_login:
        auto_login_button = tk.Button(screen_auto_login, text='AutoLogin: OFF', font=('Microsoft Sans Serif', 10),
                                      bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_login,
                                      activebackground=_from_rgb((123, 13, 5)))
        auto_login_button.place(w=328, h=29, x=12, y=469)
    else:
        auto_login_button = tk.Button(screen_auto_login, text='AutoLogin: ON', font=('Microsoft Sans Serif', 10),
                                      bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_login,
                                      activebackground=_from_rgb((123, 13, 5)))
        auto_login_button.place(w=328, h=29, x=12, y=469)

    check_one = tk.Checkbutton(screen_auto_login, bg=_from_rgb((120, 98, 51)), height=2, text="Print on Tibia's screen",
                               variable=var_check_one, onvalue="on", offvalue="off")
    check_one.place(x=10, y=408)
    check_one.deselect()

    check_two = tk.Checkbutton(screen_auto_login, bg=_from_rgb((120, 98, 51)), text="Low Mana Warnings",
                               variable=var_check_two, onvalue="on", offvalue="off")
    check_two.place(x=10, y=440)
    check_two.deselect()

    username_label = tk.Label(screen_auto_login, text='Username', font=('Microsoft Sans Serif', 10),
                              bg=_from_rgb((130, 16, 6)), fg='white')
    username_label.place(x=69, y=84)

    username = tk.Entry(screen_auto_login)
    username.place(x=149, y=86)
    global username_value
    username_value = username.get()

    passwd_label = tk.Label(screen_auto_login, text='Password', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((130, 16, 6)), fg='white')
    passwd_label.place(x=69, y=124)

    passwd = tk.Entry(screen_auto_login)
    passwd.place(x=149, y=126)
    global passwd_value
    passwd_value = passwd.get()

    screen_auto_login.mainloop()


def auto_attack():
    screen_auto_attack = tk.Toplevel(root)
    screen_auto_attack.focus_force()
    screen_auto_attack.grab_set()
    w = 348
    h = 546
    sw = screen_auto_attack.winfo_screenwidth()
    sh = screen_auto_attack.winfo_screenheight()
    x = (sw - w) / 1.325
    y = (sh - h) / 2.36
    screen_auto_attack.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen_auto_attack.resizable(width=False, height=False)
    screen_auto_attack.title('Module: Auto Attack')
    screen_auto_attack.configure(background='#000', takefocus=True)
    image = Image.open('images/FundoHealingEdited.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(screen_auto_attack, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def exit_button():
        screen_auto_attack.destroy()

    def func_auto_attack():
        global bool_auto_attack
        if not bool_auto_attack:
            bool_auto_attack = True
            auto_attack_button.configure(text='AutoAttack: ON')
            print("AutoAttack: ON")
            global get_attack_location
            if not get_attack_location:
                get_attack_location = True
                battle_location[0], battle_location[2], battle_location[1], battle_location[3] = get_battle_position.get_battle_xy()
                global get_player_location
                if not get_player_location:
                    Player[0], Player[1] = get_player_position.get_gw_xy()
                    if Player[0] and Player[1] != 0:
                        if battle_location[0] != 0:
                            if bool_auto_attack and master_key_start:
                                combine_funcs(scanning_auto_attack(), scanning_follow_modee())
                            else:
                                print("Master Key Non Activated!")
                        else:
                            print("Not Battle Position")
                    else:
                        print("Not Player Position!")
                else:
                    if bool_auto_attack and master_key_start:
                        combine_funcs(scanning_auto_attack(), scanning_follow_modee())
                    else:
                        print("Master Key Non Activated!")
            else:
                if bool_auto_attack and master_key_start:
                    combine_funcs(scanning_auto_attack(), scanning_follow_modee())
                else:
                    print("Master Key Non Activated!")
        else:
            bool_auto_attack = False
            print("AutoAttack: OFF")
            auto_attack_button.configure(text='AutoAttack: OFF')

    def scanning_auto_attack():
        if bool_auto_attack and master_key_start:
            global target_number, target_number2, battle_location, monster
            monster = var_dropdown_stage_one.get()
            Target[0], Target[1] = get_target_position.scanning_target(battle_location[0], battle_location[1], battle_location[2], battle_location[3], monster)
            target_number2 = get_target_position.number_of_targets(battle_location[0], battle_location[1], battle_location[2], battle_location[3], monster)
            print("Number of " + monster + ": ", target_number2)
            if target_number2 < target_number:
                if get_SQMs_location:
                    take_loot.take_loot(SQMs)
                    target_number = 0
                else:
                    set_SQMs.set_SQMs()

            if Target[0] != 0 and Target[1] != 0:
                target_number = get_target_position.number_of_targets(battle_location[0], battle_location[1], battle_location[2], battle_location[3], monster)

                attacking = get_target_position.attaking(battle_location[0], battle_location[1], battle_location[2], battle_location[3])

                if not attacking:
                    print("Attacking a Target")
                    past_mouse_position = pyautogui.position()
                    pyautogui.leftClick(Target[0], Target[1])
                    pyautogui.moveTo(past_mouse_position)
                    target_number2 = get_target_position.number_of_targets(battle_location[0], battle_location[1], battle_location[2], battle_location[3], monster)
                else:
                    print("You are attacking")
                    target_number2 = get_target_position.number_of_targets(battle_location[0], battle_location[1], battle_location[2], battle_location[3], monster)

        if bool_auto_attack and master_key_start:
            root.after(250, scanning_auto_attack)

    def scanning_follow_modee():
        if bool_auto_attack and master_key_start:
            battle_log = 0
            follow_x_pos, follow_y_pos = GetFollow().scanning_follow_mode()

            if follow_x_pos != 0 and follow_y_pos != 0:
                past_mouse_position = pyautogui.position()
                pyautogui.leftClick(follow_x_pos, follow_y_pos)
                pyautogui.moveTo(past_mouse_position)

        if bool_auto_attack and master_key_start:
            root.after(3000, scanning_follow_modee)

    # Buttons

    var_check_one = tk.StringVar()
    var_check_two = tk.StringVar()
    var_check_three = tk.StringVar()
    global monster
    var_dropdown_stage_one = tk.StringVar()
    var_dropdown_stage_one.set(monster)
    var_dropdown_stage_two = tk.StringVar()
    var_dropdown_stage_two.set(1)

    ''' ok button '''

    button_exit = tk.Button(screen_auto_attack, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button auto login '''

    global bool_auto_attack
    if not bool_auto_attack:
        auto_attack_button = tk.Button(screen_auto_attack, text='AutoAttack: OFF', font=('Microsoft Sans Serif', 10),
                                       bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_attack,
                                       activebackground=_from_rgb((123, 13, 5)))
        auto_attack_button.place(w=328, h=29, x=12, y=469)
    else:
        auto_attack_button = tk.Button(screen_auto_attack, text='AutoAttack: ON', font=('Microsoft Sans Serif', 10),
                                       bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_attack,
                                       activebackground=_from_rgb((123, 13, 5)))
        auto_attack_button.place(w=328, h=29, x=12, y=469)

    check_one = tk.Checkbutton(screen_auto_attack, bg=_from_rgb((120, 98, 51)), height=2,
                               text="Print on Tibia's screen",
                               variable=var_check_one, onvalue="on", offvalue="off")
    check_one.place(x=10, y=408)
    check_one.deselect()

    check_two = tk.Checkbutton(screen_auto_attack, bg=_from_rgb((120, 98, 51)), text="Low Mana Warnings",
                               variable=var_check_two, onvalue="on", offvalue="off")
    check_two.place(x=10, y=440)
    check_two.deselect()

    check_three = tk.Checkbutton(screen_auto_attack, bg=_from_rgb((130, 16, 6)), text="Attack Monster",
                                 variable=var_check_three, onvalue="on", offvalue="off",
                                 activebackground=_from_rgb((130, 16, 6)))
    check_three.place(x=32, y=74)
    check_three.select()

    dropdown_stage_one = tk.OptionMenu(screen_auto_attack, var_dropdown_stage_one, *monsters)
    dropdown_stage_one["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_one["fg"] = 'white'
    dropdown_stage_one["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_one["width"] = 4
    dropdown_stage_one.place(x=155, y=70)

    dropdown_stage_two = tk.OptionMenu(screen_auto_attack, var_dropdown_stage_two, *priority)
    dropdown_stage_two["bg"] = _from_rgb((127, 17, 8))
    dropdown_stage_two["fg"] = 'white'
    dropdown_stage_two["activebackground"] = _from_rgb((103, 13, 5))
    dropdown_stage_two["width"] = 4
    dropdown_stage_two.place(x=240, y=70)

    screen_auto_attack.mainloop()


def auto_ssa():
    screen_auto_ssa = tk.Toplevel(root)
    screen_auto_ssa.focus_force()
    screen_auto_ssa.grab_set()
    w = 348
    h = 546
    sw = screen_auto_ssa.winfo_screenwidth()
    sh = screen_auto_ssa.winfo_screenheight()
    x = (sw - w) / 1.325
    y = (sh - h) / 2.36
    screen_auto_ssa.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen_auto_ssa.resizable(width=False, height=False)
    screen_auto_ssa.title('Module: Auto SSA')
    screen_auto_ssa.configure(background='#000', takefocus=True)
    image = Image.open('images/FundoHealingEdited.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(screen_auto_ssa, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def exit_button():
        screen_auto_ssa.destroy()

    def func_auto_ssa():
        global bool_auto_ssa
        if not bool_auto_ssa:
            bool_auto_ssa = True
            auto_ssa_button.configure(text='AutoSSA: ON')
            scanning_auto_ssa()
        else:
            bool_auto_ssa = False
            auto_ssa_button.configure(text='AutoSSA: OFF')

    def scanning_auto_ssa():
        if bool_auto_ssa and master_key_start:
            screencp = capture_screen()
            global pass_mouse_position
            color = screencp.getpixel((1677, 218))
            color2 = screencp.getpixel((1677, 669))
            print("Check SSA", color, color2)
            if color == (65, 67, 70) and color2 == (108, 108, 108):
                pass_mouse_position = pyautogui.position()
                pyautogui.moveTo(1677, 669)
                pyautogui.mouseDown(button='left')
                pyautogui.moveTo(1677, 218, 0.1)
                pyautogui.mouseUp(button='left')
                pyautogui.moveTo(pass_mouse_position)

        root.after(80, scanning_auto_ssa)

    # Buttons

    var_check_one = tk.StringVar()
    var_check_two = tk.StringVar()

    ''' ok button '''

    button_exit = tk.Button(screen_auto_ssa, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button auto login '''

    global bool_auto_ssa
    if not bool_auto_ssa:
        auto_ssa_button = tk.Button(screen_auto_ssa, text='AutoSSA: OFF', font=('Microsoft Sans Serif', 10),
                                    bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_ssa,
                                    activebackground=_from_rgb((123, 13, 5)))
        auto_ssa_button.place(w=328, h=29, x=12, y=469)
    else:
        auto_ssa_button = tk.Button(screen_auto_ssa, text='AutoSSA: ON', font=('Microsoft Sans Serif', 10),
                                    bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_ssa,
                                    activebackground=_from_rgb((123, 13, 5)))
        auto_ssa_button.place(w=328, h=29, x=12, y=469)

    check_one = tk.Checkbutton(screen_auto_ssa, bg=_from_rgb((120, 98, 51)), height=2, text="Print on Tibia's screen",
                               variable=var_check_one, onvalue="on", offvalue="off")
    check_one.place(x=10, y=408)
    check_one.deselect()

    check_two = tk.Checkbutton(screen_auto_ssa, bg=_from_rgb((120, 98, 51)), text="Low Mana Warnings",
                               variable=var_check_two, onvalue="on", offvalue="off")
    check_two.place(x=10, y=440)
    check_two.deselect()

    screen_auto_ssa.mainloop()


def auto_ring():
    screen_auto_ring = tk.Toplevel(root)
    screen_auto_ring.focus_force()
    screen_auto_ring.grab_set()
    w = 348
    h = 546
    sw = screen_auto_ring.winfo_screenwidth()
    sh = screen_auto_ring.winfo_screenheight()
    x = (sw - w) / 1.325
    y = (sh - h) / 2.36
    screen_auto_ring.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen_auto_ring.resizable(width=False, height=False)
    screen_auto_ring.title('Module: Auto Ring')
    screen_auto_ring.configure(background='#000', takefocus=True)
    image = Image.open('images/FundoHealingEdited.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(screen_auto_ring, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def exit_button():
        screen_auto_ring.destroy()

    def func_auto_ring():
        global bool_auto_ring
        if not bool_auto_ring:
            bool_auto_ring = True
            auto_ring_button.configure(text='Auto Ring: ON')
            scanning_auto_ring()
        else:
            bool_auto_ring = False
            auto_ring_button.configure(text='Auto Ring: OFF')

    def scanning_auto_ring():
        if bool_auto_ring and master_key_start:
            screencp = capture_screen()
            global pass_mouse_position
            color = screencp.getpixel((1673, 283))
            color2 = screencp.getpixel((1673, 715))
            print("Check Ring", color, color2)
            if color == (69, 72, 75) and color2 == (218, 182, 70):
                pass_mouse_position = pyautogui.position()
                pyautogui.moveTo(1673, 715)
                pyautogui.mouseDown(button='left')
                pyautogui.moveTo(1673, 283, 0.1)
                pyautogui.mouseUp(button='left')
                pyautogui.moveTo(pass_mouse_position)

        root.after(150, scanning_auto_ring)

    # Buttons

    var_check_one = tk.StringVar()
    var_check_two = tk.StringVar()

    ''' ok button '''

    button_exit = tk.Button(screen_auto_ring, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button auto login '''

    global bool_auto_ring
    if not bool_auto_ring:
        auto_ring_button = tk.Button(screen_auto_ring, text='Auto Ring: OFF', font=('Microsoft Sans Serif', 10),
                                     bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_ring,
                                     activebackground=_from_rgb((123, 13, 5)))
        auto_ring_button.place(w=328, h=29, x=12, y=469)
    else:
        auto_ring_button = tk.Button(screen_auto_ring, text='Auto Ring: ON', font=('Microsoft Sans Serif', 10),
                                     bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_ring,
                                     activebackground=_from_rgb((123, 13, 5)))
        auto_ring_button.place(w=328, h=29, x=12, y=469)

    check_one = tk.Checkbutton(screen_auto_ring, bg=_from_rgb((120, 98, 51)), height=2, text="Print on Tibia's screen",
                               variable=var_check_one, onvalue="on", offvalue="off")
    check_one.place(x=10, y=408)
    check_one.deselect()

    check_two = tk.Checkbutton(screen_auto_ring, bg=_from_rgb((120, 98, 51)), text="Low Mana Warnings",
                               variable=var_check_two, onvalue="on", offvalue="off")
    check_two.place(x=10, y=440)
    check_two.deselect()

    screen_auto_ring.mainloop()


def color_change():
    screen_color_change = tk.Toplevel(root)
    screen_color_change.focus_force()
    screen_color_change.grab_set()
    w = 348
    h = 546
    sw = screen_color_change.winfo_screenwidth()
    sh = screen_color_change.winfo_screenheight()
    x = (sw - w) / 1.325
    y = (sh - h) / 2.36
    screen_color_change.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen_color_change.resizable(width=False, height=False)
    screen_color_change.title('Module: Color Change')
    screen_color_change.configure(background='#000', takefocus=True)
    image = Image.open('images/FundoHealingEdited.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(screen_color_change, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def exit_button():
        screen_color_change.destroy()

    def func_color_change():
        global bool_color_change
        if not bool_color_change:
            global get_player_location
            if not get_player_location:
                get_player_location = True
                Player[0], Player[1] = get_player_position.get_gw_xy()
                if Player[0] and Player[1] != 0:
                    bool_color_change = True
                    color_change_button.configure(text='Color Change: ON')
                    scanning_color_change()
            else:
                bool_color_change = True
                color_change_button.configure(text='Color Change: ON')
                scanning_color_change()
        else:
            bool_color_change = False
            color_change_button.configure(text='Color Change: OFF')

    def scanning_color_change():
        if bool_color_change and master_key_start:
            if keyboard.is_pressed("c"):
                pyautogui.keyDown('ctrl')
                pyautogui.click(Player[0], Player[1], button='right')
                pyautogui.keyUp('ctrl')

        root.after(65, scanning_color_change)

    def dancing():
        pyautogui.hotkey("ctrl", "up")
        pyautogui.hotkey("ctrl", "left")
        pyautogui.hotkey("ctrl", "right")
        pyautogui.hotkey("ctrl", "down")

    # Buttons

    var_check_one = tk.StringVar()
    var_check_two = tk.StringVar()

    ''' ok button '''

    button_exit = tk.Button(screen_color_change, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button auto login '''

    global bool_color_change
    if not bool_color_change:
        color_change_button = tk.Button(screen_color_change, text='Color Change: OFF',
                                        font=('Microsoft Sans Serif', 10),
                                        bg=_from_rgb((127, 17, 8)), fg='white', command=func_color_change,
                                        activebackground=_from_rgb((123, 13, 5)))
        color_change_button.place(w=328, h=29, x=12, y=469)
    else:
        color_change_button = tk.Button(screen_color_change, text='Color Change: ON', font=('Microsoft Sans Serif', 10),
                                        bg=_from_rgb((127, 17, 8)), fg='white', command=func_color_change,
                                        activebackground=_from_rgb((123, 13, 5)))
        color_change_button.place(w=328, h=29, x=12, y=469)

    screen_color_change.mainloop()


def adjust_config():
    screen_adjust_config = tk.Toplevel(root)
    screen_adjust_config.focus_force()
    screen_adjust_config.grab_set()
    w = 348
    h = 546
    sw = screen_adjust_config.winfo_screenwidth()
    sh = screen_adjust_config.winfo_screenheight()
    x = (sw - w) / 1.325
    y = (sh - h) / 2.36
    screen_adjust_config.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen_adjust_config.resizable(width=False, height=False)
    screen_adjust_config.title('Module: Adjust Config')
    screen_adjust_config.configure(background='#000', takefocus=True)
    image = Image.open('images/FundoHealingEdited.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(screen_adjust_config, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def set_title():
        global TibiaName
        try:
            TibiaName = windowTitles.find_tibia_title()
        except IndexError as e:
            print("You need to login before starting bot.")
            root.destroy()
        if TibiaName is not None:
            TibiaWindow = pygetwindow.getWindowsWithTitle(TibiaName)[0]
            TibiaAuto = pygetwindow.getWindowsWithTitle("TibiaAuto V12")[0]
            Module = pygetwindow.getWindowsWithTitle("Module: Adjust Config")[0]
            TibiaAuto.minimize()
            Module.minimize()
            TibiaWindow.maximize()
            time.sleep(1)

            # configure()

            time.sleep(3)
            TibiaAuto.maximize()
            Module.maximize()
        else:
            print("Error to Log Tibia window")

    def exit_button():
        screen_adjust_config.destroy()

    def func_adjust_config():
        global bool_adjust_config
        if not bool_adjust_config:
            bool_adjust_config = True
            adjust_config_button.configure(text='Adjust Config: ON')
            scanning_adjust_config()
        else:
            bool_adjust_config = False
            adjust_config_button.configure(text='Adjust Config: OFF')

    def scanning_adjust_config():
        if bool_adjust_config and master_key_start:
            if keyboard.is_pressed("c"):
                return

        root.after(65, scanning_adjust_config)

    # Buttons

    ''' ok button '''

    button_exit = tk.Button(screen_adjust_config, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button auto login '''

    global bool_adjust_config
    if not bool_adjust_config:
        adjust_config_button = tk.Button(screen_adjust_config, text='Adjust Config: OFF',
                                         font=('Microsoft Sans Serif', 10),
                                         bg=_from_rgb((127, 17, 8)), fg='white', command=func_adjust_config,
                                         activebackground=_from_rgb((123, 13, 5)))
        adjust_config_button.place(w=328, h=29, x=12, y=469)
    else:
        adjust_config_button = tk.Button(screen_adjust_config, text='Adjust Config: ON',
                                         font=('Microsoft Sans Serif', 10),
                                         bg=_from_rgb((127, 17, 8)), fg='white', command=func_adjust_config,
                                         activebackground=_from_rgb((123, 13, 5)))
        adjust_config_button.place(w=328, h=29, x=12, y=469)

    config_button = tk.Button(screen_adjust_config, width=15, text="Configurar", command=set_title)
    config_button.pack()
    config_button.place(x=155, y=70)

    screen_adjust_config.mainloop()


def auto_looter():
    screen_auto_looter = tk.Toplevel(root)
    screen_auto_looter.focus_force()
    screen_auto_looter.grab_set()
    w = 348
    h = 546
    sw = screen_auto_looter.winfo_screenwidth()
    sh = screen_auto_looter.winfo_screenheight()
    x = (sw - w) / 1.325
    y = (sh - h) / 2.36
    screen_auto_looter.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen_auto_looter.resizable(width=False, height=False)
    screen_auto_looter.title('Module: Auto Looter')
    screen_auto_looter.configure(background='#000', takefocus=True)
    image = Image.open('images/FundoHealingEdited.jpg')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(screen_auto_looter, image=photo, bg='#000')
    label.image = photo
    label.pack()

    def exit_button():
        screen_auto_looter.destroy()

    def func_auto_looter():
        global bool_auto_looter
        if not bool_auto_looter:
            bool_auto_looter = True
            auto_looter_button.configure(text='Auto Looter: ON')
            print("Auto Looter: ON")
            global get_player_location
            if not get_player_location:
                get_player_location = True
                Player[0], Player[1] = get_player_position.get_gw_xy()
                if Player[0] and Player[1] != 0:
                    if bool_auto_looter and master_key_start:
                        scanning_auto_looter()
                    else:
                        print("Master Key Non Activated!")
                else:
                    print("ERROR!")
            else:
                if bool_auto_looter and master_key_start:
                    scanning_auto_looter()
                else:
                    print("Master Key Non Activated!")
        else:
            bool_auto_looter = False
            print("Auto Looter: OFF")
            auto_looter_button.configure(text='Auto Looter: OFF')

    def scanning_auto_looter():
        global get_SQMs_location
        if get_SQMs_location:
            print("Scanning for loot")
            if bool_auto_looter and master_key_start:
                take_loot.take_loot(SQMs)
                time.sleep(4)
            else:
                print("Marster Key not enabled")
        else:
            set_SQMs.set_SQMs()

        if bool_auto_looter and master_key_start:
            root.after(400, scanning_auto_looter)

    # Buttons

    ''' ok button '''

    button_exit = tk.Button(screen_auto_looter, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button auto login '''

    global bool_auto_looter
    if not bool_auto_looter:
        auto_looter_button = tk.Button(screen_auto_looter, text='Auto Looter: OFF',
                                       font=('Microsoft Sans Serif', 10),
                                       bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_looter,
                                       activebackground=_from_rgb((123, 13, 5)))
        auto_looter_button.place(w=328, h=29, x=12, y=469)
    else:
        auto_looter_button = tk.Button(screen_auto_looter, text='Auto Looter: ON',
                                       font=('Microsoft Sans Serif', 10),
                                       bg=_from_rgb((127, 17, 8)), fg='white', command=func_auto_looter,
                                       activebackground=_from_rgb((123, 13, 5)))
        auto_looter_button.place(w=328, h=29, x=12, y=469)

    screen_auto_looter.mainloop()


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
            if bool_Cave_Bot and master_key_start:
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
        if bool_Cave_Bot and master_key_start:
            print("CAVE BOT PRINT...")
            for i in range(len(data)):
                print(data[i]["mark"])
                mark_box = pyautogui.locateOnScreen(f'{data[i]["mark"]}', region=(map_positions[0], map_positions[1], map_positions[2], map_positions[3]), confidence=0.9)
                if data[i]['status']:
                    pyautogui.click(mark_box[0], mark_box[1])
                    # atacar os mobs e aguardar todos morrerem

                    global target_number, target_number2, battle_location, monster
                    Target[0], Target[1] = get_target_position.scanning_target(battle_location[0], battle_location[1],
                                                                               battle_location[2], battle_location[3],
                                                                               monster)
                    target_number2 = get_target_position.number_of_targets(battle_location[0], battle_location[1],
                                                                           battle_location[2], battle_location[3],
                                                                           monster)
                    print("Number of " + monster + ": ", target_number2)
                    if target_number2 < target_number:
                        if get_SQMs_location:
                            take_loot.take_loot(SQMs)
                            target_number = 0
                        else:
                            set_SQMs.set_SQMs()

                    if Target[0] != 0 and Target[1] != 0:
                        target_number = get_target_position.number_of_targets(battle_location[0], battle_location[1],
                                                                              battle_location[2], battle_location[3],
                                                                              monster)

                        attacking = get_target_position.attaking(battle_location[0], battle_location[1],
                                                                 battle_location[2], battle_location[3])

                        if not attacking:
                            print("Attacking a Target")
                            past_mouse_position = pyautogui.position()
                            pyautogui.leftClick(Target[0], Target[1])
                            pyautogui.moveTo(past_mouse_position)
                            target_number2 = get_target_position.number_of_targets(battle_location[0],
                                                                                   battle_location[1],
                                                                                   battle_location[2],
                                                                                   battle_location[3], monster)
                        else:
                            print("You are attacking")
                            target_number2 = get_target_position.number_of_targets(battle_location[0],
                                                                                   battle_location[1],
                                                                                   battle_location[2],
                                                                                   battle_location[3], monster)

                    # bloco ----
                    time.sleep(3)
                    if pyautogui.locateOnScreen(data[i]["mark"], region=(map_positions[0], map_positions[1], map_positions[2], map_positions[3]), confidence=0.9):
                        data[i]['status'] = False
                        if i + 1 >= len(data):
                            data[i - i]['status'] = True
                        else:
                            data[i + 1]['status'] = True
                        with open('CaveBot/Scripts/ratThais.json', 'w') as wJson:
                            json.dump(data, wJson, indent=4)
                else:
                    print("Error on Cave Bot")

            if bool_Cave_Bot and master_key_start:
                root.after(300, scanning_cave_bot)

    # Buttons

    ''' ok button '''

    button_exit = tk.Button(screen_cave_bot, text='Ok', font=('Microsoft Sans Serif', 10),
                            bg=_from_rgb((127, 17, 8)), fg='white', command=exit_button,
                            activebackground=_from_rgb((123, 13, 5)))
    button_exit.place(w=84, h=29, x=130, y=504)

    ''' button auto login '''

    global bool_Cave_Bot
    if not bool_Cave_Bot:
        cave_bot_button = tk.Button(screen_cave_bot, text='Cave Bot: OFF',
                                    font=('Microsoft Sans Serif', 10),
                                    bg=_from_rgb((127, 17, 8)), fg='white', command=func_cave_bot,
                                    activebackground=_from_rgb((123, 13, 5)))
        cave_bot_button.place(w=328, h=29, x=12, y=469)
    else:
        cave_bot_button = tk.Button(screen_cave_bot, text='Cave Bot: ON',
                                    font=('Microsoft Sans Serif', 10),
                                    bg=_from_rgb((127, 17, 8)), fg='white', command=func_cave_bot,
                                    activebackground=_from_rgb((123, 13, 5)))
        cave_bot_button.place(w=328, h=29, x=12, y=469)

    screen_cave_bot.mainloop()


def main():
    config_master = tk.Tk()
    w = 270
    h = 130
    sw = config_master.winfo_screenwidth()
    sh = config_master.winfo_screenheight()
    x = (sw - w) / 2.3
    y = (sh - h) / 2.4
    config_master.geometry('%dx%d+%d+%d' % (w, h, x, y))
    config_master.resizable(width=False, height=False)
    config_master.title('TibiaAuto V12')
    config_master.configure(background=_from_rgb((120, 98, 51)), takefocus=True)

    def set_title():
        start_configuration = time.time()
        global TibiaName
        try:
            TibiaName = windowTitles.find_tibia_title()
        except IndexError as e:
            print("You need to login before starting bot.")
            config_master.destroy()
        if TibiaName is not None:
            TibiaWindow = pygetwindow.getWindowsWithTitle(TibiaName)[0]
            TibiaAuto = pygetwindow.getWindowsWithTitle("TibiaAuto V12")[0]
            TibiaAuto.minimize()
            TibiaWindow.maximize()

            time.sleep(2)

            pyautogui.PAUSE = 0.005

            global get_attack_location
            battle_location[0], battle_location[2], battle_location[1], battle_location[3] = get_battle_position.get_battle_xy()
            print(f"Your Battle Box location X: {battle_location[0]} Y: {battle_location[1]}")
            get_attack_location = True

            Player[0], Player[1], gameWindow[0], gameWindow[1], gameWindow[2], gameWindow[3] = get_player_position.get_gw_xy()
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

            end_configurantion = time.time() - start_configuration
            print(f"Your Setup Time Is: {end_configurantion:.2f} Seconds")

            print("Oppening TibiaAuto...")

            time.sleep(0.3)
            config_master.destroy()
            time.sleep(1)
            root()
        else:
            print("Error to Log Tibia window")

    config_button = tk.Button(config_master, width=15, text="Configurar", command=set_title, bg=_from_rgb((127, 17, 8)),
                              fg='white',
                              activebackground=_from_rgb((123, 13, 5)))
    config_button.pack()
    config_button.place(w=220, h=45, x=26, y=43)

    config_master.mainloop()


if __name__ == '__main__':
    main()
