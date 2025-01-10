
def bisearch(mylist, search, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if search == mylist[mid]:
            return mid
        elif search < mylist[mid]:
            return bisearch(mylist, search, start, mid - 1)
        else:
            return bisearch(mylist, search, mid + 1, stop)



mylist = [10, 12, 17, 21, 24, 25, 29, 33, 35, 38, 40, 42, 56, 81, 82, 94, 96, 99]


search = 27

start = 0
stop = len(mylist)

x = bisearch(mylist, search, start, stop)

if x == False:
    print("Item ",search, "Not found!")
else:
    print("Item ", search, "found at index ", x)
