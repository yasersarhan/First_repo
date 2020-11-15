class Main:
    def __init__(self, age):
        print(f'your age is {age}')

    def mul(self, x, y):
        print(x * y)


class Calc(Main):
    def __init__(self, name):
        print(f'Welcome {name}')


class ScientificCalc(Calc):
    def __init__(self, name):
        super().__init__(name)
        print('Hello yaser')

    def sum(self, x, y):
        print(x + y)


num = ScientificCalc('yaser')
num.sum(34, 54)
print(ScientificCalc.mro())
