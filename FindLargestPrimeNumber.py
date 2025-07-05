def largest_prime_factor(n):
    # Initialize the smallest prime factor
    i = 2
    # Loop to find the largest prime factor
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Number to find the largest prime factor of
number = 600851475143

# Calculate and print the largest prime factor
largest_factor = largest_prime_factor(number)
print(f"The largest prime factor of {number} is {largest_factor}.")