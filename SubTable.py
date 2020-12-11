class Game:

    def __init__(self):

        print('Welcome In Our Game')
        print('''
            Press the game number:
                1) Multiplication table.
                2) Remove duplicated chars.
                ''')

        user_choice = int(input('Enter your choice number: '))

        if user_choice == 1:
            self.multiplacation_table()
        elif user_choice == 2:
            self.remove_duplicates()
        else:
            print('Please Enter A Valid Number')

    def multiplacation_table(self):

        start = int(input('Please enter the first num: '))
        end = int(input('Please enter the end num: '))

        for num in range(start, end + 1):
            for value in range(1, 13):
                result = num * value
                print(f'{value} x {num} = {result}')
            print('----------')

    def remove_duplicates(self):
        word = input('Enter a word: ')
        letters = []
        for letter in word:
            if letter in letters:
                continue
            else:
                letters.append(letter)
        print(letters)


g = Game()
