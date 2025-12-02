class SpaceAircraft:
    def __init__(self, model, height, fuel):
        self.model = model          
        self.height = height        
        self.fuel = fuel           

    def launch(self, km):  
        if self.fuel >= km:
            self.fuel -= km
            print(f"{self.model} uchish uchun {km} km yoqilg'i sarfladi. Yoqilg'i miqdori: {self.fuel} litrdan.")
        else:
            print("Yoqilg'i yetarli emas!")

    def land(self, km):
        if self.fuel >= km:
            self.fuel -= km
            print(f"{self.model} {km} km masofaga qo'ndi. Yoqilg'i miqdori: {self.fuel} litrdan.")
        else:
            print("No fuel")

spacecraft = SpaceAircraft("Space Shuttle", 1000, 500)
spacecraft.launch(200)
spacecraft.land(100)
spacecraft.launch(200)
spacecraft.land(400)
