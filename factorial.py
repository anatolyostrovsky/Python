def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

z = factorial(14)
print(z)


def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    

print(fibonacci(40))
    