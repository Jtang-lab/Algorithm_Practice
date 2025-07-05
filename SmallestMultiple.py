# Function to calculate the Greatest Common Divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the Least Common Multiple (LCM) of two numbers using GCD
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Function to find the smallest positive number that is evenly divisible by all numbers from 1 to n
def smallest_multiple(n):
    multiple = 1
    for i in range(1, n + 1):
        multiple = lcm(multiple, i)
    return multiple

# Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
smallest_multiple_1_to_20 = smallest_multiple(20)

print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {smallest_multiple_1_to_20}.")

    