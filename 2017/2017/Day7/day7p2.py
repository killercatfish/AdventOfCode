from anytree import Node, RenderTree, NodeMixin #https://goo.gl/Ta82Qs
from anytree.exporter import DotExporter
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

#loop through each item and place data into disc_datas then in discs
#also capture a list of everything in the -->, only the base wont be in there
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

#set parents of nodes https://goo.gl/q6NoeS
for i in input:
    current = i.split(" ")
    #print current
    if len(current) > 2:
        #print current[0]
        for i in current[3:]:
            i = i.replace(',','')
            discs[i].BELOW = current[0]

#print discs

first = ""
#find the first level
#print discs.keys()
for i in discs.keys():
    if i not in above:
        #print 'key not in above list' ,i
        first = i
    #print discs.get(i).VALUE

#Build the tree
nodes = {}
nodes[first] = Node(first)
#print nodes

#create all children nodes
for i in discs.keys():
    if i != first:
        #print 'hello'
        nodes[i] = Node(i)
#set the parent of each node
for i in discs.keys():
    if i != first:
        #print 'hello'
        nodes[i].parent = nodes[discs[i].BELOW]

#print RenderTree(nodes[first])

for pre, fill, node in RenderTree(nodes[first]):
    print("%s%s" % (pre,node.name))

#exported to dot file: https://goo.gl/okYF9g
#used this viewer: http://www.webgraphviz.com/
DotExporter(nodes[first]).to_dotfile("tree.dot")

'''
print discs[first]

n1 = Node("n1")

n2 = Node("n2")
n2.parent = n1
#print RenderTree(n1)
'''