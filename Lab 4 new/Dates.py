#ex 1 Write a Python program to subtract five days from current date.
import datetime 
a = datetime.datetime.now() + datetime.timedelta(days = 5)

print(a)

#ex 2 Write a Python program to print yesterday, today, tomorrow.
import datetime
today = datetime.datetime.now()
print("Today: ", today)

yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
print("Yesterday: ", yesterday)

tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
print("Tomorrow: ", tomorrow)

#ex 3 Write a Python program to drop microseconds from datetime.
import datetime 
a = datetime.datetime.now().replace(microsecond = 0)

print(a)

#ex 4 Write a Python program to calculate two date difference in seconds.
import datetime
date1 = datetime.datetime.now()
date2 = datetime.datetime.now() + datetime.timedelta(days=1)

delta = date2 - date1
print(delta.total_seconds())

