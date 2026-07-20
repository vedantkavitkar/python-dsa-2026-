class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    head=None
    def InsertAtBeg(self,data):
        newNode=node(data)
        if (self.head==None):
            self.head=newNode
            self.next=None
        else:
            newNode.next=self.head
            self.head=newNode

    def display(self):
        temp=self.head
        print(temp.data)
        while temp!=None:
            print(temp.data,end="-->")
            temp=temp.next
        print()

choice=1

ll=LinkedList()
# li=[12,13,14,15,16,17]
# for ele in li:
#     ll.InsertAtBeg(ele)
# ll.display()
while choice!=0:

    choice=int(input("Enter choice: "))
    match choice:
        case 1:
            data=int(input("Data? :"))
            ll.InsertAtBeg(data)
        case 2:
            ll.display() 