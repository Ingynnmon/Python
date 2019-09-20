#5 Data Sturctures
fruits = ['orange','apple','pear','banana','coconut']
fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.remove('apple')
fruits

fruits.insert('banana','cucumber')
fruits

fruits.insert(1,'cucumber')
fruits

fruits.sort()
fruits

fruits.pop()
fruits

fruits.pop(1)
fruits

fruits.clear()

fruits.index('apple')

fruits.index('apple',5)

fruits.copy()

a = [1,2,3,4,5,6]
a[len(a): ]

a

fruits.extend(fruits[len(fruits):3])

fruits.extend(fruits[len(fruits):])

#Collection
#5.1.2 Using Lists as Queues
from collections import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.popleft()

queue

#5.1.4 List Comprehension
from math import pi
[str( round ( pi, i )) for i in range(1,6)]

[str(round(pi,6))]

[str(round(pi, ))]

#5.4.1.1 Nested List Comprehensions
#transpose row and column matrix
matrix = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	]

[[row[i] for row in matrix] for i in range(4)]
#(or)
transposed = []
for i in range(4):
	transposed.append([row[i] for row in matrix])

#zip function
list zip(*matrix)

#current date time
import datetime
x = datetime.datetime.now()
x

student = {
		"name" : "Smith",
		"code" : "123",
}