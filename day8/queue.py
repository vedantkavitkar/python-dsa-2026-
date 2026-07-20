# ---------------------- QUEUE ----------------------

# Queue follows FIFO (First In First Out)
# Operations:
# 1. Enqueue() -> Insert element
# 2. Dequeue() -> Remove element
# 3. Peek()    -> View front element
# 4. Display() -> Print queue

# size = 5
# queue = [0] * size

# front = -1
# rear = -1

# # ---------------------- Enqueue ----------------------

# def enqueue(value):
#     global front, rear

#     if rear == size - 1:
#         print("Queue Overflow!")

#     else:
#         if front == -1:
#             front = 0

#         rear += 1
#         queue[rear] = value
#         print(value, "Inserted")

# # ---------------------- Dequeue ----------------------

# def dequeue():
#     global front, rear

#     if front == -1 or front > rear:
#         print("Queue Underflow!")

#     else:
#         print(queue[front], "Deleted")
#         front += 1

#         if front > rear:
#             front = rear = -1

# # ---------------------- Peek ----------------------

# def peek():

#     if front == -1:
#         print("Queue is Empty")

#     else:
#         print("Front Element =", queue[front])

# # ---------------------- Display ----------------------

# def display():

#     if front == -1:
#         print("Queue is Empty")

#     else:
#         print("Queue Elements:")

#         for i in range(front, rear + 1):
#             print(queue[i], end=" ")

#         print()

# # ---------------------- Menu ----------------------

# choice = 1

# while choice != 0:

#     print("\n1. Enqueue")
#     print("2. Dequeue")
#     print("3. Peek")
#     print("4. Display")
#     print("0. Exit")

#     choice = int(input("Enter Choice: "))

#     if choice == 1:
#         value = int(input("Enter Value: "))
#         enqueue(value)

#     elif choice == 2:
#         dequeue()

#     elif choice == 3:
#         peek()

#     elif choice == 4:
#         display()

#     elif choice == 0:
#         print("Program Ended")

#     else:
#         print("Invalid Choice")



   class QueueIM:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.size = 5
        self.queue = [0] * self.size

    def enqueue(self, data):
        if self.rear == self.size - 1:
            print("Queue Overflow")
        elif self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
        elif self.front == self.rear:
            print("Deleted:", self.queue[self.front])
            self.front = -1
            self.rear = -1
        else:
            print("Deleted:", self.queue[self.front])
            self.front += 1

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Queue Elements:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


q = QueueIM()

while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("0. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        data = int(input("Enter Element: "))
        q.enqueue(data)

    elif ch == 2:
        q.dequeue()

    elif ch == 3:
        q.display()

    elif ch == 0:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")    