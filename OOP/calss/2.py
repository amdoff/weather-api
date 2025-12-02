class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1  
        self.num2 = num2 

    def sum(self):
        result = self.num1 + self.num2
        print(f"{self.num1} + {self.num2} = {result}")

    def mul(self):
        result = self.num1 * self.num2
        print(f"{self.num1} * {self.num2} = {result}")

    def div(self):
        if self.num2 != 0: 
            result = self.num1 / self.num2
            print(f"{self.num1} / {self.num2} = {result}")
        else:
            print("Nolga bo'lish mumkin emas!")

    def sub(self):
        result = self.num1 - self.num2
        print(f"{self.num1} - {self.num2} = {result}")

calc = Calculator(10, 5)

calc.sum()   
calc.mul()  
calc.div()   
calc.sub() 