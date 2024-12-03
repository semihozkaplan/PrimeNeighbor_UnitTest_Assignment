'''
Created by Neda Topuz
Modified by Semih Özkaplan
'''


def primeNeighbor(upperBound):

    # If upperBound is not an integer, less than 1 or greater than 1000, 0 is returned.
    if not isinstance(upperBound, int) or upperBound <= 1 or upperBound > 1000:
        return 0

    # Function to check if prime or not
    def is_prime(n):
        # Numbers less than 2 are not prime.
        if n < 2:
            return False
        #This loop checks with numbers starting from 2 up to half of n (n // 2 + 1). If a number in this range is an exact divisor of n, then n is not prime.
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False # If the divisor is found, n is not prime.
        return True # If no divisor is found, n is a prime number.

    # Finds and returns the first prime number, starting at upperBound and working backwards to 1.
    for num in range(upperBound, 1, -1):
        if is_prime(num):
            return num

    return 0  # This line is not expected because the loop must find a prime number.


# Example Outputs:
print(primeNeighbor(3))  # Expected Output: 2
print(primeNeighbor(52))  # Expected Output: 47
print(primeNeighbor(89))  # Expected Output: 89
print(primeNeighbor(-7))  # Expected Output: 0
print(primeNeighbor(72))
print(primeNeighbor(978)) # Expected Output: 977
print(primeNeighbor("100"))  # Expected Output: 0
print(primeNeighbor("Hello"))  # Expected Output: 0
