from Core.HookWindow import LocateCenterImage, LocateImage


def ScanAmulet(AmuletPositions, Amulet):
    HasAmulet = [0, 0]

    HasAmulet[0], HasAmulet[1] = LocateImage('images/Amulets/' + Amulet + '.png', Precision=0.9, Region=(
        AmuletPositions[0], AmuletPositions[1], AmuletPositions[2], AmuletPositions[3]))
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
