def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Replace '5' with the number for which you want to calculate the factorial
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")