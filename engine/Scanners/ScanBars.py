from conf.Constants import LifeColor, LifeColorFull, ManaColor, ManaColorFull
from engine.Scanners.ScanStages import ScanStages


def ScanBars(health_location, mana_location):
    return (ScanStages('Life').ScanStages(health_location, LifeColor, LifeColorFull), ScanStages('Mana').ScanStages(mana_location, ManaColor, ManaColorFull))
