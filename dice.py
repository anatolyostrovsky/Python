import random

print("This is a Dice")

x = ["[------------]", "[            ]", "[     O      ]",
    "[   O        ]", "[       O    ]", "[   O    O   ]"]

y = "y"
while y == "y":
    a = random.randint(1,6)

    if a == 1:
        print(x[0])
        print(x[1])
        print(x[2])
        print(x[1])
        print(x[0])
    
    elif a == 2:
        print(x[0])
        print(x[3])
        print(x[1])
        print(x[4])
        print(x[0])
    
    elif a == 4:
        print(x[0])
        print(x[5])
        print(x[1])
        print(x[5])
        print(x[0])
    
    elif a == 3:
        print(x[0])
        print(x[3])
        print(x[2])
        print(x[4])
        print(x[0])
    
    elif a == 5:
        print(x[0])
        print(x[5])
        print(x[2])
        print(x[5])
        print(x[0])
    
    else:
        print(x[0])
        print(x[5])
        print(x[5])
        print(x[5])
        print(x[0])
    y = input("Enter y to roll the dice again")
    

