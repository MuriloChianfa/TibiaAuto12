from core.HookWindow import LocateImage


def ScanHur(StatsPositions):
    HasHur = [0, 0]

    HasHur[0], HasHur[1] = LocateImage('images/PlayerStats/Hur.png', Precision=0.9, Region=(
        StatsPositions[0], StatsPositions[1], StatsPositions[2], StatsPositions[3]))
    if HasHur[0] != 0 and HasHur[1] != 0:
        return False
    else:
        return True
