
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None 

    def append(self, data):
        # If thre is no node in list, create head node
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        # Usual adding of new node which points to the head node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
 # Printing untill we reach our head node again
    def print_list(self):
       
        cur = self.head 
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
# Simple check by checking if head has any data
    def check(self):
        if self.head.data !=None:
            print("List is circular")
        else:
            print("List is not circular")

list = CircularLinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.print_list()
list.check()