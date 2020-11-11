class Calc:
    def __init__(self, name):
        print(f'Welcome {name}')


class ScientificCalc(Calc):
    def __init__(self, name):
        super(ScientificCalc, self).__init__(name)
        print('Hello yaser')
    def sum(self, x, y):
        print(x + y)


num = ScientificCalc('yaser')
num.sum(34, 54)
