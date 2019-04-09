from threading import Thread as T
import threading as H
from time import sleep as S

def NatNumber():
    print(H.current_thread().getName(), " Started\n")
    S(2)
    for x in range(11):
        print(x)
    print(H.current_thread().getName(), " Ended\n")


t1 = T(target=NatNumber)
t2 = T(target=NatNumber)
t1.start()
t2.start()
