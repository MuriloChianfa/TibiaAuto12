import threading
from multiprocessing import Process

ActiveThreads = {}


class ThreadManager:
    def __init__(self, ThreadName):
        self.ThreadName = ThreadName
        self.Thread = None

    def NewThread(self, fn):
        global ActiveThreads
        self.Thread = MyThread(fn)
        target = self.Thread.start()
        ActiveThreads[self.ThreadName] = self.Thread

    def StopThread(self):
        ActiveThreads[self.ThreadName].stop()
        ActiveThreads.pop(self.ThreadName)


class MyThread(threading.Thread):
    def __init__(self, target):
        super(MyThread, self).__init__(group=None, target=target, daemon=True)
        self.target = target
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        while True:
            if self.stopped():
                return
            self.target()
