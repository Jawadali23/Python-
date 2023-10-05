class Train:
    def __init__(self,name,fare,seats):
        self.name= name
        self.fare = fare
        self.seats = seats
    
    def getStatus(self):
        print('**********')
        print(f"The name of the Trian is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print('*********')

    def fareInfo(self):
        print(f"The price of the Ticket is: Rs {self.fare}")

    def bookticket(self):
        if (self.seats >0):
            print(f"Your Ticket has been booked! Your seat number is {self.seats}")
            self.seats =self.seats -1
        else:
            print('Sorry this train is full! kindly try in another')

        def cancelTicket(self,seatNo):
            pass

intercity = Train("Green Express: 4525",1500,2)
intercity.getStatus()
intercity.bookticket()
intercity.bookticket()
intercity.bookticket()
intercity.getStatus()
    
        
