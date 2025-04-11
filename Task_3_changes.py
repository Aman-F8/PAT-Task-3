# 1) Find odd or even numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]  # List of numbers to check

# Loop through each number in the list
for number in numbers:
    if number % 2 == 0:  # If number is divisible by 2, it's even
        print(f"{number} is even")  # Print if number is even
    else:
        print(f"{number} is odd")  # Print if number is odd

# 2) Find prime numbers
def is_prime(number):  # Define a function to check if a number is prime
    if number > 1:  # Prime numbers are greater than 1
        # Loop from 2 to half of the number (more efficient than full range)
        for i in range(2, (number // 2) + 1):
            if number % i == 0:  # If divisible, not a prime number
                print(f"{number} is not a prime number")
                break  # Exit the loop if a divisor is found
        else:
            print(f"{number} is a prime number")  # No divisors found, it's prime

prime_check_list = [10, 501, 22, 37, 100, 999, 87, 351]  # List of numbers to check

# Loop through each number in the list and check if it's prime
for value in prime_check_list:
    is_prime(value)

# 3) Find happy numbers
def is_happy_number(n):  # Define a function to check for happy number
    seen_numbers = set()  # Use a set to track numbers we've already seen
    while n != 1 and n not in seen_numbers:  # Loop until n becomes 1 or we detect a cycle
        seen_numbers.add(n)  # Add current number to the seen set
        n = sum(int(digit) ** 2 for digit in str(n))  # Replace number with sum of squares of its digits
    return n == 1  # Return True if happy (n==1), else False

# Function to filter happy numbers from a list
def get_happy_numbers(numbers_list):
    happy_numbers = []  # List to store happy numbers
    for number in numbers_list:
        if is_happy_number(number):  # If the number is happy
            happy_numbers.append(number)  # Add to happy_numbers list
    return happy_numbers  # Return all happy numbers

happy_input_list = [10, 501]  # List of numbers to check
happy_numbers_found = get_happy_numbers(happy_input_list)  # Get happy numbers from the list

# Print all happy numbers found in the list
print("Happy numbers in the list:", happy_numbers_found)

# 4) Find the sum of first and last digit of an integer
def get_first_digit(number):  # Function to find the first digit
    while number >= 10:  # Keep dividing until only one digit remains
        number = number // 10
    return number  # Return the first digit

def get_last_digit(number):  # Function to find the last digit
    return number % 10  # Last digit is the remainder of division by 10

input_number = 1008  # Number to analyze
first_digit = get_first_digit(input_number)  # Get first digit
last_digit = get_last_digit(input_number)  # Get last digit

print("First digit:", first_digit)  # Display first digit
print("Last digit:", last_digit)  # Display last digit
print("Sum of first and last digit:", first_digit + last_digit)  # Print their sum

# 5) Find duplicate values between two lists
list_one = [10, 222, 3]  # First list
list_two = [3, 547, 85]  # Second list

set_one = set(list_one)  # Convert first list to set
set_two = set(list_two)  # Convert second list to set

duplicate_values = set_one & set_two  # Find common elements (intersection)
print("Duplicate values:", duplicate_values)  # Print duplicates

# 5.1) Check for duplicates across three lists
list_a = [12, 24, 36]  # Base list to compare with
list_b = [110, 24, 316]  # List 2
list_c = [12, 204, 36]  # List 3

combined_list = list_b + list_c  # Merge list_b and list_c into one list

# Check each element in the combined list
for element in combined_list:
    if element in list_a:  # If element is also in list_a
        print(f"{element} is a duplicate value")  # Print duplicate
    else:
        print(f"{element} is not a duplicate value")  # Print if not duplicate

# 6) Find the minimum element in a list
unsorted_list = [10, 5, 9, 2, 3]  # Original unsorted list
sorted_list = sorted(unsorted_list)  # Sort the list

print("Sorted list:", sorted_list)  # Display sorted list
print("Minimum value:", min(unsorted_list))  # Use min() to find smallest value
