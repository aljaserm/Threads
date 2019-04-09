from threading import Thread as T
import threading as H

# inhirt the Thread Class
class myThread(T):
    def run(self):
        print("Egyptian Pyramid")
        print(H.current_thread().getName())
        for x in range(0, 5):
            for j in range(0, x + 1):
                print("*", end=" ")
            print("\r")


draw = myThread()
draw.start()

draw.run()