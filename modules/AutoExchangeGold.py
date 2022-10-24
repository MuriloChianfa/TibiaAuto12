import time
import json

from tkinter.constants import RAISED, SUNKEN
from conf.Constants import Containers

from conf.Hotkeys import Hotkey
from conf.conf_manager import ConfManager

from core.GUI import *
from core.GUIManager import *
from core.GUISetter import GUISetter
from core.Getters import GetMainContainerPosition
from core.ThreadManager import ThreadManager
from engine.Scanners.ScanAutoExchangeGold import ScanAutoExchangeGold

ContainersPath = 'images/Items/None/Containers'

EnabledAutoExchangeGold = False
NewMainContainerPosition = [0, 0, 0, 0]
BackpackImg = None
BagImg = None
BasketImg = None
BeachBackpackImg = None
BlueBackpackImg = None
BrocadeBagImg = None
BuggyBackpackImg = None
CamouflageBackpackImg = None
CrownBackpackImg = None
DeeplingBackpackImg = None
DemonBackpackImg = None
DragonBackpackImg = None
ExpeditionBackpackImg = None
FurBackpackImg = None
FurBagImg = None
GloothBackpackImg = None
GoldenBackpackImg = None
GreenBackpackImg = None
GreenBagImg = None
GreyBackpackImg = None
JewelledBackpackImg = None
MinotaurBackpackImg = None
OrangeBackpackImg = None
PirateBackpackImg = None
PirateBagImg = None
PresentImg = None
PurpleBackpackImg = None
RedBackpackImg = None
RedBagImg = None
ShoppingBagImg = None
StampedParcelImg = None
YellowBackpackImg = None

GUIChanges = []


