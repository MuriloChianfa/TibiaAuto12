from Core.HookWindow import LocateCenterImage, LocateImage

BattlePositions = [0, 0, 0, 0]
MapPositions = [0, 0, 0, 0]
StatsPositions = [0, 0, 0, 0]
GameWindow = [0, 0, 0, 0]
Player = [0, 0]
SQMs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
SQMsSizes = [0, 0]


def GetAccountNamePosition():
    AccountName = LocateCenterImage('images/TibiaSettings/AccountName.png', Precision=0.9)
    if AccountName[0] != 0 and AccountName[1] != 0:
        return AccountName[0], AccountName[1]
    else:
        return 0, 0


def GetBattlePosition():
    BattlePositions[0], BattlePositions[1] = LocateCenterImage('images/TibiaSettings/BattleList.png', Precision=0.75)
    BattlePositions[0] = BattlePositions[0] - 40
    BattlePositions[1] = BattlePositions[1] - 5
    BattlePositions[2] = BattlePositions[0] + 155
    BattlePositions[3] = BattlePositions[1] + 415

    if BattlePositions[0] != 0 and BattlePositions[1] != 0:
        return int(BattlePositions[0]), int(BattlePositions[1]), int(BattlePositions[2]), int(
            BattlePositions[3])
    else:
        return 0, 0, 0, 0


def GetHealthPosition():
    HealthPositions = LocateCenterImage('images/PlayerSettings/health.png', Precision=0.8)
    if HealthPositions[0] != 0 and HealthPositions[1] != 0:
        return HealthPositions[0], HealthPositions[1]
    else:
        return 0, 0


def GetManaPosition():
    ManaPositions = LocateCenterImage('images/PlayerSettings/mana.png', Precision=0.9)
    if ManaPositions[0] != 0 and ManaPositions[1] != 0:
        return ManaPositions[0], ManaPositions[1]


def GetMapPosition():
    top_right = LocateImage("images/MapSettings/MapSettings.png", Precision=0.8)
    map_size = 110  # 110px square
    MapPositions[0], MapPositions[1] = top_right[0] - map_size + 4, top_right[1] + 1
    MapPositions[2], MapPositions[3] = top_right[0] - 1, top_right[1] + map_size - 1
    if top_right[0] != -1:
        print(f"MiniMap Start [X: {MapPositions[0]}, Y: {MapPositions[1]}]")
        print(f"MiniMap End [X: {MapPositions[2]}, Y: {MapPositions[3]}]")
        print("")
        print(f"Size of MiniMap [X: {MapPositions[2] - MapPositions[0]}, Y: {MapPositions[3] - MapPositions[1]}]")
        return MapPositions[0], MapPositions[1], MapPositions[2], MapPositions[3]
    else:
        print("Error To Get Map Positions")
        return -1, -1, -1, -1


def GetStatsPosition():
    StatsPositions[0], StatsPositions[1] = LocateImage('images/TibiaSettings/Stop.png', Precision=0.8)
    if StatsPositions[0] != 0 and StatsPositions[1] != 0:
        StatsPositions[0] = StatsPositions[0] - 117
        StatsPositions[1] = StatsPositions[1] + 1
        StatsPositions[2] = StatsPositions[0] + 105
        StatsPositions[3] = StatsPositions[1] + 10
        return StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3]
    else:
        return 0, 0, 0, 0


