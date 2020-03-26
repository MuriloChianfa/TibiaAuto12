import pyautogui
import time

class GetLoot:
    def take_loot(log, SQM1_X, SQM1_Y, SQM2_X, SQM2_Y, SQM3_X, SQM3_Y,
                    SQM4_X, SQM4_Y, SQM5_X, SQM5_Y, SQM6_X, SQM6_Y,
                    SQM7_X, SQM7_Y, SQM8_X, SQM8_Y, SQM9_X, SQM9_Y):
        defaul_autogui_temp = pyautogui.PAUSE
        start_loot_time = time.time()
        pyautogui.PAUSE = 0.09
        pyautogui.click(SQM1_X, SQM1_Y, button='right')
        pyautogui.click(SQM2_X, SQM2_Y, button='right')
        pyautogui.click(SQM3_X, SQM3_Y, button='right')
        pyautogui.click(SQM4_X, SQM4_Y, button='right')
        pyautogui.click(SQM5_X, SQM5_Y, button='right')
        pyautogui.click(SQM6_X, SQM6_Y, button='right')
        pyautogui.click(SQM7_X, SQM7_Y, button='right')
        pyautogui.click(SQM8_X, SQM8_Y, button='right')
        pyautogui.click(SQM9_X, SQM9_Y, button='right')
        end_loot_time = time.time() - start_loot_time
        pyautogui.PAUSE = defaul_autogui_temp
        print("Looted In: ", end_loot_time)