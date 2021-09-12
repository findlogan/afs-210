class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Transversal function for the linked list, displaying all nodes through a print() message
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    # Adding a new node to the end of the linked list, with ref going to the next node
    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

# Create a linkedlist
myLinkedList = LinkedList()

# Add items to linked list
myLinkedList.add_node("PHP")
myLinkedList.add_node("Python")
myLinkedList.add_node("C#")
myLinkedList.add_node("C++")
myLinkedList.add_node("Java")

# Printing linked list
myLinkedList.print_LL()
