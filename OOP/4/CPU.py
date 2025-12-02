class CPU:
    def __init__(self, op1: int, op2: int):
        self.__operand_one = op1
        self.__operand_two = op2

    def change_operand_one(self, val: int):
        self.__operand_one = val

    def change_operand_two(self, val: int):
        self.__operand_two = val

    def __sum(self) -> int:
        return self.__operand_one + self.__operand_two

    def __sub(self) -> int:
        return self.__operand_one - self.__operand_two

    def __mult(self) -> int:
        return self.__operand_one * self.__operand_two

    def __div(self) -> float:
        if self.__operand_two == 0:
            return float("inf")  
        return self.__operand_one / self.__operand_two

    def calculate(self, operation: str):
        if operation == "+":
            return self.__sum()
        elif operation == "-":
            return self.__sub()
        elif operation == "*":
            return self.__mult()
        elif operation == "/":
            return self.__div()
        else:
            return "Invalid operation"
