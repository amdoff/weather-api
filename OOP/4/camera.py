class Camera:
    def __init__(self, model: str, memory: int, mb_per_min: int):
        self.__model = model
        self.__memory = memory * 1024  
        self.__mb_per_min = mb_per_min
        self.__used_memory = 0

    def get_model(self) -> str:
        return self.__model

    def capture(self, mins: int) -> int:
        size = mins * self.__mb_per_min
        if self.__used_memory + size <= self.__memory:
            self.__used_memory += size
            return 0
        else:
            excess = (self.__used_memory + size) - self.__memory
            self.__used_memory = self.__memory  
            return excess

    def delete(self, mins: int):
        size = mins * self.__mb_per_min
        self.__used_memory = max(0, self.__used_memory - size)
