>>> cube = []
>>> for i in range(10):
...     cube.append(i**2)
...
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> for i in range(3):
...     cube.append(i**2)
...
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4]
>>> for i in range(3):
...     cube.append(i**3)
...
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 0, 1, 8]

>>> cube.clear()
>>> cube = list(map(lambda x: x**2, range(10)))
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube.clear()
>>> cube = [x**2 for x in range(10)]
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>>


