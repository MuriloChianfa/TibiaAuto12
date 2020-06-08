from Core.HookWindow import LocateCenterImage, LocateImage


def ScanRing(RingPositions):
    NoHasRing = [0, 0]

    NoHasRing[0], NoHasRing[1] = LocateImage('images/PlayerStats/NoRing.png', Precision=0.9, Region=(
        RingPositions[0], RingPositions[1], RingPositions[2], RingPositions[3]))
    if NoHasRing[0] != 0 and NoHasRing[1] != 0:
        return True
    else:
        return False


def SearchForRing(Ring):
    FoundRing = [0, 0]

    FoundRing[0], FoundRing[1] = LocateCenterImage('images/Rings/' + Ring + '.png', Precision=0.9)
    if FoundRing[0] != 0 and FoundRing[1] != 0:
        return FoundRing[0], FoundRing[1]
    else:
        return 0, 0
