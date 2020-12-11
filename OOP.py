class Main_calc():
    def __init__(self):
        print('welcome in our calculator')
    def sum (self,x,y):
        print(x+y)
    

class Calculator():
    def mul (self,x,y):
        print(x*y)

class Scientific(Calculator, Main_calc):
    def power(self,x,y):
       print(x**y)

x = Scientific()
x.sum(44,56)

    

