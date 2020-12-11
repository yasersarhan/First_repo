#First Question:

num1 = int(input('Enter the first num:'))
num2 = int(input('Enter the second num:'))

for x in range(num1, num2+1):
    print(x)

#Second Question:

num1 = int(input('Enter your num:'))
num2 = 50
if num1 < 20:
    while num1 <= num2:
        print(num1)
        num1 += 3
else:
    while num1 <= num2:
        print(num1)
        num1 += 2

print('Thank you')

