MainPath = "images"

# Percentage For ScanStages.py, More Percents Require Mode Hardware Work ! But Elevate The Bot Precision
Percentage = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
Priority = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# RGB Of Life Color Pixel For Analyze In ScanStages.py
LifeColorFull = [194, 74, 74]
LifeColor = [219, 79, 79]

# RGB Of Mana Color Pixel For Analyze In ScanStages.py
ManaColorFull = [45, 45, 105]
ManaColor = [83, 80, 218]

# region Items

ItemsPath = MainPath + "/Items/"

ContainersNamePath = ItemsPath + "ContainersName/"

CornersItemsPath = ItemsPath + "Corners/"
FramesItemsPath = ItemsPath + "Frames/"
NoneItemsPath = ItemsPath + "Nome/"


# Containers
Containers = {
    "Backpack": {"Name": "Backpack", "Precision": 0.8},
    "Bag": {"Name": "Bag", "Precision": 0.8},
    "Basket": {"Name": "Basket", "Precision": 0.8},
    "BeachBackpack": {"Name": "BeachBackpack", "Precision": 0.8},
    "BlueBackpack": {"Name": "BlueBackpack", "Precision": 0.8},
    "BrocadeBag": {"Name": "BrocadeBag", "Precision": 0.8},
    "BuggyBackpack": {"Name": "BuggyBackpack", "Precision": 0.8},
    "CamouflageBackpack": {"Name": "CamouflageBackpack", "Precision": 0.8},
    "CrownBackpack": {"Name": "CrownBackpack", "Precision": 0.8},
    "DeeplingBackpack": {"Name": "DeeplingBackpack", "Precision": 0.8},
    "DemonBackpack": {"Name": "DemonBackpack", "Precision": 0.8},
    "DragonBackpack": {"Name": "DragonBackpack", "Precision": 0.8},
    "ExpeditionBackpack": {"Name": "ExpeditionBackpack", "Precision": 0.8},
    "FurBackpack": {"Name": "FurBackpack", "Precision": 0.8},
    "FurBag": {"Name": "FurBag", "Precision": 0.8},
    "GloothBackpack": {"Name": "GloothBackpack", "Precision": 0.8},
    "GoldenBackpack": {"Name": "GoldenBackpack", "Precision": 0.8},
    "GreenBackpack": {"Name": "GreenBackpack", "Precision": 0.8},
    "GreenBag": {"Name": "GreenBag", "Precision": 0.8},
    "GreyBackpack": {"Name": "GreyBackpack", "Precision": 0.8},
    "JewelledBackpack": {"Name": "JewelledBackpack", "Precision": 0.8},
    "MinotaurBackpack": {"Name": "MinotaurBackpack", "Precision": 0.8},
    "OrangeBackpack": {"Name": "OrangeBackpack", "Precision": 0.8},
    "PirateBackpack": {"Name": "PirateBackpack", "Precision": 0.8},
    "PirateBag": {"Name": "PirateBag", "Precision": 0.8},
    "Present": {"Name": "Present", "Precision": 0.8},
    "PurpleBackpack": {"Name": "PurpleBackpack", "Precision": 0.8},
    "RedBackpack": {"Name": "RedBackpack", "Precision": 0.8},
    "RedBag": {"Name": "RedBag", "Precision": 0.8},
    "ShoppingBag": {"Name": "ShoppingBag", "Precision": 0.8},
    "StampedParcel": {"Name": "StampedParcel", "Precision": 0.8},
    "YellowBackpack": {"Name": "YellowBackpack", "Precision": 0.8}
}

# Rings
Rings = {
    "AxeRing": {"Name": "AxeRing", "Precision": 0.9},
    "BrokenKeyRing": {"Name": "BrokenKeyRing", "Precision": 0.9},
    "BrokenRingOfEnding": {"Name": "BrokenRingOfEnding", "Precision": 0.9},
    "ButterflyRing": {"Name": "ButterflyRing", "Precision": 0.9},
    "ClubRing": {"Name": "ClubRing", "Precision": 0.9},
    "CrystalRing": {"Name": "CrystalRing", "Precision": 0.9},
    "DeathRing": {"Name": "DeathRing", "Precision": 0.9},
    "DwarvenRing": {"Name": "DwarvenRing", "Precision": 0.9},
    "EnergyRing": {"Name": "EnergyRing", "Precision": 0.9},
    "GoldRing": {"Name": "GoldRing", "Precision": 0.9},
    "LifeRing": {"Name": "LifeRing", "Precision": 0.9},
    "MightRing": {"Name": "MightRing", "Precision": 0.9},
    "PowerRing": {"Name": "PowerRing", "Precision": 0.9},
    "RingOfBluePlasma": {"Name": "RingOfBluePlasma", "Precision": 0.9},
    "RingOfHealing": {"Name": "RingOfHealing", "Precision": 0.9},
    "StealthRing": {"Name": "StealthRing", "Precision": 0.9},
    "SweetheartRing": {"Name": "SweetheartRing", "Precision": 0.9},
    "SwordRing": {"Name": "SwordRing", "Precision": 0.9},
    "TimeRing": {"Name": "TimeRing", "Precision": 0.9},
    "WeddingRing": {"Name": "WeddingRing", "Precision": 0.9}
}

