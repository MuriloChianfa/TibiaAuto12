from Core.HookWindow import LocateImage


def CheckWaypoint(image, map_positions):
    wpt = [0, 0]
    middle_start = (map_positions[0] + 48, map_positions[1] + 48)
    middle_end = (map_positions[2] - 48, map_positions[3] - 48)

    wpt[0], wpt[1] = LocateImage('images/MapSettings/' + image + '.png', Precision=0.7, Region=(middle_start[0], middle_start[1], middle_end[0], middle_end[1]))

    if wpt[0] != 0 and wpt[1] != 0:
        print("Arrived At Mark:", image)
        return True
    else:
        print("Didn't Arrived At Mark:", image, "\n")
        return False