def GetPlayerPosition():
    LeftGameWindow = LocateImage("images/PlayerSettings/LeftOption1.png", Precision=0.75)
    if LeftGameWindow[0] == 0 and LeftGameWindow[1] == 0:
        LeftGameWindow = LocateImage("images/PlayerSettings/LeftOption2.png", Precision=0.75)

    if LeftGameWindow[0] == 0 and LeftGameWindow[1] == 0:
        LeftGameWindow = LocateImage("images/PlayerSettings/LeftOption3.png", Precision=0.75)

    try:
        GameWindow[0] = int(LeftGameWindow[0])
        GameWindow[1] = int(LeftGameWindow[1])
    except Exception as errno:
        print("?Error On ", errno)

    RightGameWindow = LocateImage("images/PlayerSettings/RightOption1.png", Precision=0.75)
    if RightGameWindow[0] == 0 and RightGameWindow[1] == 0:
        RightGameWindow = LocateImage("images/PlayerSettings/RightOption2.png", Precision=0.75)

    if RightGameWindow[0] == 0 and RightGameWindow[1] == 0:
        RightGameWindow = LocateImage("images/PlayerSettings/RightOption3.png", Precision=0.75)

    if RightGameWindow[0] == 0 and RightGameWindow[1] == 0:
        RightGameWindow = LocateImage("images/PlayerSettings/RightOption4.png", Precision=0.75)
    try:
        GameWindow[2] = int(RightGameWindow[0])
    except Exception as errno:
        print("?Error On ", errno)

    ButtomGameWindow = LocateImage("images/PlayerSettings/EndLocation.png", Precision=0.7)
    if ButtomGameWindow[0] == 0 and ButtomGameWindow[1] == 0:
        print("BUTTON GAME WINDOWS IS NONE")
    else:
        GameWindow[3] = int(ButtomGameWindow[1])

    if GameWindow[0] != 0 and GameWindow[2] != 0:
        Player[0] = int(((GameWindow[2] - GameWindow[0]) / 2) + GameWindow[0])
    else:
        try:
            raise Exception('ex')
        except Exception as Ex:
            print('X Game Window Error... Please Press "c" With Your Mouse On Player Position')
            import keyboard
            from Conf.Hotkeys import Hotkey
            MoveMouse = Hotkey(1)
            Waiting = True
            while Waiting:
                if keyboard.is_pressed("c"):
                    x, y = MoveMouse.Position()
                    Player[0] = x
                    Player[1] = y
                    if GameWindow[0] == 0:
                        GameWindow[0] = 1
                    if GameWindow[1] == 0:
                        GameWindow[1] = 1
                    if GameWindow[2] == 0:
                        GameWindow[2] = 1
                    if GameWindow[3] == 0:
                        GameWindow[3] = 1
                    return x, y, GameWindow[0], GameWindow[1], GameWindow[2], GameWindow[3]

    if GameWindow[1] != 0 and GameWindow[3] != 0:
        Player[1] = int(((GameWindow[3] - GameWindow[1]) / 2) + GameWindow[1])
    else:
        try:
            raise Exception('Y Game Window Error')
        except Exception as Ex:
            print(Ex)
            pass

    if Player[1] != 0:
        return Player[0], Player[1], GameWindow[0], GameWindow[1], GameWindow[2], GameWindow[3]
    else:
        print("Error To Get Player Position !!!")
        return 0, 0, 0, 0, 0, 0


def SetSQMs():
    if GameWindow[0] and GameWindow[1] != 0:
        SQMsSizes[0] = int((GameWindow[2] - GameWindow[0]) / 15)
        SQMsSizes[1] = int((GameWindow[3] - GameWindow[1]) / 11)
        print(f"Size of Your SQM [Width: {SQMsSizes[0]}px, Height: {SQMsSizes[1]}px]")
        print('')
    else:
        print("Reconfiguring The Player Position")
        print('')
        Player[0], Player[1], GameWindow[0], GameWindow[1], GameWindow[2], GameWindow[
            3] = GetPlayerPosition()
        SetSQMs()

    if Player[0] and Player[1] != 0 and SQMsSizes[0] and SQMsSizes[1] != 0:
        SQMs[0] = Player[0] - SQMsSizes[0]
        SQMs[1] = Player[1] + SQMsSizes[1]
        SQMs[2] = Player[0]
        SQMs[3] = Player[1] + SQMsSizes[1]
        SQMs[4] = Player[0] + SQMsSizes[0]
        SQMs[5] = Player[1] + SQMsSizes[1]
        SQMs[6] = Player[0] - SQMsSizes[0]
        SQMs[7] = Player[1]
        SQMs[8] = Player[0]
        SQMs[9] = Player[1]
        SQMs[10] = Player[0] + SQMsSizes[0]
        SQMs[11] = Player[1]
        SQMs[12] = Player[0] - SQMsSizes[0]
        SQMs[13] = Player[1] - SQMsSizes[1]
        SQMs[14] = Player[0]
        SQMs[15] = Player[1] - SQMsSizes[1]
        SQMs[16] = Player[0] + SQMsSizes[0]
        SQMs[17] = Player[1] - SQMsSizes[1]
        return SQMs[0], SQMs[1], SQMs[2], SQMs[3], SQMs[4], SQMs[5], SQMs[6], \
               SQMs[7], SQMs[8], SQMs[9], SQMs[10], SQMs[11], SQMs[12], SQMs[13], \
               SQMs[14], SQMs[15], SQMs[16], SQMs[17]
    else:
        print("Setting Player Position...")
        Player[0], Player[1], GameWindow[0], GameWindow[1], GameWindow[2], GameWindow[
            3] = GetPlayerPosition()
        SetSQMs()
