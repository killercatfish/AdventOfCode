
f = open('input.txt', 'rU')
list = []
for line in f:  ## iterates over the lines of the file
    #print line,

    # get input from file
    input = line.strip('\n')



    list.append(int(input))

print list

#list = [0,3,0,1,-3]
length = len(list)

print length

current = 0
counter = 0

while True:
    counter += 1
    move = list[current]
    if move >= 3:
        list[current] -= 1
    else:
        list[current] += 1
    #print move
    current += move
    if current < 0 or current >= length:
        break

print 'list: ', list
print 'moves: ', counter