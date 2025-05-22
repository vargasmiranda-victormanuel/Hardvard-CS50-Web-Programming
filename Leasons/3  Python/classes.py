class Point():
    def __init__(self, x1, y2):
        self.x = x1
        self.y = y2


p = Point(2,30)

print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seat():
            return False
        self.passengers.append(name)
        return True
    
    def open_seat(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people =["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person}")
    else:
        print(f"Not available seats for {person}")