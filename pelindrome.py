# Check whether a number is a palindrome

num = int(input("Enter a number: "))
temp = num          # Store the original number
rev = 0             # Variable to store the reversed number

while num != 0:     # Reverse the number
    rev = rev * 10 + num % 10
    num //= 10

# Compare the original and reversed numbers
if temp == rev:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")