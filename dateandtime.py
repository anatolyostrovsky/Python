import datetime

x = datetime.datetime.now()
#x = datetime.datetime(2024, 5, 21)

#print(x.year)
#print(x.month)
#print(x.day)

print(x.strftime("%A %H %p"))

