import threading as T

t = T.current_thread().getName()
if T.current_thread() == T.main_thread():
    for x in range(10):
        if x % 2 == 0:
            print(x)
else:
    print("Not Main")
print(t)

t = T.current_thread().name = "MJ"
print(t)
