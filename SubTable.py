'''
start = int(input('Please enter the first num: '))
end = int(input('Please enter the end num: '))

for num in range(start, end+1):
   for value in range(1,13):
       result = num*value
       print(f'{value} x {num} = {result}')
   print('----------')
'''
'''
word = input('Enter a word: ')
letters = []
for letter in word:
    if letter in letters:
        continue
    else:
        letters.append(letter)
print(letters)
'''
class Game:
    def __init__(self):
        
        print('Welcom In Our Game')
        print('''
            Press the game number:
                1) Multiplication table.
                2) Remove dublicated chars.
                ''')
        user_choice = int(input('Enter your choice number: '))

g = Game()