class AutoExchangeGold:
    def __init__(self, ContainerLocation, MOUSE_OPTION):
        self.AutoExchangeGold = GUI(
            'AutoExchangeGold', 'Module: Auto Exchange Gold')
        self.AutoExchangeGold.DefaultWindow(
            'AutoExchangeGold', [186, 252], [1.4, 2.29])
        self.Setter = GUISetter("ExchangeGoldLoader")
        self.ThreadManager = ThreadManager("ThreadAutoExchangeGold")
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.Conf = ConfManager.get('conf.json')
        preferences_path = self.Conf['preferences_name']
        preferences = ConfManager.get(preferences_path)

        _container_found = ContainerLocation[0] != 0 and ContainerLocation[1] != 0
        _container_set = not preferences['Boxes']['MainContainerBox'][0]['Stats']

        NewMainContainerPosition = [ContainerLocation[0], ContainerLocation[1], preferences['Boxes']
                                    ['MainContainerBox'][0]['w'], preferences['Boxes']['MainContainerBox'][0]['h']]

        global BackpackImg, BagImg, BasketImg, BeachBackpackImg, BlueBackpackImg, BrocadeBagImg, BuggyBackpackImg, CamouflageBackpackImg, CrownBackpackImg, DeeplingBackpackImg, DemonBackpackImg, DragonBackpackImg, ExpeditionBackpackImg, FurBackpackImg, FurBagImg, GloothBackpackImg, GoldenBackpackImg, GreenBackpackImg, GreenBagImg, GreyBackpackImg, JewelledBackpackImg, MinotaurBackpackImg, OrangeBackpackImg, PirateBackpackImg, PirateBagImg, PresentImg, PurpleBackpackImg, RedBackpackImg, RedBagImg, ShoppingBagImg, StampedParcelImg, YellowBackpackImg

        BackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/Backpack.png', [64, 64])
        BagImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/Bag.png', [64, 64])
        BasketImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/Basket.png', [64, 64])
        BeachBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/BeachBackpack.png', [64, 64])
        BlueBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/BlueBackpack.png', [64, 64])
        BrocadeBagImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/BrocadeBag.png', [64, 64])
        BuggyBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/BuggyBackpack.png', [64, 64])
        CamouflageBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/CamouflageBackpack.png', [64, 64])
        CrownBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/CrownBackpack.png', [64, 64])
        DeeplingBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/DeeplingBackpack.png', [64, 64])
        DemonBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/DemonBackpack.png', [64, 64])
        DragonBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/DragonBackpack.png', [64, 64])
        ExpeditionBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/ExpeditionBackpack.png', [64, 64])
        FurBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/FurBackpack.png', [64, 64])
        FurBagImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/FurBag.png', [64, 64])
        GloothBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/GloothBackpack.png', [64, 64])
        GoldenBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/GoldenBackpack.png', [64, 64])
        GreenBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/GreenBackpack.png', [64, 64])
        GreenBagImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/GreenBag.png', [64, 64])
        GreyBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/GreyBackpack.png', [64, 64])
        JewelledBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/JewelledBackpack.png', [64, 64])
        MinotaurBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/MinotaurBackpack.png', [64, 64])
        OrangeBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/OrangeBackpack.png', [64, 64])
        PirateBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/PirateBackpack.png', [64, 64])
        PirateBagImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/PirateBag.png', [64, 64])
        PresentImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/Present.png', [64, 64])
        PurpleBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/PurpleBackpack.png', [64, 64])
        RedBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/RedBackpack.png', [64, 64])
        RedBagImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/RedBag.png', [64, 64])
        ShoppingBagImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/ShoppingBag.png', [64, 64])
        StampedParcelImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/StampedParcel.png', [64, 64])
        YellowBackpackImg = self.AutoExchangeGold.openImage(
            f'{ContainersPath}/YellowBackpack.png', [64, 64])

        def SetPreferencesMainContainer(name):
            BackpackVarName = f'{name}Img'
            LabelImage.configure(image=globals()[BackpackVarName])

            NewMainContainerPosition[0], NewMainContainerPosition[1] = GetMainContainerPosition(
                name)
            time.sleep(.2)

            preferences['Boxes']['MainContainerBox'][0]['x'] = int(
                NewMainContainerPosition[0])
            preferences['Boxes']['MainContainerBox'][0]['y'] = int(
                NewMainContainerPosition[1])
            preferences['Boxes']['MainContainerBox'][0]['Stats'] = True

            with open(f'scripts/{preferences_path}', 'w') as wJson:
                json.dump(preferences, wJson, indent=4)

            if NewMainContainerPosition[0] != 0 and NewMainContainerPosition[1] != 0:
                LabelImage.configure(bg='green')
                ButtonEnabled.config(state='active')
                return True

            LabelImage.configure(bg='red')
            ButtonEnabled.config(state='disabled')
            return False

        def ToggleState():
            global EnabledAutoExchangeGold
            if not EnabledAutoExchangeGold:
                EnabledAutoExchangeGold = True
                CheckingButtons()
                self.ThreadManager.NewThread(Scan)
                ButtonEnabled.configure(
                    text='Auto Gold: ON', relief=SUNKEN, bg=rgb((158, 46, 34)))
                print("AutoExchangeGold: ON")
            else:
                EnabledAutoExchangeGold = False
                CheckingButtons()
                self.ThreadManager.StopThread()
                ButtonEnabled.configure(
                    text='Auto Gold: OFF', relief=RAISED, bg=rgb((127, 17, 8)))
                print("AutoExchangeGold: OFF")

        def Scan():
            while EnabledAutoExchangeGold:
                ScanAutoExchangeGold(EnabledAutoExchangeGold, (NewMainContainerPosition[0], NewMainContainerPosition[1]), (
                    NewMainContainerPosition[2], NewMainContainerPosition[3]), self.SendToClient.RawRightClick)

                time.sleep(2)

        def CheckingGUI(Init, Get, Name):
            if Get != Init:
                GUIChanges.append((Name, Get))

        def Destroy():
            CheckingGUI(InitiatedMainContainerName,
                        MainContainerName.get(), 'MainContainerName')

            if len(GUIChanges) != 0:
                for EachChange in range(len(GUIChanges)):
                    self.Setter.SetVariables.SetVar(
                        GUIChanges[EachChange][0], GUIChanges[EachChange][1])

            self.AutoExchangeGold.destroyWindow()

        self.AutoExchangeGold.addButton('OK', Destroy, [73, 21], [60, 227])

        MainContainerName, InitiatedMainContainerName = self.Setter.Variables.Str(
            'MainContainerName'
        )

        global EnabledAutoExchangeGold
        if not EnabledAutoExchangeGold:
            ButtonEnabled = self.AutoExchangeGold.addButton(
                'Auto Gold: OFF', ToggleState, [108, 24], [44, 199])
        else:
            ButtonEnabled = self.AutoExchangeGold.addButton(
                'Auto Gold: ON', ToggleState, [108, 24], [44, 199])
            ButtonEnabled.configure(relief=SUNKEN, bg=rgb((158, 46, 34)))
        ButtonEnabled.config(
            state='active' if _container_found else 'disabled')

        ImgContainer = f"{ContainersPath}/{MainContainerName.get() if MainContainerName.get() else 'Bag'}.png"
        ImageID = self.AutoExchangeGold.openImage(ImgContainer, [64, 64])

        ImgLabel = self.AutoExchangeGold.addLabel(
            'Current container', [44, 20])
        LabelImage = self.AutoExchangeGold.addImage(ImageID, [60, 45])
        LabelImage.configure(
            borderwidth=2, bg='green' if _container_found else 'yellow' if _container_set else 'red')
        SelectedContainerName = self.AutoExchangeGold.addOption(
            MainContainerName, Containers, [20, 122], width=18, command=SetPreferencesMainContainer)
        SearchContainerButton = self.AutoExchangeGold.addButton(
            'Search Container', lambda: SetPreferencesMainContainer(MainContainerName.get()), [126, 24], [32, 156])

        def CheckingButtons():
            if EnabledAutoExchangeGold:
                Disable(LabelImage)
                Disable(ImgLabel)
                Disable(SelectedContainerName)
                Disable(SearchContainerButton)
            else:
                Enable(LabelImage)
                Enable(ImgLabel)
                Enable(SelectedContainerName)
                Enable(SearchContainerButton)

            ExecGUITrigger()

        CheckingButtons()

        self.AutoExchangeGold.Protocol(Destroy)
        self.AutoExchangeGold.loop()
