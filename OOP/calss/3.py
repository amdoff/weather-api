class MinutConverter:
    def __init__(self,minutes):
        self.minutes = minutes
        
    def toHours(self):
       Hours = self.minutes / 60
       print(f"{self.minutes}minut = {Hours} soat")

    def toSeconds(self):
       seconds = self.minutes * 60
       print(f"{self.minutes}minut = {seconds} sekund")
    
    def toDay(self):
        Days = self.minutes / (60 * 24)
        print(f"{self.minutes} minut = {Days}kun")

minutes =1000000
converter = MinutConverter(minutes)

converter.toHours()
converter.toSeconds()
converter.toDay()