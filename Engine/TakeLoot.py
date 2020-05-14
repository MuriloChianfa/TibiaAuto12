import pyautogui
import time

from Conf.Hotkeys import Hotkey


class GetLoot:
    def __init__(self, button, MOUSE_OPTION):
        self.MOUSE_OPTION = MOUSE_OPTION
        self.SendToClient = Hotkey(MOUSE_OPTION)
        self.button = button

    def TakeLoot(self, SQMs):
        if self.button == 'right':
            if self.MOUSE_OPTION == 1:
                pass_mouse_position = self.SendToClient.Position()
            else:
                pass_mouse_position = [0, 0]
            start_loot_time = time.time()
            for i, j in zip(range(0, 18, + 2), range(1, 19, + 2)):
                self.SendToClient.RightClick(SQMs[i], SQMs[j])
            end_loot_time = time.time() - start_loot_time
            if self.MOUSE_OPTION == 1:
                self.SendToClient.MoveTo(pass_mouse_position[0], pass_mouse_position[1])
            print("Looted In: ", end_loot_time)
        elif self.button == 'left':
            if self.MOUSE_OPTION == 1:
                pass_mouse_position = self.SendToClient.Position()
            else:
                pass_mouse_position = [0, 0]
            start_loot_time = time.time()
            for i, j in zip(range(0, 18, + 2), range(1, 19, + 2)):
                self.SendToClient.LeftClick(SQMs[i], SQMs[j])
            end_loot_time = time.time() - start_loot_time
            if self.MOUSE_OPTION == 1:
                self.SendToClient.MoveTo(pass_mouse_position[0], pass_mouse_position[1])
            print("Looted In: ", end_loot_time)

