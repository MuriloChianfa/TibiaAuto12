from Core.HookWindow import LocateAllImages, LocateCenterImage, LocateBoolRGBImage, LocateImage


def NumberOfTargets(BattlePosition, Monster):
    Number = LocateAllImages('images/Targets/' + Monster + '.png', Precision=0.8, Region=(
        BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))

    if Number > 0:
        return Number
    else:
        return 0


def ScanTarget(BattlePosition, Monster):
    HasTarget = [0, 0]

    HasTarget[0], HasTarget[1] = LocateCenterImage('images/Targets/' + Monster + '.png', Precision=0.86, Region=(
        BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))

    if HasTarget[0] != 0 and HasTarget[1] != 0:
        if HasTarget[0] < BattlePosition[0]:
            return (BattlePosition[0] - 30) + HasTarget[0] + 1, HasTarget[1] + BattlePosition[1] + 1
        else:
            return (BattlePosition[0] - 40) + HasTarget[0] + 1, HasTarget[1] + BattlePosition[1] + 1
    else:
        return 0, 0


def CheckWaypoint(image, map_positions):
    wpt = [0, 0]
    middle_start = (map_positions[0] + 48, map_positions[1] + 48)
    middle_end = (map_positions[2] - 48, map_positions[3] - 48)

    wpt[0], wpt[1] = LocateImage('images/MapSettings/' + image + '.png', Precision=0.7, Region=(middle_start[0], middle_start[1], middle_end[0], middle_end[1]))

    if wpt[0] != 0 and wpt[1] != 0:
        print("Arrived At Mark:", image)
        return True
    else:
        print("Didn't Arrived At Mark:", image)
        return False


def IsAttacking(BattlePosition):
    X, Y = LocateCenterImage('images/MonstersAttack/RedColor1.png', Precision=0.75, Region=(
        BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))
    if X != 0 and Y != 0:
        print('1', X, Y)
        return True
    else:
        X, Y = LocateCenterImage('images/MonstersAttack/RedColor2.png', Precision=0.85, Region=(
            BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))
        if X != 0 and Y != 0:
            print('2', X, Y)
            return True
        else:
            X, Y = LocateCenterImage('images/MonstersAttack/RedColor3.png', Precision=0.65, Region=(
                BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))
            if X != 0 and Y != 0:
                print('3', X, Y)
                return True
            else:
                X, Y = LocateCenterImage('images/MonstersAttack/RedColor4.png', Precision=0.75, Region=(
                    BattlePosition[0], BattlePosition[1], BattlePosition[2], BattlePosition[3]))
                if X != 0 and Y != 0:
                    print('4', X, Y)
                    return True
                else:
                    return False


def NeedFollow():
    X, Y = LocateImage('images/TibiaSettings/Idle.png', Precision=0.7)
    if X != 0 and Y != 0:
        return True
    else:
        return False


def NeedIdle():
    X, Y = LocateImage('images/TibiaSettings/Following.png', Precision=0.7)
    if X != 0 and Y != 0:
        return True
    else:
        return False
