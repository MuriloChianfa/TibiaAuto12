import pyautogui

class GetLifeStage:
    def scanning_auto_life(glife, healthX, healthY):
        if pyautogui.pixelMatchesColor(healthX + 100, healthY + 3, (110, 58, 58)):
            print("Get Life: 100")
            return 100
        elif pyautogui.pixelMatchesColor(healthX + 95, healthY + 3, (255, 125, 125)):
            print("Get Life: 95")
            return 95
        elif pyautogui.pixelMatchesColor(healthX + 90, healthY + 3, (255, 125, 125)):
            print("Get Life: 90")
            return 90
        elif pyautogui.pixelMatchesColor(healthX + 85, healthY + 3, (255, 125, 125)):
            print("Get Life: 85")
            return 85
        elif pyautogui.pixelMatchesColor(healthX + 80, healthY + 3, (255, 125, 125)):
            print("Get Life: 80")
            return 80
        elif pyautogui.pixelMatchesColor(healthX + 75, healthY + 3, (255, 125, 125)):
            print("Get Life: 75")
            return 75
        elif pyautogui.pixelMatchesColor(healthX + 70, healthY + 3, (255, 125, 125)):
            print("Get Life: 70")
            return 70
        elif pyautogui.pixelMatchesColor(healthX + 65, healthY + 3, (255, 125, 125)):
            print("Get Life: 65")
            return 65
        elif pyautogui.pixelMatchesColor(healthX + 60, healthY + 3, (255, 125, 125)):
            print("Get Life: 60")
            return 60
        elif pyautogui.pixelMatchesColor(healthX + 55, healthY + 3, (255, 125, 125)):
            print("Get Life: 55")
            return 55
        elif pyautogui.pixelMatchesColor(healthX + 50, healthY + 3, (255, 125, 125)):
            print("Get Life: 50")
            return 50
        elif pyautogui.pixelMatchesColor(healthX + 45, healthY + 3, (255, 125, 125)):
            print("Get Life: 45")
            return 45
        elif pyautogui.pixelMatchesColor(healthX + 40, healthY + 3, (255, 125, 125)):
            print("Get Life: 40")
            return 40
        elif pyautogui.pixelMatchesColor(healthX + 35, healthY + 3, (255, 125, 125)):
            print("Get Life: 35")
            return 35
        elif pyautogui.pixelMatchesColor(healthX + 30, healthY + 3, (255, 125, 125)):
            print("Get Life: 30")
            return 30
        elif pyautogui.pixelMatchesColor(healthX + 25, healthY + 3, (255, 125, 125)):
            print("Get Life: 25")
            return 25
        elif pyautogui.pixelMatchesColor(healthX + 20, healthY + 3, (255, 125, 125)):
            print("Get Life: 20")
            return 20
        elif pyautogui.pixelMatchesColor(healthX + 14, healthY + 3, (255, 125, 125)):
            print("Get Life: 15")
            return 15
        elif pyautogui.pixelMatchesColor(healthX + 10, healthY + 3, (255, 125, 125)):
            print("Get Life: 10")
            return 10
        elif pyautogui.pixelMatchesColor(healthX + 5, healthY + 3, (255, 125, 125)):
            print("Get Life: 5")
            return 5
        else:
            print("Get Life: 0")
            return 0
        
class GetManaStage:
    def scanning_auto_mana(gmana, manaLocX, manaLocY):
        if pyautogui.pixelMatchesColor(manaLocX + 100, manaLocY, (45, 45, 105)):
            print("Get Mana: 100")
            return 100
        elif pyautogui.pixelMatchesColor(manaLocX + 95, manaLocY, (83, 80, 218)):
            print("Get Mana: 95")
            return 95
        elif pyautogui.pixelMatchesColor(manaLocX + 90, manaLocY, (83, 80, 218)):
            print("Get Mana: 90")
            return 90
        elif pyautogui.pixelMatchesColor(manaLocX + 85, manaLocY, (83, 80, 218)):
            print("Get Mana: 85")
            return 85
        elif pyautogui.pixelMatchesColor(manaLocX + 80, manaLocY, (83, 80, 218)):
            print("Get Mana: 80")
            return 80
        elif pyautogui.pixelMatchesColor(manaLocX + 75, manaLocY, (83, 80, 218)):
            print("Get Mana: 75")
            return 75
        elif pyautogui.pixelMatchesColor(manaLocX + 70, manaLocY, (83, 80, 218)):
            print("Get Mana: 70")
            return 70
        elif pyautogui.pixelMatchesColor(manaLocX + 65, manaLocY, (83, 80, 218)):
            print("Get Mana: 65")
            return 65
        elif pyautogui.pixelMatchesColor(manaLocX + 60, manaLocY, (83, 80, 218)):
            print("Get Mana: 60")
            return 60
        elif pyautogui.pixelMatchesColor(manaLocX + 55, manaLocY, (83, 80, 218)):
            print("Get Mana: 55")
            return 55
        elif pyautogui.pixelMatchesColor(manaLocX + 50, manaLocY, (83, 80, 218)):
            print("Get Mana: 50")
            return 50
        elif pyautogui.pixelMatchesColor(manaLocX + 45, manaLocY, (83, 80, 218)):
            print("Get Mana: 45")
            return 45
        elif pyautogui.pixelMatchesColor(manaLocX + 40, manaLocY, (83, 80, 218)):
            print("Get Mana: 40")
            return 40
        elif pyautogui.pixelMatchesColor(manaLocX + 35, manaLocY, (83, 80, 218)):
            print("Get Mana: 35")
            return 35
        elif pyautogui.pixelMatchesColor(manaLocX + 30, manaLocY, (83, 80, 218)):
            print("Get Mana: 30")
            return 30
        elif pyautogui.pixelMatchesColor(manaLocX + 25, manaLocY, (83, 80, 218)):
            print("Get Mana: 25")
            return 25
        elif pyautogui.pixelMatchesColor(manaLocX + 20, manaLocY, (83, 80, 218)):
            print("Get Mana: 20")
            return 20
        elif pyautogui.pixelMatchesColor(manaLocX + 14, manaLocY, (83, 80, 218)):
            print("Get Mana: 15")
            return 15
        elif pyautogui.pixelMatchesColor(manaLocX + 10, manaLocY, (83, 80, 218)):
            print("Get Mana: 10")
            return 10
        elif pyautogui.pixelMatchesColor(manaLocX + 5, manaLocY, (83, 80, 218)):
            print("Get Mana: 5")
            return 5
        else:
            print("Get Mana: 0")
            return 0

