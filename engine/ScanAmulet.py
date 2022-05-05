from core.HookWindow import LocateCenterImage, LocateBoolRGBImage


def ScanAmulet(AmuletPositions, Amulet, Precision):
    return not LocateBoolRGBImage('images/Amulets/' + Amulet + '.png', Precision=Precision, Region=(
        AmuletPositions[0] - 1, AmuletPositions[1] - 1, AmuletPositions[2] + 1, AmuletPositions[3] + 1))


def SearchForAmulet(Amulet):
    FoundAmulet = [0, 0]

    FoundAmulet[0], FoundAmulet[1] = LocateCenterImage('images/Amulets/' + Amulet + '.png', Precision=0.9)
    if FoundAmulet[0] != 0 and FoundAmulet[1] != 0:
        return FoundAmulet[0], FoundAmulet[1]
    else:
        return 0, 0
