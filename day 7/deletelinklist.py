# ---------------------- Deletion in Linked List ----------------------

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at End
    def insert(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Delete Given Element
    def deleteGiven(self, key):

        temp = self.head

        # If first node contains the key
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        # Search for the key
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # Key not found
        if temp is None:
            print("Element Not Found")
            return

        # Delete node
        prev.next = temp.next
        temp = None

    # Display Linked List
    def display(self):

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("NULL")


# ---------------------- Main ----------------------

ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Before Deletion:")
ll.display()

ll.deleteGiven(20)

print("After Deletion:")
ll.display()


# ---------------------- Delete From Beginning ----------------------

# def deleteBeginning(self):

#     if self.head is None:
#         print("Linked List is Empty")
#         return

#     self.head = self.head.next


# ---------------------- Delete From End ----------------------

# def deleteEnd(self):

#     if self.head is None:
#         print("Linked List is Empty")
#         return

#     if self.head.next is None:
#         self.head = None
#         return

#     temp = self.head

#     while temp.next.next is not None:
#         temp = temp.next

#     temp.next = None


# ---------------------- Delete Given Node ----------------------

# def deleteMiddle(self, key):

#     if self.head is None:
#         print("Linked List is Empty")
#         return

#     if self.head.data == key:
#         self.head = self.head.next
#         return

#     temp = self.head

#     while temp.next is not None and temp.next.data != key:
#         temp = temp.next

#     if temp.next is None:
#         print("Element Not Found")
#         return

#     temp.next = temp.next.next