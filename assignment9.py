import math

class MyMathModule:
    def __init__(self, num):
        self.num= num
    
    def square(self):
        return self.num ** 2
    
    def square_root(self):
        return math.sqrt(self.num)
    
    def factorial(self):
        return math.factorial(self.num)
    
    def logarithm(self):
        return math.log(self.num)
    
    def ceil(self):
        return math.ceil(self.num)
    
class MyException(Exception):
    def _init_(self, message):
        self.message = message

    def msg(self):
        return self.message