#WAP to insert a node 

class Node :
    def __init__(self, data):
        self.data = data
        self.next = None 




class LinkedList :
    def __init(self):
        self.data = None 

    def insertNodeFirst(self, data):
        first = Node(data)
        first.next = self.head 
        self.head = first 

    def insertNodeLast(self, data):
        last = Node(data)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = last 
    
    def insertNodeMiddle(self, data, prevNode):
        insertNode = Node(data)
        temp = self.head
        while(temp.data != prevNode.data):
            temp = temp.next
        temp.next.next = insertNode.next
        temp.next = insertNode

    def printLList(self):
        temp = self.head
        while temp:
            print (temp.data)
            temp = temp.next


if __name__ == '__main__':
    LList = LinkedList()
    LList.head = Node(1)
    second = Node(2)
    LList.head.next = second
    third = Node(3)
    second.next = third 

    LList.insertNodeFirst(0)
    LList.insertNodeLast(5)
    prevInsertNode = Node(3)
    LList.insertNodeMiddle(4,prevInsertNode)

    LList.printLList()
