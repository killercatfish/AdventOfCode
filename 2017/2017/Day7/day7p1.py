from enum import Enum
f = open('input.txt', 'rU')
input = []
for line in f:   ## iterates over the lines of the file
	#print line,

	#get input from file
    input.append(line.strip('\n'))

#class to hold data
#had trouble with printing the number as an int using str() so made str
class disc_data():
    def __init__(self,me):
        self.SELF = me
        self.BELOW = ""
        self.ABOVE = []
        self.VALUE = "0"

    #what to do when print a disc_data is called https://goo.gl/YRJPbw
    def __repr__(self):
        #val = str(self.VALUE)
        str = "Disc Name: " + self.SELF + " Value: " + self.VALUE + " Below: " + self.BELOW + " Above: "+ " ".join(self.ABOVE)
        #print str
        return str


discs = {}
above = []


for i in input:
    current = i.split(" ")

    test = disc_data(current[0])
    test.VALUE = current[1][1:-1]

    if len(current) > 2:
        #print len(current)
        above_list = []
        for i in current[3:]:
            i = i.replace(',','')
            above_list.append(i)
            above.append(i)
        test.ABOVE = above_list
    discs[current[0]] = test
        #print test.ABOVE
    #print test

print discs.keys()
for i in discs.keys():
    if i not in above:
        print 'key not in above list' ,i