x = input("Enter a number: ")
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(int(x)))