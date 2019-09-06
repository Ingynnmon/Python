#Defining Functions
def fib(n):
     a, b = 0, 1
    while a < n:
            print( a, end = ' ')
            a, b = b, a + b
	 print()

def fib2(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result

#Default Argument Values
i = 5

def f(arg=i):
    print arg

i = 6
f()

def f(a, L = []):
	L.append(a)
	return L

print(f(1))

#Keyword Arguments
def parrot(voltage = 10000, state = 'a stiff', action = 'voom', type = 'bird'):
	print("This parrot wouldn't ", action, end =' ')
	print("if you put ", voltage, " volts throught on you")
	print("Lovely plumage, the ", type)
	print("It's ", state, "!")

parrot(voltage = 10)
parrot(action = "Boom", type = "dead")
parrot('a million', 'bereft of life', 'jump')