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
        new_node=Node(data)
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
#deleting nodes
    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("List is empty. Nothing to delete.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  
    
        if n <= 0:
            raise Exception("Invalid index. Must be 1 or greater.")

        if n == 1:
            self.head = self.head.next
            return
        current = self.head
        count = 1
        while current and count < n - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            raise Exception("Index out of range. Cannot delete node.")
        current.next = current.next.next
