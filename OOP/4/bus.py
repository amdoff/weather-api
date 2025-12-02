import random

class Bus:
    def __init__(self):
        self.__capacity = []

    def enter_bus(self, count: int):
        if len(self.__capacity) + count > 100:
            print("BUS IS FULL")
            count = 100 - len(self.__capacity)
        for _ in range(count):
            self.__capacity.append(random.randint(1, 100))

    def exit_bus(self, count: int):
        if len(self.__capacity) == 0:
            print("BUS IS EMPTY")
            return
        if count > len(self.__capacity):
            count = len(self.__capacity)
        for _ in range(count):
            self.__capacity.pop()

    def people_count(self) -> int:
        return len(self.__capacity)
