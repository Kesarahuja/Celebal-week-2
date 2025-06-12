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

# for example usage 
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.add_node(10)
    my_list.add_node(20)
    my_list.add_node(30)
    my_list.add_node(40)

    print("Initial list:")
    my_list.print_list()

    #deleting 
    try:
        my_list.delete_nth_node(2)
        print("\nAfter deleting the 2nd node:")
        my_list.print_list()
    except Exception as e:
        print("Error:",e)
    #deleting node that doesn't exist
    try:
        my_list.delete_nth_node(10)
    except Exception as e:
        print("\nError while deleting 10th node:", e)
    try:
        my_list.delete_nth_node(1)
        my_list.delete_nth_node(1)
        my_list.delete_nth_node(1)
        print("\nAfter deleting all nodes:")
        my_list.print_list()
        my_list.delete_nth_node(1)
    except Exception as e:
        print("\nError while deleting from empty list:", e)


#EXAMPLE OUTPUT
# Initial list:
# 10 -> 20 -> 30 -> 40 -> None
# 10 -> 20 -> 30 -> 40 -> None

# After deleting the 2nd node:
# 10 -> 30 -> 40 -> None
# 10 -> 30 -> 40 -> None

# Error while deleting 10th node: Index out of range. Cannot delete node.
# 10 -> 30 -> 40 -> None
# 30 -> 40 -> None
# 40 -> None

# After deleting all nodes:
# list is empty.

# Error while deleting from empty list: List is empty. Nothing to delete.
