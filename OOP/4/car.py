class Car:
    def __init__(self, model: str, fuel: int):
        self.__model = model
        self.__fuel = fuel
        self.__state = False  
    def get_model(self) -> str:
        return self.__model

    def get_fuel(self) -> int:
        return self.__fuel

    def is_on(self) -> bool:
        return self.__state

    def add_fuel(self, fuel: int):
        self.__fuel += fuel

    def change_state(self):
        if self.__fuel > 0:
            self.__state = not self.__state
        else:
            print("Cannot start the car. Fuel is empty.")

    def drive(self, km: int):
        if not self.__state:
            print("Car is off. Cannot drive.")
            return
        if self.__fuel == 0:
            print("Out of fuel!")
            self.__state = False
            return
        if km > self.__fuel:
            print(f"Only drove {self.__fuel} km before stopping. Out of fuel!")
            self.__fuel = 0
            self.__state = False
        else:
            self.__fuel -= km