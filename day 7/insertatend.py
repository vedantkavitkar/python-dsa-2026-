class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    head = None

    def InsertAtBeg(self, data):
        newNode = node(data)

        if self.head == None:
            self.head = newNode
            newNode.next = None
        else:
            newNode.next = self.head
            self.head = newNode

    def InsertAtEnd(self, data):
        newNode = node(data)

        if self.head == None:
            self.head = newNode
            newNode.next = None
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            newNode.next = None
            temp.next = newNode

    def display(self):
        if self.head == None:
            print("Empty !!")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")


choice = 1
l1 = LinkedList()

while choice != 0:
    print("\n1. Insert At Beginning")
    print("2. Insert At End")
    print("3. Display")
    print("0. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        data = int(input("Enter Data: "))
        l1.InsertAtBeg(data)

    elif choice == 2:
        data = int(input("Enter Data: "))
        l1.InsertAtEnd(data)

    elif choice == 3:
        l1.display()

    elif choice == 0:
        print("Program Ended")

    else:
        print("Invalid Choice")

