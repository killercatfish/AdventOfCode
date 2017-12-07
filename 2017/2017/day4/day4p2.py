
f = open('input.txt', 'rU')
list = []
for line in f:  ## iterates over the lines of the file
    #print line,

    # get input from file
    input = line.strip('\n')

    next = input.split(" ")

    list.append(next)
total = 0
#print list
for l in list:
    count = {}
    for j in l:
        j = ''.join(sorted(j))#part 2 just required this line
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

#didnt need this
def is_anagram(w1,w2):
    if len(w1) != len(w2):
        return False
    w1 = ''.join(sorted(w1))
    w2 = ''.join(sorted(w2))
    print w1, w2
    return w1 == w2

#print is_anagram("hello","lolhe")