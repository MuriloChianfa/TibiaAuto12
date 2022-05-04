from core.HookWindow import LocateCenterImage, LocateImage


def ScanAmulet(AmuletPositions, Amulet, Precision):
    HasAmulet = [0, 0]

    HasAmulet[0], HasAmulet[1] = LocateImage('images/Items/None/Amulets/' + Amulet + '.png', Precision=Precision, Region=(
        AmuletPositions[0] - 1, AmuletPositions[1] - 1, AmuletPositions[2] + 1, AmuletPositions[3] + 1))
    if HasAmulet[0] != 0 and HasAmulet[1] != 0:
        return False
    else:
        return True


def SearchForAmulet(Amulet):
    FoundAmulet = [0, 0]

    FoundAmulet[0], FoundAmulet[1] = LocateCenterImage('images/Amulets/' + Amulet + '.png', Precision=0.9)
    if FoundAmulet[0] != 0 and FoundAmulet[1] != 0:
        return FoundAmulet[0], FoundAmulet[1]
    else:
        return 0, 0
