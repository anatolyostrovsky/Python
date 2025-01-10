listtosort = [21, 46, 75, -1, 8, 94, 32, 47, 32, 55, 68, 99, 122]

def bubblesort(mylist):
    lastitem = len(mylist) -1 
    for x in range(0, lastitem):
        for x in range(0, lastitem - x):
            print(mylist)
            if mylist[x]>mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]


    return mylist

print ("Old list", listtosort)
newlist = bubblesort(listtosort).copy()
print("New list: ", newlist)