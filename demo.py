 # Greatest of three numbers using nested if-else

# Take three numbers as input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Compare the first and second numbers
if a > b:
    # Check if 'a' is also greater than 'c'
    if a > c:
        print("Greatest number is:", a)
    else:
        print("Greatest number is:", c)
else:
    # Check if 'b' is greater than 'c'
    if b > c:
        print("Greatest number is:", b)
    else:
        print("Greatest number is:", c)



        # --------------------------------------------
# Conditional Statements (if, elif, else)
# Program: Find the Greatest of Three Numbers
# Concept: Nested if-else
# --------------------------------------------