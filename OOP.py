class Calculator():
    def __init__(self):
        print('welcome in our calculator')

    def sum (self,x,y):
        print(x+y)

    def mul (self,x,y):
        print(x*y)


my_calc = Calculator()
my_calc.sum(4,5)

class Scientific(Calculator):
    def power(self,x,y):
       print(x**y)

    def divison(slef,x,y):
       print(x/y)

    def sub(self,x,y):
        print(x-y)

x = Scientific()
x.sum(1,1)

    

