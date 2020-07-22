#This class contains the function for defining a node 
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
#This class helps in creating the linked list
class LinkedList:
    # Constructor so head points towards null and last node also points to null
    def __init__(self):
        self.head = None
        self.last_node = None
    # This function appends the new node to the end
    def append(self, data):
    # If the last node points to null create new node and last node to head 
        if self.last_node is None: 
            self.head = Node(data)
            self.last_node = self.head
    # else point the next node to new data and point to next data
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    # Displaying the data by iterating throughout the list 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next

    # Function to delete node
    def deleteNode(self, key):  
        # Create a temporary node
        temp = self.head  
        # Check if the head is not pointing to none
        if (temp is not None):  
            # Set the temp data to key since head contains the keyx
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return
        
        while(temp is not None):  
            # Search for the key and keep track of prev.next
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
        # return if node wasn't found
        if(temp == None):  
            return  
        # Unlink the node
        prev.next = temp.next
        temp = None
    def removeDuplicates(self):
        # Create a temp node 
        temp = self.head 
        # if its having nothing return since list is empty
        if temp is None: 
            return
        # Iterate till the next pointer points to None indicating end of the list
        while temp.next is not None:
        # Iterate till you find node having same data
            if temp.data == temp.next.data: 
                new = temp.next.next
                temp.next = None
                temp.next = new 
            # Else go to next node  
            else:
                temp = temp.next
        return self.head 
    # Bubble sorting the list
    def bub_sort_datachange(self):
        # set var end to None
        end = None
        #Loop till head points to None
        while end != self.head:
            p = self.head
            # p will be set to head and we will iterate till end
            while p.next != end:
                # q is the next node
                q = p.next
                # Sorting 
                if p.data > q.data:
                # Assigning the newer values
                    p.data, q.data = q.data, p.data
                #  points to next node
                p = p.next
            # End p points to None to reset pointer
            end = p

list = LinkedList()
list.append(1)
list.append(2)
list.append(4)
list.append(5)
list.append(3)
list.append(0)
list.append(10)
list.removeDuplicates()
list.bub_sort_datachange()
list.display()
