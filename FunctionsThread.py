# To target multiple functions
from threading import Thread as T
import threading as H


def evenOdd():
    even()
    odd()
    name=H.current_thread().getName()
    print(name)

    # to rename the thread
    th = H.current_thread().name = "Inner Even and Odd Thread"
    print(th)


def even():
    print("Evens: \n")
    for x in range(21):
        if x % 2 is 0:
            print(x)
    print("\n")
    print(H.current_thread().getName())


def odd():
    print("Odds: \n")
    for x in range(21):
        if x % 2 is not 0:
            print(x)
    print("\n")
    print(H.current_thread().getName())


a = H.current_thread().getName()
mainName=H.current_thread().name="Even and Odd Thread"
print(a)

t = T(target=evenOdd)
print(mainName)
# Start the thread
t.start()
