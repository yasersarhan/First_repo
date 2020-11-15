file = open('Test_File.txt', 'r')
words = file.readlines()
print(words)

file.close()

file = open('Test2_File.txt', 'w')
print(file.write('Welcome in python world'))
file.close()

file = open('Test2_File.txt', 'w')
print(file.write('Mona yaser sarhan'))
file.close()
