from Core.HookWindow import LocateBoolRGBImage


def IsAttacking(BattlePosition, MonsterName):
    if LocateBoolRGBImage('images/MonstersAttack/' + MonsterName + '1.png', Region=(BattlePosition[0] - 1, BattlePosition[1] - 1, BattlePosition[2], BattlePosition[3]), Precision=0.8):
        return True
    else:
        if LocateBoolRGBImage('images/MonstersAttack/' + MonsterName + '2.png', Region=(BattlePosition[0] - 1, BattlePosition[1] - 1, BattlePosition[2], BattlePosition[3]), Precision=0.6):
            return True
        else:
            return False
