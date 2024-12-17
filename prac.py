

 # Input:- space-separated integers
l = list(map(int, input("Enter space-separated integers: ").split()))

# MAking  a new list with only even numbers
even_numbers = [num for num in l if num % 2 == 0]

# Printing the original and new lists
print("Original List:", l)
print("Even Numbers List:", even_numbers)





print("__________________________________________________________")

decimal_number = int(input("Enter a positive decimal number: "))

# using loop convert to binary
binary_number = ""#creating an empty string
while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number#storing the remainder
    decimal_number //= 2 #discard the no.

# Print the binary representation
print("Binary Representation:", binary_number)


print("___________________________________________________________")


# Input: Size of the square
n = int(input("Enter the size of the square (n): "))

# Print the hollow square pattern
for i in range(n):
    if i == 0 or i == n - 1:  # Top or bottom row
        print("*" * n)
    else:  # Middle rows with spaces inside
        print("*" + " " * (n - 2) + "*")
