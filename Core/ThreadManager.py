import threading
from queue import Queue

ThreadsStarted = []
Queue = Queue(maxsize=19)


class ThreadManager:
    def __init__(self, ThreadName):
        self.ThreadName = ThreadName

    def StartNewThread(self, Target):
        NewThread = threading.Thread(target=Target)
        NewThread.start()
        ThreadsStarted.append((NewThread, str(self.ThreadName)))


def ThreadsActives():
    ActivatedThreads = []
    for i in range(len(ThreadsStarted)):
        if ThreadsStarted[i][0].is_alive():
            print(f"Thread [{ThreadsStarted[i][1]}] Is Activated")
            ActivatedThreads.append(ThreadsStarted[i][0])
    return ActivatedThreads


def NumberOfLiveThreads():
    print(len(ThreadsStarted), "Threads Actives")
    return len(ThreadsStarted)


