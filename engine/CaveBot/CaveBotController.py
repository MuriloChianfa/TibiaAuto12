import json
from time import sleep, time

from conf.Hotkeys import Hotkey

from core.HookWindow import LocateCenterImage
from engine.CaveBot.Scanners import NumberOfTargets, ScanTarget, IsAttacking, NeedFollow, CheckWaypoint

TargetNumber = 0
NumberOfMonster = []


class CaveBotController:
    def __init__(self, MOUSE_OPTION, ScriptName, LootButton, TimeToStand, Walk, Loot, ForRefresh, MapPosition, BattlePosition, SQMs):
        self.MOUSE_OPTION = MOUSE_OPTION
        self.SendToClient = Hotkey(self.MOUSE_OPTION)
        self.ScriptName = ScriptName
        self.LootButton = LootButton
        self.TimeToStand = TimeToStand
        self.EnabledWalk = Walk
        self.EnabledLooting = Loot
        self.WalkForRefresh = ForRefresh
        self.MapPosition = MapPosition
        self.BattlePosition = BattlePosition
        self.SQMs = SQMs
        self.Target = []

        # Remember Set For Get From Cavebot (for me)

        self.FollowMode = True

    '''
    StartCaveBot Take The Data From Module CaveBot And Search For Mark With Status TRUE,
    When He Finds, He Starts The Engine Of CaveBot.
    '''

    def StartCaveBot(self, data, MonstersToAttack):
        while IsEnable():
            for i in range(len(data)):
                if not IsEnable():
                    return
                else:
                    if data[i]['status']:
                        self.HandleCaveBot(data, i, MonstersToAttack)

    '''
    The Handler 
    '''

    def HandleCaveBot(self, data, i, Monsters):

        global TargetNumber
        MarkLocation = [0, 0]

        sleep(self.TimeToStand)

        if not IsEnable():
            return

        '''
        Disconsider This Block If You Don't Mark The Walk Option...
        '''
        # region Walk

        if self.EnabledWalk:
            while MarkLocation[0] == 0 and MarkLocation[1] == 0:
                MarkLocation[0], MarkLocation[1] = LocateCenterImage('images/MapSettings/' + data[i]["mark"] + '.png',
                                                 Region=(
                                                     self.MapPosition[0], self.MapPosition[1], self.MapPosition[2],
                                                     self.MapPosition[3]),
                                                 Precision=0.8)
                if MarkLocation[0] == 0 and MarkLocation[1] == 0:
                    print("Mark: { ", data[i]["mark"], " } Not Located, Try Again")
                    if self.WalkForRefresh:
                        sleep(.3)
                        self.SendToClient.Press('up_arrow')
                        sleep(.1)
                        self.SendToClient.Press('left_arrow')
                        sleep(.7)
                        self.SendToClient.Press('down_arrow')
                        sleep(.1)
                        self.SendToClient.Press('right_arrow')
                        sleep(.1)
                else:
                    print("successfully Located The Mark: { ", data[i]["mark"], " } Clicking On Your Position")
                    MarkLocation[0] = self.MapPosition[0] + MarkLocation[0]
                    MarkLocation[1] = self.MapPosition[1] + MarkLocation[1]

            # Clicking In Mark Position

            if self.MOUSE_OPTION == 1:
                PastPosition = self.SendToClient.Position()
            else:
                PastPosition = [0, 0]

            self.SendToClient.LeftClick(MarkLocation[0], MarkLocation[1])

            if self.MOUSE_OPTION == 1:
                self.SendToClient.MoveTo(PastPosition[0], PastPosition[1])

        # endregion

        '''
        The Attack, Is Every Time Enabled.
        '''

        # region Attack

        for Monster in Monsters:

            FirstMonstersNumber = 0
            SecondMonstersNumber = 0

            Number = NumberOfTargets(self.BattlePosition, Monster)
            # NumberOfMonster.append(Number)

            while Number > 0:

                if not IsEnable():
                    return

                self.Target = ScanTarget(self.BattlePosition, Monster)

                if self.Target[0] != 0 and self.Target[1] != 0:

                    # Verify If You Are Already Attacking !
                    if IsAttacking(self.BattlePosition):
                        print("Attacking The Target")

                        if self.MOUSE_OPTION == 1:
                            PastPosition = self.SendToClient.Position()
                        else:
                            PastPosition = [0, 0]

                        print(self.Target[0] - 10)
                        print(self.Target[1])

                        self.SendToClient.LeftClick(self.Target[0] - 10, self.Target[1])

                        if self.MOUSE_OPTION == 1:
                            self.SendToClient.MoveTo(PastPosition[0], PastPosition[1])

                        FirstMonstersNumber = NumberOfTargets(self.BattlePosition, Monster)
                    else:
                        print("You are attacking")
                        FirstMonstersNumber = NumberOfTargets(self.BattlePosition, Monster)

                # Control Follow Mode In Attack (Follow Or Idle)

                if self.FollowMode:

                    IsNeedFollow = NeedFollow()

                    if IsNeedFollow:
                        print("Clicking In Follow")

                        if self.MOUSE_OPTION == 1:
                            PastPosition = self.SendToClient.Position()
                        else:
                            PastPosition = [0, 0]
                        FollowPosition = LocateCenterImage('images/TibiaSettings/NotFollow.png', Precision=0.7)
                        self.SendToClient.LeftClick(FollowPosition[0], FollowPosition[1])
                        if self.MOUSE_OPTION == 1:
                            self.SendToClient.MoveTo(PastPosition[0], PastPosition[1])

                sleep(.2)

                self.Target = ScanTarget(self.BattlePosition, Monster)

                if self.Target[0] != 0 and self.Target[1] != 0:

                    # Verify If You Are Already Attacking !
                    if IsAttacking(self.BattlePosition):
                        # For Debugging
                        # print("Attacking The Target2")

                        if self.MOUSE_OPTION == 1:
                            PastPosition = self.SendToClient.Position()
                        else:
                            PastPosition = [0, 0]

                        self.SendToClient.LeftClick(self.Target[0], self.Target[1])

                        if self.MOUSE_OPTION == 1:
                            self.SendToClient.MoveTo(PastPosition[0], PastPosition[1])

                        SecondMonstersNumber = NumberOfTargets(self.BattlePosition, Monster)
                    else:
                        # For Debugging
                        # print("You are attacking2")

                        SecondMonstersNumber = NumberOfTargets(self.BattlePosition, Monster)

                if SecondMonstersNumber < FirstMonstersNumber:
                    self.TakeLoot()

                self.Target = []

                sleep(0.2)

                Number = NumberOfTargets(self.BattlePosition, Monster)

                if Number == 0:
                    break

        '''
            If Walk Option Is Enabled, It Verify If The Player Already
            Arrived To The Current Mark.
            
            If Already Arrived, It Set On Script, The Current Mark As False
            And The Next Mark As True, For The Next Check.
        '''

        if self.EnabledWalk:
            if CheckWaypoint(data[i]["mark"], self.MapPosition):
                data[i]['status'] = False
                if i + 1 == len(data):
                    data[i - i]['status'] = True
                    with open('Scripts/' + self.ScriptName + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                else:
                    data[i + 1]['status'] = True
                    with open('Scripts/' + self.ScriptName + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
            else:
                self.HandleCaveBot(data, i, Monsters)

        # endregion

    '''
        Clicking Around Of The Player To Get A Loot.
    '''

    def TakeLoot(self):
        if self.MOUSE_OPTION == 1:
            PastPosition = self.SendToClient.Position()
        else:
            PastPosition = [0, 0]

        # For Debugging
        # StartLootTime = time()

        for i, j in zip(range(0, 18, + 2), range(1, 19, + 2)):
            if self.LootButton == 'right':
                self.SendToClient.RightClick(self.SQMs[i], self.SQMs[j])
            elif self.LootButton == 'left':
                self.SendToClient.LeftClick(self.SQMs[i], self.SQMs[j])

        # For Debugging
        # EndLootTime = time() - StartLootTime

        if self.MOUSE_OPTION == 1:
            self.SendToClient.MoveTo(PastPosition[0], PastPosition[1])

        # For Debugging
        # print("Looted In: ", EndLootTime)


'''
    Import The EnabledCaveBot Variable From CaveBot Module, To Verify
    If CaveBot Is Enabled.
'''


def IsEnable():
    from modules.CaveBot import EnabledCaveBot
    return EnabledCaveBot
