# node class represents a single element in the linked list
class Node:
    def __init__(self, data):
        self.data=data    # actual data stored in node
        self.next=None    # Pointer to node 
# LinkedList class handles all the logic related to the list
class LinkedList:
    def __init__(self):
        self.head = None  # initially the list is empty

    def add_node(self, data):
        # adds a new node with the given data to the end of the list.
        new_node=Node(data)

        # if the list is empty then new node becomes the head
        if not self.head:
            self.head = new_node
            return

        # otherwise, find  last node and link the new node there 
        current= self.head
        while current.next:
            current =current.next
        current.next=new_node

