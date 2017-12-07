f = open('input.txt', 'rU')
input = ""
for line in f:   ## iterates over the lines of the file
	print line, 
	
	#get input from file
	input = line.strip('\n')

list = [int(x) for x in input]

double_list = list + list
	
print double_list

sum = 0
next = len(list)/2
for i in range(len(list)):
	
	if list[i] == double_list[i+next]:
		sum += list[i]

print sum