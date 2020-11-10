class Calculator():

    def sum (self,x,y):
        print(self)
        #print(x+y)

    def mul (self,x,y):
        print(x*y)


my_calc = Calculator()
print(my_calc)
my_calc.sum(4,5)
#my_calc.mul(3,8)

your_calc = Calculator()
print(your_calc)
your_calc.sum(8,9)


