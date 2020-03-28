import pyautogui
import time
from Functions.getPlayerPosition import *


class SetSQMs:
    def __init__(self):
        self.SQMs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.Player = [0, 0]
        self.gameWindow = [0, 0, 0, 0]
        self.horizontal_SQM_size = 0
        self.vertical_SQM_size = 0

    def set_SQMs(self):
        if self.gameWindow[0] and self.gameWindow[1] != 0:
            self.horizontal_SQM_size = int((self.gameWindow[2] - self.gameWindow[0]) / 15)
            print("Size of Your Horizontal SQM:", self.horizontal_SQM_size)
            self.vertical_SQM_size = int((self.gameWindow[3] - self.gameWindow[1]) / 11)
            print("Size of Your Vertical SQM:", self.vertical_SQM_size)
        else:
            print("Setting Window Size...")
            self.Player[0], self.Player[1], self.gameWindow[0], self.gameWindow[1], self.gameWindow[2], self.gameWindow[
                3] = GetPlayerPosition().get_gw_xy()
            self.set_SQMs()

        if self.Player[0] and self.Player[1] != 0 and self.horizontal_SQM_size and self.vertical_SQM_size != 0:
            self.SQMs[0] = self.Player[0] - self.horizontal_SQM_size
            self.SQMs[1] = self.Player[1] + self.vertical_SQM_size
            self.SQMs[2] = self.Player[0]
            self.SQMs[3] = self.Player[1] + self.vertical_SQM_size
            self.SQMs[4] = self.Player[0] + self.horizontal_SQM_size
            self.SQMs[5] = self.Player[1] + self.vertical_SQM_size
            self.SQMs[6] = self.Player[0] - self.horizontal_SQM_size
            self.SQMs[7] = self.Player[1]
            self.SQMs[8] = self.Player[0]
            self.SQMs[9] = self.Player[1]
            self.SQMs[10] = self.Player[0] + self.horizontal_SQM_size
            self.SQMs[11] = self.Player[1]
            self.SQMs[12] = self.Player[0] - self.horizontal_SQM_size
            self.SQMs[13] = self.Player[1] - self.vertical_SQM_size
            self.SQMs[14] = self.Player[0]
            self.SQMs[15] = self.Player[1] - self.vertical_SQM_size
            self.SQMs[16] = self.Player[0] + self.horizontal_SQM_size
            self.SQMs[17] = self.Player[1] - self.vertical_SQM_size
            return self.SQMs[0], self.SQMs[1], self.SQMs[2], self.SQMs[3], self.SQMs[4], self.SQMs[5], self.SQMs[6], \
                   self.SQMs[7], self.SQMs[8], self.SQMs[9], self.SQMs[10], self.SQMs[11], self.SQMs[12], self.SQMs[13], \
                   self.SQMs[14], self.SQMs[15], self.SQMs[16], self.SQMs[17]
        else:
            print("Setting Player Position...")
            self.Player[0], self.Player[1], self.gameWindow[0], self.gameWindow[1], self.gameWindow[2], self.gameWindow[
                3] = GetPlayerPosition().get_gw_xy()
            self.set_SQMs()
