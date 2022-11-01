from core.HookWindow import LocateImage


def ScanHur(stats_position, check_pz, check_low_mana, current_mana, minimum_mana):
    is_in_pz = False
    is_low_mana = False

    stats_region = stats_position[0], stats_position[1], stats_position[2], stats_position[3]
    hur_pos = [0, 0]
    pz_pos = [0, 0]

    if (check_pz):
        pz_pos[0], pz_pos[1] = LocateImage(
            'images/PlayerStats/PZ.png', Precision=0.9, Region=(stats_region)
        )
        is_in_pz = pz_pos[0] != 0 and pz_pos[1] != 0

        if is_in_pz:
            return False

    if (check_low_mana):
        is_low_mana = current_mana <= minimum_mana

        if is_low_mana:
            return False

    hur_pos[0], hur_pos[1] = LocateImage(
        'images/PlayerStats/Hur.png', Precision=0.9, Region=(stats_region)
    )
    HasHur = hur_pos[0] != 0 and hur_pos[1] != 0

    return not HasHur
