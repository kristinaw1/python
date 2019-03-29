#
#Kristina Woods
#COP4533 Algorithmic Design and Development
#
#Assigment 2 b recursion max

import timeit
from timeit import Timer
#linked list
class Node:
    #create nodes
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class OrderedList:
    #create ordered list and methods
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

def test_linkedlist_add():
    #create and add to linked list
    mylist = OrderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    return mylist

def test_linkedlist_search(listN):
    #search linked list
    listN.search(93)
    listN.search(100)  

def test_linkedlist_size(listN):
    #chekc linked list's size
    listN.size()

def test_pythonlist_add():
    #create and add to python list
    listPython = list()
    listPython.append(31)
    listPython.append(77)
    listPython.append(17)
    listPython.append(93)
    listPython.append(26)
    listPython.append(54)

    return listPython


def test_pythonlist_search(listN):
    #search python list
      100 in listN
      93 in listN

def test_pythonlist_size(listN):
    #check python list's size
      len(listN)
      

#main function called to test python and linked lists
def main():
    mylist =test_linkedlist_add()
    listPython = test_pythonlist_add()
    #test create and add functions for linked list
    t= timeit.timeit(test_linkedlist_add, number=1)
    print("Link list time to create and add is ", t)
    
    #test create and add functions for python list
    t2= timeit.timeit(test_pythonlist_add, number=1)
    print("Python list time to create and add is ", t2)

    #check which list was faster
    if t2 > t:
        print("The Python list was faster to create a list")
    elif t2 == t:
        print("Both lists took the same amount of time")
    else:
        print("The Linked list was faster to create a list")

    
    #test search function for linked list
    t3 = Timer(lambda: test_linkedlist_search(mylist))
    t3 =t3.timeit(number=1)
    print("Link list time to search for two variables is  ", t3)


    
    #test search function for python list
    t4 = Timer(lambda: test_pythonlist_search(listPython))
    t4 =t4.timeit(number=1)
    print("Python list time to search for two variables is  ", t4)

   #check which list was faster
    if t4 > t3:
       print("The Python list was faster to search a list")
    elif t4 == t3:
       print("Both lists took the same amount of time")
    else:
        print("The Linked list was faster to search a list")
    

    #test size function for linked list
    t5 = Timer(lambda: test_linkedlist_size(mylist))
    t5 = t5.timeit(number=1)
    print("Link list time to check list size is  ", t5)
    
    #test size function for python list
    t6 = Timer(lambda: test_pythonlist_size(listPython))
    t6 = t6.timeit(number=1)
    print("Python list time to check list size is  ", t6)

    #check which list was faster
    if t6 > t5:
       print("The Python list was faster to determine the size of the list")
    elif t6 == t5:
        print("Both lists took the same amount of time")
    else:
        print("The Linked list was faster to determine the size of the list")
    


main()
