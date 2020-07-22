#This class contains the function for defining a node 
class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

# Class having all functions of linked list 
class DoublyLinkedList: 
    # Constructor so head points towards null and last node also points to null
    def __init__(self):
        self.head = Node()
    
    def append(self,data):
        prevs = []
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current  = self.head 
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            prevs.append(new_node.prev.data)
            new_node.next = None
            print(prevs)
       # Displaying the data by iterating throughout the list 
    def display(self):
        current = self.head
        while current:
            current = current.next
            if current == None:
                return
            print(current.data)
           

    def length(self):
        current = self.head
        len = -1
        while current!=None:
           len = len + 1
           current = current.next 
        print(len)

list = DoublyLinkedList()
list.append(1)
list.append(2)
list.append(3)
list.display()
list.length()