# ejercicio 1

from datetime import datetime

now = datetime.now()
print(now)
timestamp = now.timestamp()
print(timestamp)

# ejercicio 2

from datetime import datetime 

now = datetime.now()
t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)

# ejercicio 3

date = "5 December, 2019"
change_date = datetime.strptime(date, "%d %B, %Y")
print(change_date)

# ejercicio 4

from datetime import date

new_year = date(year=2025, month=1, day=1)
now = now.date()
difference = new_year - now
print(difference)

# ejercicio 5

from datetime import datetime

now = datetime.now()
timestamp = datetime(year = 1970, month = 1, day = 1, hour = 0, minute= 0, second = 0)
difference_timestamp = now - timestamp
print(difference_timestamp)





