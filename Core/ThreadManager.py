from threading import Event, Thread
from queue import Queue

ActivatedThreads = []
Queue = Queue(maxsize=19)
Event = Event()

'''
    This Class Has Been Rewritten So That We Can Pause The Modules Enabled,
    In Original Class, Its Not Possible, There He Had To Keep Creating New Threads
    And That, Overloads The System.
    
    Example For Usage:
    
    # Import The Module Fist
    from Core.ThreadManager import ThreadManager
    
    # And Create The Instance
    ThreadManager = ThreadManager("NameOfYourThread")
    
    # For Start The New Thread
    ThreadManager.NewThread(TargetFunctionHere) [DOES NOT ACCEPT ARGUMENTS YET]
    
    # For Pause All Threads
    ThreadManager.PauseThread()
    
    # For UnPause All Threads
    ThreadManager.UnPauseThread()
    
    #
    # The Kill Threads Functions Not Ready Yet !!! Sorry
    #
'''


class ThreadManager:
    def __init__(self, Name):
        self.Name = Name
        self.Queue = Queue
        self.Target = None

    # Create One New Thread And Put Them In The Pipeline
    def NewThread(self, _Target):
        # The Handle Need The 1st Arg to Work..
        def HandleTarget(PipeOBJ):
            # print(f"PipeObject: {PipeOBJ}")
            _Target()

        self.Target = Pipeline(HandleTarget)
        self.Queue.put(self.Target)
        Event.set()
        TheThread = self.ThreadHandler(Target=self.Target, Qqueue=Queue, Name=self.Name)

        TheThread.start()
        ActivatedThreads.append((TheThread, str(self.Name)))

    # Pause The All Threads Created From Manager Object
    def PauseThread(self):
        for i in range(len(ActivatedThreads)):
            if ActivatedThreads[i][1] == self.Name:
                ActivatedThreads[i][0].PauseOn()
        # print(self.Queue.queue)

    # UnPause The All Threads Created From Manager Object
    def UnPauseThread(self):
        for i in range(len(ActivatedThreads)):
            if ActivatedThreads[i][1] == self.Name:
                ActivatedThreads[i][0].PauseOff()

    # This Function Is Not Ready To Use !!!
    def KillThread(self):
        for i in range(len(ActivatedThreads)):
            if ActivatedThreads[i][1] == self.Name:
                ActivatedThreads.remove(ActivatedThreads[i])
        Queue.put('Kill')
        # print(f"{self.Name} Killed")

    def __repr__(self) -> str:
        return str(self.Name)

    '''
        This Is Thread Class Rewrited, To Can Pause Them.
    '''

    class ThreadHandler(Thread):
        def __init__(self, Target, Qqueue, *, Name='Handler'):
            super().__init__()
            self.Name = Name
            self.Queue = Qqueue
            self._target = Target
            self._stoped = False
            # print(self.Name, "Created")

        def run(self):
            # Event.wait()
            while not self.Queue.empty():
                SelectedThread = self.Queue.get()
                # print(self.Name, "Pipeline To Handle:",SelectedThread)
                if SelectedThread == 'Kill':
                    self.Queue.put(SelectedThread)
                    self._stoped = True
                    # self.Queue.pop(-1)
                    break
                self._target(SelectedThread)

        def PauseOn(self):
            self._stoped = False

        def PauseOff(self):
            self._stoped = True

        def __repr__(self) -> str:
            return str(self.Name)


def Pipeline(*funcs):
    def Inner(argument):
        state = argument
        for func in funcs:
            state = func(state)
    return Inner
