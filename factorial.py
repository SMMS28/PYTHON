def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
n = int(input("Enter a number: "))

print(factorial(n)) # Output: 120
