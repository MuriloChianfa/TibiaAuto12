import pyautogui
import time


class GetLoot:
    def __init__(self, button):
        self.pass_mouse_position = 0
        self.start_loot_time = 0
        self.end_loot_time = 0
        self.button = button

    def TakeLoot(self, SQMs):
        self.pass_mouse_position = pyautogui.position()
        self.start_loot_time = time.time()
        for i, j in zip(range(0, 18, + 2), range(1, 19, + 2)):
            pyautogui.click(SQMs[i], SQMs[j], button=self.button)
        self.end_loot_time = time.time() - self.start_loot_time
        pyautogui.moveTo(self.pass_mouse_position)
        print("Looted In: ", self.end_loot_time)

