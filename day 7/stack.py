# ---------------------- STACK ----------------------

# Stack is a Linear Data Structure.
# It follows the LIFO (Last In First Out) principle.
# Example: Stack of plates.
# Operations:
# 1. Push()  -> Insert element
# 2. Pop()   -> Remove top element
# 3. Peek()  -> View top element
# 4. Display() -> Show all elements

size = 5
stack = [0] * size
top = -1

# ---------------------- Push ----------------------

def push(value):
    global top

    if top == size - 1:
        print("Stack Overflow!")
    else:
        top += 1
        stack[top] = value
        print(value, "Inserted")

# ---------------------- Pop ----------------------

def pop():
    global top

    if top == -1:
        print("Stack Underflow!")
    else:
        print(stack[top], "Removed")
        top -= 1

# ---------------------- Peek ----------------------

def peek():

    if top == -1:
        print("Stack is Empty")
    else:
        print("Top Element =", stack[top])

# ---------------------- Display ----------------------

def display():

    if top == -1:
        print("Stack is Empty")
    else:
        print("Stack Elements:")
        for i in range(top, -1, -1):
            print(stack[i])

# ---------------------- Menu ----------------------

choice = 1

while choice != 0:

    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("0. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        value = int(input("Enter Value: "))
        push(value)

    elif choice == 2:
        pop()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 0:
        print("Program Ended")

    else:
        print("Invalid Choice")