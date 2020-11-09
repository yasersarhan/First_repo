tup1 = ('html', 'css', 'javascript', 'python', 'Django')
print(tup1)

print(tup1[2:])

tup2 = ('visual basic', 'C#', 'C++')
print(tup2)

tup3 = tup1 + tup2
print(tup3)

del tup2
print(tup3)

print(tup1[2:])
list1 = list(tup1)
print(list1)

dict1 = {'Name' : 'yaser sarhan', 'Age' : 37 , 'Job' : 'Accountant'}
print(dict1)
print(dict1['Name'], dict1['Age'])
dict1['Job'] = 'Developer'
print(dict1['Job'])

dict1['School'] = 'Yas School'
print(dict1['School'])
print(dict1)

f = dict1.copy()
print(f)

print(dict1.get('Name'))
print(dict1.items())

print(f.keys())
print(f.values())

d = {'gender' : 'male'}
print(d)

d.update(f)
print(d)

x = {1: 'Arabic', 2: 'English', 3: 'History'}




