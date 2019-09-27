with open('test.txt', 'r') as f:

	scope_to_read =1000
	f_text = f.read(scope_to_read)

	while len(f_text) > 0:
		print(f_text, end = '')

# for n in f:
# 	print(n, end='')

# f = open('test.txt', 'r')
# print(f.name)
# f.close()