import subprocess

CLIENT_IDENTIFIER = "T" + "ib" + "ia - "


def Execute(cmd):
    output, _ = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()

    return output.decode("utf8")


def kill():
    return Execute(["killall", "client"])


def FindAnotherWindow():
    output = Execute(["xdotool", "getactivewindow"])
    lines = output.split("\n")
    Windows = list(filter(lambda line: line != "", lines))

    if len(Windows) < 1:
        raise Exception("No foreground window found.")
    else:
        input("Foreground window obtained. Press enter to continue.")
        return Windows[0]


def FindWindow():
    output = Execute(
        ["xdotool", "search", "--name", CLIENT_IDENTIFIER]
    )
    lines = output.split("\n")
    Windows = list(filter(lambda line: line != "", lines))

    if len(Windows) < 1:
        raise Exception("No client found.")
    elif len(Windows) > 1:
        print(lines)
        raise Exception("Too many clients found.")
    else:
        return Windows[0]
