from threading import *

class Flight:
    def __init__(self, ReaminingTickets):
        self.ReaminingTickets=ReaminingTickets

    def ticketBuy(self, OrderedTickets):
        if self.ReaminingTickets >= OrderedTickets:
            print("Purchase Confirmed")
            print("Print your tickets\n")
            self.ReaminingTickets -= OrderedTickets
        else:
            print("Sorry we ran out of tickets\n")


order=Flight(10)
t1=Thread(target=order.ticketBuy,args=[4])
t2=Thread(target=order.ticketBuy,args=[4])
t3=Thread(target=order.ticketBuy,args=[4])
t1.start()
t2.start()
t3.start()
