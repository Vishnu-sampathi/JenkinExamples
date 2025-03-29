def is_prime(num):
    # Check if number is less than 2, which is not prime
    if num < 2:
        return False
    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If divisible by any number, it's not prime
            return False
    return True

# Test the function
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

