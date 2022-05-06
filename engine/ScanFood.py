from core.HookWindow import LocateImage


def scan_food(stats_positions):
    starving = [0, 0]

    starving[0], starving[1] = LocateImage('images/PlayerStats/Starving.png', Precision=0.9, Region=(
        stats_positions[0], stats_positions[1], stats_positions[2], stats_positions[3]))

    if starving[0] != 0 and starving[1] != 0:
        return True
    return False
