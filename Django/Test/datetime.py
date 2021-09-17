import string
from _datetime import datetime

time_stamp = datetime.now()
print(time_stamp)

now = datetime.now()

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)
