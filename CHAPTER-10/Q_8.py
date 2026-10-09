class Train:

    stations = {
        "BBSR": {"seats": 25, "fare": 300},
        "KATAK": {"seats": 10, "fare": 200},
        "JK": {"seats": 0, "fare": 500},
        "PURI": {"seats": 15, "fare": 400}}
    def ticketbooking(self):
        station = input("Enter the station you want to travel to: ").upper()
        if station not in self.stations:
            print("Station not found")
        elif self.stations[station]["seats"] == 0:
            print("Sorry, no seats are available for", station)
        else:
            self.stations[station]["seats"] -= 1
            print("Ticket booked successfully for", station)
            print("Fare: ₹", self.stations[station]["fare"])
    def seatstatus(self):
        station = input("Enter the station: ").upper()
        if station in self.stations:
            print("Seats available:", self.stations[station]["seats"])
        else:
            print("Station not found")
    def fareinfo(self):
        station = input("Enter the station: ").upper()
        if station in self.stations:
            print("Fare for", station, ": ₹", self.stations[station]["fare"])
        else:
            print("Station not found")
train = Train()
train.ticketbooking()
train.seatstatus()
train.fareinfo()
  
   