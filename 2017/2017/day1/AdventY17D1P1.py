f = open('input.txt', 'rU')
input = ""
for line in f:   ## iterates over the lines of the file
	print line, 
	
	#get input from file
	input = line.strip('\n')

list = [int(x) for x in input]
	
print list
sum = 0
for i in range(len(list)):
	next = 0
	if i == len(list)-1:
		next = list[0]
	else:
		next = list[i+1]
		
	if list[i] == next:
		sum += next

print sum