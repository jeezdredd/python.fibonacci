# Function to calculate the Fibonacci sequence
def fibonacci(n, memo={}):
    if n <= 0:
        return "Invalid input! Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result

# Getting user input
number = int(input("Enter a positive integer: "))

# Validating user input
while number <= 0:
    print("Invalid input! Please enter a positive integer.")
    number = int(input("Enter a positive integer: "))

# Calculating and printing Fibonacci sequence
print("Fibonacci sequence up to", number, ":")
for i in range(1, number+1):
    print(fibonacci(i))
