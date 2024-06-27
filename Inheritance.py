class Car:
    def __init__(self,windows,doors,engine):
        self.windows=windows
        self.doors=doors
        self.engine=engine

    def driving(self):
        print("Car is used for driving")
    

#Audi  Car is inherting from car class
class Audi(Car):
    def __init__(self,windows,doors,engine,horsepower):
        super().__init__(windows,doors,engine)
        self.horsepower=horsepower
    
    def self_driving(self):
        print("It is a self driving car.")
    
audiq7 =Audi(4,5,"Diesel",200)

print(audiq7.windows)
print(audiq7.doors)
print(audiq7.engine)
print(audiq7.horsepower)

audiq7.driving()
audiq7.self_driving()