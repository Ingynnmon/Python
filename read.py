# print name of the file
f = open('text.txt', 'wb')

with open('text.txt') as f:
	read_data = f.read()
	print(read_data)
f.close()

# saving structured data with json
import json
json.dumps([1, 'simple', 'list'])