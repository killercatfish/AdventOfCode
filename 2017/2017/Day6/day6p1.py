import re
f = open('input.txt', 'rU')

for line in f:   ## iterates over the lines of the file
	#print line,

	#get input from file
	line = line.strip('\n')

input = [int(x) for x in line.split()]

#input = [0,2,7,0]

configurations = []
cycles = []

def find_largest():
    largest = 0
    index = 0
    for i in range(len(input)):
        if input[i] > largest:
            index = i
            largest = input[i]
            #print input[i], largest
    return index

def redistribute(input):
    configurations.append(input[:])
    cycles.append(0)
    new_input = input
    largest_index = find_largest()
    #print largest_index
    value = input[largest_index]
    distribute_all = value/len(input)
    distribute_some = value % len(input)
    input[largest_index] -= value
    current_location = largest_index
    for i in range(len(input)):
        if current_location + 1 == len(input):
            current_location = 0
        else:
            current_location += 1

        new_input[current_location] = input[current_location] + distribute_all
        if distribute_some > 0:
            new_input[current_location] += 1
            distribute_some -= 1


    return new_input

counter = 0
while input not in configurations:
    counter += 1
    #print input
    input = redistribute(input)
    #increment number of cycles since being added
    for i in range(len(cycles)):
        cycles[i]+=1

    #print configurations
    #print input

print configurations.index(input) #find previous location of most recent input
print cycles[configurations.index(input)] #find the cycles since its insertion
print configurations
print counter