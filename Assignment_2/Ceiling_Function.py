import string
import sys


class Tree:

    class Node(object):
        def __init__(self, value, index):
            self.left = None
            self.right = None
            self.value = value
            self.index = index

        def getValue(self):
            return self.value

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def getIndex(self):
            return self.index

        def setValue(self, val):
            self.value = val

        def setLeft(self, xleft):
            self.left = xleft

        def setRight(self, xright):
            self.right = xright

        def setIndex(self, indx):
            self.index = indx

    def __init__(self):
        self.root = None
        #self.index_list = ''

    def add(self, value):
        self.root = Tree.addNode(self, self.root, value, 0)

    def addNode(self, root, value, index):
        if root is None:
            #self.index_list += str(index)
            return Tree.Node(value, index)

        if value <= root.getValue():
            index = (index * 2) + 1
            root.setLeft(Tree.addNode(self, root.getLeft(), value, index))
        else:
            index = (index * 2) + 2
            root.setRight(Tree.addNode(self, root.getRight(), value,index))

        return root

    def printOut(self):
        Tree.printingOut(self.root)

    def printingOut(root):
        print("Root Value: ",root.getValue(), "with index: ", root.getIndex())
        if root.getLeft() is not None:
            print("Left child: ",root.getLeft().getValue())
            Tree.printingOut(root.getLeft())
        else: print("No left child")

        if root.getRight() is not None:
            print("Right child: ", root.getRight().getValue())
            Tree.printingOut(root.getRight())
        else: print("No Right child")

    def indexOut(self):
        if self.root is not None:
            index_string = Tree.makeIndex(self.root)
            return index_string

    def makeIndex(root):
        indexstr = str(root.getIndex())
        if root.getLeft() is not None:
            indexstr += Tree.makeIndex(root.getLeft())
        if root.getRight() is not None:
            indexstr += Tree.makeIndex(root.getRight())
        return indexstr


if __name__ == '__main__':
    x = 0
    index_list = {}
    numbers = input()
    count, size = numbers.split(" ")
    count = int(count)
    size = int(size)
    inputs = 0
    _size = 0
    for in_line in sys.stdin:
        lst = in_line.split()
        tree = Tree()

        for n in lst:
            tree.add(int(n))
            _size += 1
            if _size == size:
                break

        #tree.printOut()
        index_string = tree.indexOut()
        #print( index_string)
        #print(hash(index_string))
        index_list[index_string] = 0;
        # print(indexstring)
        inputs += 1
        if inputs == count:
            break

    print(len(index_list))