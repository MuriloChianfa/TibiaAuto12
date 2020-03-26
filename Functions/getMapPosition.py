import pyautogui


WAYPOINTS = [
    {
        "mark": "CheckMark",
        "type": "stand"
    },
    {
        "mark": "QuestionMark",
        "type": "stand"
    },
    {
        "mark": "ExclimationMark",
        "type": "stand"
    },
    {
        "mark": "Star",
        "type": "stand"
    },
    {
        "mark": "Cross",
        "type": "stand"
    },
    {
        "mark": "Church",
        "type": "stand"
    },
    {
        "mark": "Mouth",
        "type": "stand"
    },
    {
        "mark": "ArrowUp",
        "type": "stand"
    },
    {
        "mark": "ArrowDown",
        "type": "stand"
    },
    {
        "mark": "ArrowLeft",
        "type": "stand"
    },
    {
        "mark": "ArrowRight",
        "type": "stand"
    },
    {
        "mark": "Above",
        "type": "stand"
    },
    {
        "mark": "Bellow",
        "type": "stand"
    },
    {
        "mark": "Flag",
        "type": "stand"
    },
    {
        "mark": "Lock",
        "type": "stand"
    },
    {
        "mark": "Sword",
        "type": "stand"
    },
    {
        "mark": "Shovel",
        "type": "stand"
    },
    {
        "mark": "Bag",
        "type": "stand"
    },
    {
        "mark": "Skull",
        "type": "stand"
    },
    {
        "mark": "Money",
        "type": "stand"
    },
]


class GetMapPosition:
    def __init__(self):
        self.map_start = None
        self.map_end = None

    def get_map_xy(self):
        top_right = pyautogui.locateOnScreen("images/MapSettings/MapSettings.png", confidence=0.8)
        map_size = 110  # 110px square
        self.map_start = top_right[0] - map_size, top_right[1]
        self.map_end = top_right[0], top_right[1] + map_size
        if top_right[0] != -1:
            return self.map_start[0], self.map_start[1], self.map_end[0], self.map_end[1]
        return -1, -1, -1, -1

