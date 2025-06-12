# node class gives a single element in linked list
class Node:
    def __init__(self, data):
        self.data=data    
        self.next=None    
# LinkedList class handles all logic of list
class LinkedList:
    def __init__(self):
        self.head = None 

    def add_node(self, data):
        # adds a new node to end list.
        new_node=Node(data)

        # if list is empty then new node becomes the head
        if not self.head:
            self.head = new_node
            return
        current= self.head
        while current.next:
            current =current.next
        current.next=new_node

    def print_list(self):
        if not self.head:
            print("list is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None") 
