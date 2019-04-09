# # To target one function
from threading import Thread as T
import threading as H


def even():
    for x in range(21):
        if x % 2 is 0:
            print(x)
    # to rename the thread
    th = H.current_thread().name = "EvenThread"
    print(th)


a = H.current_thread().getName()
print(a)
t = T(target=even)

# Start the thread
t.start()
