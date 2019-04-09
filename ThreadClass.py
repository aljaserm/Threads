from threading import Thread as T
import threading as H


class myThread():
    def natNumbers(self):
        if H.current_thread().getName() == "Thread-1":
            for x in range(10):
                print(x)
        else:
            print("Not Thread-1")


nat = myThread()
t=T(target=nat.natNumbers)
t.start()
