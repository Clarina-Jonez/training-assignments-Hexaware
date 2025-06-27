# Node class
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node at the end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    # Display all node values
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

print("Original list:")
ll.display()

ll.reverse()

print("Reversed list:")
ll.display()
