# Armstrong Number:
# A number is Armstrong if the sum of its digits raised to the power of
# number of digits is equal to the original number.
# Example: 153 = 1³ + 5³ + 3³ = 153

num = int(input("Enter a number: "))

temp = num                    # Store original number
count = len(str(num))         # Count number of digits
digit_sum = 0                 # Store the sum

while num != 0:
    digit_sum += (num % 10) ** count   # Add digit power
    num //= 10                        # Remove last digit

# Check Armstrong condition
if temp == digit_sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")