# A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.
# Find the largest palindrome made from the product of two $3$-digit numbers.

def is_palindrome(n):
    # Check if the number reads the same both ways
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    max_palindrome = 0
    # Iterate through all pairs of 3-digit numbers
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            # Check if the product is a palindrome and larger than the current max
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

# Find and print the largest palindrome made from the product of two 3-digit numbers
largest_palindrome = largest_palindrome_product()
print(f"The largest palindrome made from the product of two 3-digit numbers is {largest_palindrome}.")