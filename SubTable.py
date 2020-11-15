'''
start = int(input('Please enter the first num: '))
end = int(input('Please enter the end num: '))

for num in range(start, end+1):
   for value in range(1,13):
       result = num*value
       print(f'{value} x {num} = {result}')
   print('----------')
'''
word = input('Enter a word: ')
letters = []
for letter in word:
    if letter in letters:
        continue
    letters.append(letter)
print(letters)
