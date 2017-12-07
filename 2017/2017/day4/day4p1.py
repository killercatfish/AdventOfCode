f = open('input.txt', 'rU')
list = []
for line in f:  ## iterates over the lines of the file
    #print line,

    # get input from file
    input = line.strip('\n')

    next = input.split(" ")

    list.append(next)
total = 0
print list
for l in list:
    count = {}
    for j in l:
        if j in count:
            count[j]+=1
        else:
            count[j] = 1
    #print count
    counter = 1
    for i in count:
        #print count[i]
        if count[i] != 1:
            counter = 0
            break
    #print counter
    total += counter
print total