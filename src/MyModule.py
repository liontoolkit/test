class MyModule:
    def __init__(self):
        self.number1 = 1
        self.number2 = 2

    def my_function(self,num1=None,num2=None):
        if num1 is None: num1 = self.number1
        if num2 is None: num2 = self.number2
        return num1 + num2
