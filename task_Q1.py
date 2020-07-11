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
        final_index = 0
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
            final_index  = final_index + 1
        print(final_index)

    # Displays size of linked list
    def display_size(self):
        current = self.head
        final_index = 0
        while current is not None:
            current = current.next
            final_index  = final_index + 1
        print(final_index)

    """To find the index we compare the key to the data contained in each node 
       and thus increment index till we find our data else print -1"""
    def find_index(self, key):
        current = self.head
        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index = index + 1
        print(-1)
        return 

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


list = LinkedList()
list.append(1)
list.append(2)
list.append(3)
print(list.find_index(1))
list.display_size()
list.deleteNode(2)
list.display_size()
list.display()
