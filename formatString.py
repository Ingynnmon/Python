#week 5A 26.9.2019
animals = { 'Tiger' : 3000,
			'Lion ' : 3822,
			'Leopard': 400
		  }

for animal, amount in animals.items():
	print(f'{animal:1} ==> {amount:1d}')

#
bird = 'sparrow'

print(f'My plane hits {bird} over the cloud.')
print(f'{bird} {bird} My plane hits {bird!r} over the cloud.')

#The string format
x = 'Hey'
print('{}, {} are the {} who say "{}!"'.format(x, 'We', 'Knights', 'Nee'))

print('This {food} is {adjective} {object}'.format(food = 'cake', adjective = 'very', object = 'good'))

# 
for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 7.2 Reading and Writing files
f = open('workfile','w')

with open('workfile') as f:
	read_data = f.read()

>>>f.read()
'This is the entire file. \n'
>>>f.read()