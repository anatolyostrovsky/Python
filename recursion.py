def hola(x):
    if x == 0:
        return
    else:
        print("Hola mundo")
        hola(x-1)
hola(2)

def sum(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + sum(x-1)



z = sum(20)
print(z)