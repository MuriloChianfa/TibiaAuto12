ComponentsForEnable = []
ComponentsForDisable = []


def Enable(Component):
    ComponentsForEnable.append(Component)


def Disable(Component):
    ComponentsForDisable.append(Component)


def ComponentsToDisable():
    for f in range(len(ComponentsForDisable)):
        ComponentsForDisable[f].configure(state='disabled')


def ComponentsToEnable():
    for f in range(len(ComponentsForEnable)):
        ComponentsForEnable[f].configure(state='normal')


def ExecGUITrigger():
    ComponentsToEnable()
    ComponentsToDisable()
    global ComponentsForDisable, ComponentsForEnable
    ComponentsForDisable = []
    ComponentsForEnable = []