# Amulets
Amulets = {
    "AmuletOfLoss": {"Name": "AmuletOfLoss", "Precision": 0.8},
    "AncientAmulet": {"Name": "AncientAmulet", "Precision": 0.8},
    "BronzeAmulet": {"Name": "BronzeAmulet", "Precision": 0.8},
    "ElvenAmulet": {"Name": "ElvenAmulet", "Precision": 0.8},
    "GlacierAmulet": {"Name": "GlacierAmulet", "Precision": 0.8},
    "GloothAmulet": {"Name": "GloothAmulet", "Precision": 0.8},
    "LeviathansAmulet": {"Name": "LeviathansAmulet", "Precision": 0.8},
    "MagmaAmulet": {"Name": "MagmaAmulet", "Precision": 0.8},
    "PlatinumAmulet": {"Name": "PlatinumAmulet", "Precision": 0.8},
    "ProtectionAmulet": {"Name": "ProtectionAmulet", "Precision": 0.8},
    "SacredTreeAmulet": {"Name": "SacredTreeAmulet", "Precision": 0.8},
    "ScarabAmulet": {"Name": "ScarabAmulet", "Precision": 0.8},
    "ShockwaveAmulet": {"Name": "ShockwaveAmulet", "Precision": 0.8},
    "SilverAmulet": {"Name": "SilverAmulet", "Precision": 0.8},
    "StarAmulet": {"Name": "StarAmulet", "Precision": 0.8},
    "StoneSkinAmulet": {"Name": "StoneSkinAmulet", "Precision": 0.8},
    "TerraAmulet": {"Name": "TerraAmulet", "Precision": 0.8},
    "WerewolfAmulet": {"Name": "WerewolfAmulet", "Precision": 0.8}
}

# Foods
Foods = {
    "BrownMushrooms": {"Name": "BrownMushrooms", "Precision": 0.8},
    "Cheese": {"Name": "Cheese", "Precision": 0.8},
    "Corncobs": {"Name": "Corncobs", "Precision": 0.8},
    "DeeplingFilet": {"Name": "DeeplingFilet", "Precision": 0.8},
    "FireMushrooms": {"Name": "FireMushrooms", "Precision": 0.8},
    "Fish": {"Name": "Fish", "Precision": 0.8},
    "GloothSandwichs": {"Name": "GloothSandwichs", "Precision": 0.8},
    "Grapes": {"Name": "Grapes", "Precision": 0.8},
    "GreenMushrooms": {"Name": "GreenMushrooms", "Precision": 0.8},
    "Melons": {"Name": "Melons", "Precision": 0.8},
    "OrangeMushrooms": {"Name": "OrangeMushrooms", "Precision": 0.8},
    "Peanuts": {"Name": "Peanuts", "Precision": 0.8},
    "RedMushrooms": {"Name": "RedMushrooms", "Precision": 0.8},
    "WhiteMushrooms": {"Name": "WhiteMushrooms", "Precision": 0.8}
}

# endregion

# Stats
ImageStats = []

Stats = [
    'paralyze',
    'poison',
    'fire',
    'electrify',
    'mort',
    'blood'
]

# region CaveBotRegion

# Monsters For Select To Attack On CaveBot Module
Monsters = [
    "Rat",
    "CaveRat",
    "Orc",
    "OrcWarrior",
    "OrcSpearman",
    "Cyclops",
    "Rotworm",
    "AnyCorym",
    "CorymCharlatan",
    "CorymSkirmisher",
    "CorymVanguard",
    "Stonerefiner"
]

# Hotkeys For Pause CaveBot Module
Hotkeys = [
    'Page Up'
]

AttackModes = [
    'Full Attack',
    'Balance',
    'Full Defence'
]

CavebotScriptsPath = "scripts/"

# Script's Name For Load To Walk In CaveBot Module
Scripts = [
    "ratThais",
    "StonerefinerVenore"
]

# endregion

# region DepotChests

ChestsPath = MainPath + "/Depot/Chests/"

ChestsNamesPath = ChestsPath + "Names/"
ChestsSpritesPath = ChestsPath + "Sprites/"

Chests = {
    "Chest1",
    "Chest2",
    "Chest3",
    "Chest4",
    "Chest5",
    "Chest6",
    "Chest7",
    "Chest8",
    "Chest9",
    "Chest10",
    "Chest11",
    "Chest12",
    "Chest13",
    "Chest14",
    "Chest15",
    "Chest16",
    "Chest17",
}

# endregion
