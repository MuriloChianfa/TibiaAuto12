from core.LinuxClient import Execute, FindAnotherWindow, FindWindow


class MoveLinuxMouse:
    def __init__(self):
        self.AnotherWindow = FindAnotherWindow()
        self.Window = FindWindow()

    def Position(self):
        location = Execute(["xdotool", "getmouselocation", "--shell"])
        lines = location.split("\n")
        x, y, window = lines[0], lines[1], lines[3]

        x = x.replace("X=", "")
        y = y.replace("Y=", "")
        window = window.replace("WINDOW=", "")

        return (int(x), int(y), window)

    def RightClick(self, X, Y):
        return self.Click(X, Y, click_type=3)

    def Click(self, X, Y, click_type=1):
        current_x, current_y, _ = self.Position()

        Execute(
            [
                "xdotool",
                "mousemove",
                "--window",
                self.Window,
                str(X),
                str(Y),
                "click",
                "--window",
                self.Window,
                str(click_type),
                "mousemove",
                str(current_x),
                str(current_y),
            ]
        )

    def DragTo(self, FromX, FromY, ToX, ToY):
        current_x, current_y, _ = self.Position()

        Execute(
            [
                "xdotool",
                "mousemove",
                "--window",
                self.Window,
                str(FromX),
                str(FromY),
                "mousedown",
                "--window",
                self.Window,
                "1",
                "mousemove",
                "--window",
                self.Window,
                str(ToX),
                str(ToY),
                "mouseup",
                "--window",
                self.Window,
                "1",
                "mousemove",
                str(current_x),
                str(current_y),
            ]
        )

    def MoveMouse(self, X, Y):
        Execute(
            ["xdotool", "mousemove", "--window", self.Window, str(X), str(Y), ]
        )

    def Press(self, key):
        Execute(["xdotool", "key", "--window", self.Window, key])

    def KeyDown(self, key):
        Execute(["xdotool", "keydown", key])

    def KeyUp(self, key):
        Execute(["xdotool", "keyup", key])
